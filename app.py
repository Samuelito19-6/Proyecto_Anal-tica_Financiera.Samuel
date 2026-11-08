import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf

# Configuración de la página
st.set_page_config(
    page_title="Risk IT All 4u | Analítica Financiera",
    page_icon="📈",
    layout="wide",
)

# Encabezado principal
st.title("📈 Risk IT All 4u: Comparador Riesgo-Retorno (Acciones vs. ETFs)")
st.markdown(
    "Análisis cuantitativo de rentabilidad vs. volatilidad móvil en acciones y"
    " ETFs para optimización de riesgo."
)

# --- BARRA LATERAL (CONTROLES) ---
st.sidebar.header("⚙️ Parámetros del Análisis")

activos_default = ["NVDA", "QQQ", "NU", "EEM", "MSTR", "IBIT"]
tickers = st.sidebar.multiselect(
    "Selecciona los activos a comparar:",
    options=[
        "NVDA",
        "QQQ",
        "NU",
        "EEM",
        "MSTR",
        "IBIT",
        "AAPL",
        "MSFT",
        "SPY",
        "GLD",
    ],
    default=activos_default,
)

benchmark = st.sidebar.selectbox(
    "Selecciona el ETF Benchmark (para cálculo de Beta):",
    options=tickers if tickers else ["QQQ"],
    index=tickers.index("QQQ") if "QQQ" in tickers else 0,
)

ventana_vol = st.sidebar.slider(
    "Ventana de Volatilidad Móvil (días):", min_value=10, max_value=90, value=30
)
rf_anual = (
    st.sidebar.number_input(
        "Tasa Libre de Riesgo Anual (%):",
        min_value=0.0,
        max_value=15.0,
        value=4.2,
        step=0.1,
    )
    / 100
)

if len(tickers) < 2:
  st.warning(
      "⚠️ Por favor selecciona al menos 2 activos en la barra lateral para"
      " realizar la comparación."
  )
  st.stop()


# --- DESCARGA Y LIMPIEZA DE DATOS ---
@st.cache_data(ttl=3600)
def cargar_datos(lista_tickers):
  df = yf.download(lista_tickers, period="3y", auto_adjust=True)["Close"]
  return df.dropna()


with st.spinner("Descargando y alineando series históricas de mercado..."):
  datos = cargar_datos(tickers)

retornos = np.log(datos / datos.shift(1)).dropna()
dias_anuales = 252

st.caption(
    f"📅 Ventana alineada: **{datos.index.min().date()}** al"
    f" **{datos.index.max().date()}** ({len(datos)} días hábiles comparables)"
)

# --- CÁLCULO DE MÉTRICAS ---
metricas = pd.DataFrame(index=datos.columns)
metricas["Retorno Acumulado (%)"] = ((datos.iloc[-1] / datos.iloc[0]) - 1) * 100
metricas["Retorno Anualizado (%)"] = retornos.mean() * dias_anuales * 100
metricas["Volatilidad Anual (%)"] = retornos.std() * np.sqrt(dias_anuales) * 100
metricas["Ratio de Sharpe"] = (
    (retornos.mean() * dias_anuales) - rf_anual
) / (retornos.std() * np.sqrt(dias_anuales))
metricas["VaR Diario 95% (%)"] = np.percentile(retornos, 5, axis=0) * 100

riqueza = (1 + retornos).cumprod()
drawdowns = (riqueza - riqueza.cummax()) / riqueza.cummax()
metricas["Max Drawdown (%)"] = drawdowns.min() * 100

# Cálculo de Beta respecto al benchmark elegido
var_bench = retornos[benchmark].var()
betas = [
    retornos[col].cov(retornos[benchmark]) / var_bench for col in datos.columns
]
metricas[f"Beta (vs {benchmark})"] = betas

# --- SECCIÓN 1: TABLA RESUMEN ---
st.subheader("📊 Tabla Comparativa de Métricas Cuantitativas")
st.dataframe(
    metricas.style.format("{:.2f}").background_gradient(
        subset=["Ratio de Sharpe"], cmap="RdYlGn"
    ),
    use_container_width=True,
)

# --- SECCIÓN 2: GRÁFICOS PRINCIPALES ---
col1, col2 = st.columns(2)

with col1:
  st.subheader("🎯 Mapa Riesgo vs. Retorno")
  df_scatter = metricas.reset_index().rename(columns={"Ticker": "Activo"})
  df_scatter.columns.values[0] = "Activo"
  fig_scatter = px.scatter(
      df_scatter,
      x="Volatilidad Anual (%)",
      y="Retorno Anualizado (%)",
      text="Activo",
      size="Retorno Acumulado (%)",
      color="Ratio de Sharpe",
      color_continuous_scale="Viridis",
      title="Rentabilidad Anualizada vs. Volatilidad",
  )
  fig_scatter.update_traces(textposition="top center")
  st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
  st.subheader("🚀 Evolución Base 100 (Crecimiento de $100)")
  base_100 = (datos / datos.iloc[0]) * 100
  fig_base = px.line(
      base_100,
      labels={"value": "Valor ($)", "Date": "Fecha"},
      title="Rendimiento Acumulado Normalizado",
  )
  st.plotly_chart(fig_base, use_container_width=True)

# --- SECCIÓN 3: VOLATILIDAD MÓVIL Y DRAWDOWN ---
col3, col4 = st.columns(2)

with col3:
  st.subheader(f"🌊 Volatilidad Móvil ({ventana_vol} días)")
  vol_movil = retornos.rolling(ventana_vol).std() * np.sqrt(dias_anuales) * 100
  fig_vol = px.line(
      vol_movil.dropna(),
      labels={"value": "Volatilidad Anualizada (%)", "Date": "Fecha"},
      title=f"Dinámica de Riesgo (Rolling {ventana_vol}d)",
  )
  st.plotly_chart(fig_vol, use_container_width=True)

with col4:
  st.subheader("📉 Caídas desde Máximos (Drawdown)")
  fig_dd = px.area(
      drawdowns * 100,
      labels={"value": "Caída (%)", "Date": "Fecha"},
      title="Profundidad de Pérdidas Históricas",
  )
  st.plotly_chart(fig_dd, use_container_width=True)

# --- SECCIÓN 4: MATRIZ DE CORRELACIÓN ---
st.subheader("🔗 Matriz de Correlación de Retornos")
corr_matrix = retornos.corr()
fig_corr = px.imshow(
    corr_matrix,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    title="Correlación de Pearson entre Activos",
)
st.plotly_chart(fig_corr, use_container_width=True)
