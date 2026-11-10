# Proyecto de analítica financiera | IX Concurso ITM 2026 |

> **Plantilla de trabajo para estudiantes.** Crea una copia de este archivo en el repositorio de tu equipo y reemplaza los textos entre corchetes. Conserva las preguntas como apoyo durante la investigación. No publiques claves de acceso ni información privada.

**Curso:** Lenguajes de Programación · Ingeniería Financiera  
**Concurso:** 12 de noviembre de 2026  
**Simulacro:** 10 de noviembre de 2026  
**Tecnología:** Python + Streamlit

## 1. Identificación del proyecto

- **Nombre de la aplicación:** Risk IT All 4u
- **Equipo e integrantes:** Samuel David Peinado Guerrero
- **Enlace a la aplicación:** [https://w5yuxtwyqgmcvc6imxyo73.streamlit.app/](https://definition-rate-adelaide-states.trycloudflare.com/)
- **Repositorio del proyecto:** https://github.com/Samuelito19-6/Proyecto_Anal-tica_Financiera.Samuel.git
- **Última actualización:** 2026-11-05

## 2. ¿Qué queremos investigar? · S25

**Investiga:** ¿Qué significa analizar el comportamiento histórico de un activo financiero?
R// Significa estudiar de manera cuantitativa los periodos de tiempo en los datos pasados de los activos, para así identificar patrones de comportamiento, niveles de riesgo y rendimiento.

¿Qué preguntas pueden responderse con datos de mercado y cuáles no?
R// ° Responden con precisión matemática al "QUÉ ocurrió" y a la medición del riesgo estadístico, digamos, ¿Qué tan volátil es un activo en comparación con su ETF de referencia? o ¿Cómo se correlacionan los activos entre sí?, etc... 
° Las preguntas que NO responden al "POR QUÉ" cualitativo ni garantizan sucesos futuros, es decir: ¿Cuánto valdrá la acción o el ETF mañana o el próximo año?, ¿Cómo reaccionará el activo ante eventos sin precedentes?, etc...

- **Situación o fenómeno de interés:** Deseamos comprender cómo difiere el perfil de riesgo y rendimiento entre activos de gestión activa y activos de gestión pasiva en tres sectores clave: tecnología de gran capitalización, mercados emergentes/commodities y criptoactivos.
  
- **Pregunta principal:** ¿En qué medida la inversión en acciones individuales de alto crecimiento (NVDA, NU, MSTR) compensa la volatilidad adicional y el riesgo a la baja en comparación con sus respectivos ETFs de referencia (QQQ, EEM, IBIT) durante los últimos 3 años de datos históricos diarios?
- **Objetivo del análisis:** Comparar cuantitativamente el riesgo y la rentabilidad ajustada por riesgo entre acciones individuales y ETFs representativos, evaluando además el efecto de la diversificación al construir un portafolio.
  
- **Importancia financiera:** Comprender este comportamiento es crucial para la toma de decisiones de inversión y la gestión de portafolios. Permite a los inversionistas determinar si la selección de acciones individuales genera un rendimiento superior suficiente para justificar la volatilidad adicional asumida.
- 
- **Preguntas complementarias:** ¿Cómo cambian las matrices de correlación entre estos activos en periodos de alta volatilidad frente a periodos de estabilidad de mercado?
- 
> **Comprueba:** ¿tu pregunta identifica activos, variables y un período de estudio? ¿Es posible responderla con datos disponibles?
> R// Sí, la pregunta satisface plenamente ambos criterios ya que ve activos claramente delimitados: Compara 3 pares específicos de gestión activa vs. pasiva, y cuenta con disponibilidad de datos suficiente para poder darle solución.

## 3. Activos, datos y alcance · S25

**Investiga:** ¿qué activos se ajustan a tu pregunta? ¿qué datos históricos existen? ¿qué frecuencia, período y fuente utilizarás?

| Activo | Símbolo o ticker | Tipo | Razón para incluirlo |
|---|---|---|---|
| NVIDIA Corp. | NVDA| Acción | Gestión activa en tecnología de alto crecimiento e impacto en Inteligencia Artificial |
| Invesco QQQ Trust | QQQ | ETF | Diversificación en el sector tecnológico |
| Nu Holdings Ltd. | NU | Acción |Emergente líder en América Latina con fuerte dinamismo |
| iShares MSCI | EEM | ETF | Diversificado de gestión pasiva que rastrea economías en desarrollo |
| MicroStrategy Inc. | MSTR | Acción |Gestión activa con volatilidad extrema que actúa como proxy corporativo |
| iShares Bitcoin Trust| IBIT | ETF | Ideal para comparar el riesgo entre una acción expuesta a criptoactivos y un ETF regulado |


- **Fuente de datos:** Yahoo Finance API a través de la librería yfinance en Python (Documentación de yfinance)
- **Período:** 3 años (Noviembre 2023 – Noviembre 2026).
- **Frecuencia:** Diaria
- **Variables disponibles:** Fecha, Precios de Apertura, Máximo, Mínimo, Cierre, Cierre Ajustado y Volumen.
- **Limitaciones de los datos:** El ETF IBIT comenzó a cotizar a principios de 2024, por lo que su serie histórica es más corta que la de los demás activos.

- **Primera prueba:** Enlace: https://github.com/Samuelito19-6/Proyecto_Anal-tica_Financiera.Samuel/blob/4f3cac808996d518638f9773424347ef208f2d71/Primera_Prueba_Datos_yf.ipynb
  - **Se ejecutó** la extracción de datos diarios a 3 años mediante `yfinance` en Google Colab.
  - **Funcionó:** Descarga completa de 753 registros de precios de cierre ajustados y exportación a `datos_historicos_limpios.csv`.
  - **Ajuste realizado:** Se detectaron exactamente 44 registros nulos iniciales en `IBIT` (comenzó a cotizar el 11 de enero de 2024), por lo que se aplicó `dropna()` para alinear las 6 series temporales en una ventana comparable de **709 días hábiles** 
    
## 4. Metodología de análisis · S25–S26

**Investiga:** ¿qué indicadores permiten responder la pregunta principal? ¿cómo se calculan? ¿qué interpretación y limitaciones tienen?

| Indicador / técnica | ¿Qué mide? | ¿Por qué lo necesitamos? | Implementación |
|---|---|---|---|
| **Retorno Logarítmico y Anualizado** | Variación porcentual continua del precio: $r_t = \ln(P_t / P_{t-1})$ y su proyección anual $E[R] = \bar{r} \times 252$. | Permite comparar en igualdad de condiciones el crecimiento de acciones individuales frente a ETFs durante la ventana de 709 días hábiles. | [Primera_Prueba_Datos_yf.ipynb](https://github.com/Samuelito19-6/Proyecto_Anal-tica_Financiera.Samuel/blob/4f3cac808996d518638f9773424347ef208f2d71/Primera_Prueba_Datos_yf.ipynb) |
| **Volatilidad Anualizada ($\sigma$) y Móvil** | Dispersión de los retornos diarios escalada al año: $\sigma_{anual} = \sigma_{diaria} \times \sqrt{252}$. | Cuantifica el riesgo total asumido en acciones de alto crecimiento (`NVDA`, `NU`, `MSTR`) frente a la diversificación de sus ETFs (`QQQ`, `EEM`, `IBIT`). | Pendiente en `app.py` (Streamlit) |
| **Ratio de Sharpe** | Rentabilidad excedente por cada unidad de riesgo asumido: $SR = \frac{E[R] - R_f}{\sigma_{anual}}$. | Responde directamente a la pregunta principal: determina si la rentabilidad extra de las acciones individuales realmente compensa su mayor volatilidad. | Pendiente en `app.py` (Streamlit) |
| **Valor en Riesgo (VaR Histórico 95%)** | Pérdida máxima esperada en un día normal de negociación con un 95% de confianza. | Evalúa el riesgo de cola o escenarios adversos diarios, fundamental para comparar activos extremos como `MSTR` contra `IBIT`. | Pendiente en `app.py` (Streamlit) |
| **Drawdown Máximo** | Caída porcentual máxima registrada desde un pico histórico hasta un valle posterior antes de alcanzar un nuevo máximo. | Mide la peor pérdida acumulada que habría sufrido un inversionista en cada par Acción vs. ETF durante el período 2024–2026. | Pendiente en `app.py` (Streamlit) |
| **Coeficiente Beta ($\beta$) y Correlación** | Sensibilidad del activo respecto a su benchmark de mercado: $\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$. | Permite identificar qué tan amplificados son los movimientos de cada acción respecto a su ETF de referencia y evaluar beneficios de diversificación. | Pendiente en `app.py` (Streamlit) |

No es necesario utilizar todos los indicadores estudiados en clase. Selecciona y justifica únicamente los pertinentes.

### Visualizaciones previstas

| Gráfico | Pregunta que ayuda a responder | Variables | Interpretación esperada |
|---|---|---|---|
| **Mapa Dispersión Riesgo vs. Retorno** | ¿Qué activos ofrecen mejor relación rentabilidad-riesgo y cuáles presentan volatilidad excesiva sin compensación? | Volatilidad Anualizada (eje X) vs. Retorno Anualizado (eje Y). | Ubicación visual de cada par Acción vs. ETF; se espera que los ETFs (`QQQ`, `EEM`, `IBIT`) se sitúen más a la izquierda (menor riesgo) que sus acciones pares. |
| **Evolución de Retorno Acumulado (Base 100)** | ¿Cómo ha evolucionado el capital invertido en gestión activa frente a gestión pasiva a lo largo del tiempo? | Fecha (eje X) vs. Crecimiento de $100 invertidos (eje Y). | Comparación directa de tendencias alcistas, velocidad de recuperación y brechas de rendimiento entre cada acción y su ETF. |
| **Volatilidad Móvil (*Rolling Volatility* 30d)** | ¿En qué momentos del período 2024–2026 se disparó la incertidumbre y qué tan persistente fue? | Fecha (eje X) vs. Desviación estándar móvil anualizada a 30 días (eje Y). | Identificación de picos de estrés de mercado y comprobación de cómo los ETFs amortiguan las oscilaciones bruscas frente a acciones individuales. |
| **Gráfico de Caídas (*Underwater / Drawdown*)** | ¿Cuál es la profundidad y duración de las peores caídas de cada activo? | Fecha (eje X) vs. Porcentaje de caída desde máximos históricos (eje Y). | Visualización clara del riesgo a la baja y comparación del tiempo de recuperación entre activos individuales y ETFs. |
| **Matriz de Correlación (*Heatmap*)** | ¿Qué tan diversificado está realmente el conjunto de activos seleccionados? | Coeficiente de correlación de Pearson entre los 6 activos. | Detección de pares altamente correlacionados (ej. `MSTR`–`IBIT` o `NVDA`–`QQQ`) frente a activos con baja correlación útil para optimizar portafolios. |

**Primer resultado verificable:** https://colab.research.google.com/drive/1-YiZ39ITof0xbQtT641O7II8fVfvbhGa?usp=sharing

## 5. Diseño de la aplicación · S25

**Investiga:** ¿cómo se construyen controles, gráficos y métricas con la herramienta elegida? ¿qué sucede cuando el usuario modifica una selección?

- **Usuarios previstos:** [Quién podría consultar la aplicación]
- **Entradas y filtros:** [Activos, fechas, parámetros...]
- **Secciones de la interfaz:** [Pantalla principal, comparación, riesgo, etc.]
- **Resultados visibles:** [Gráficos, tablas, indicadores y explicaciones]
- **Interacción principal:** [Describe qué cambia cuando el usuario modifica un control]

**Flujo previsto:**  
Selección de activos y parámetros → Obtención de datos → Preparación y cálculos → Visualización → Interpretación.

**Boceto o esquema:** [Inserta una imagen o enlace al diseño, por ejemplo `docs/boceto.png`]

**Decisión técnica:** [¿Por qué usarás Python o R y qué biblioteca de aplicación elegiste?]

## 6. Construcción y pruebas · S26 (5 de noviembre)

Actualiza esta sección durante el laboratorio de desarrollo.

- **Componentes implementados:** [Qué funciona realmente]
- **Cómo ejecutar la aplicación:** [Comandos, dependencias y pasos]
- **Dependencias:** [Archivo `requirements.txt`, `renv.lock` u otro]
- **Pruebas realizadas:** [Caso probado, resultado esperado y resultado obtenido]
- **Errores conocidos y cómo se resolvieron:** [Explicación]
- **Pendientes antes del simulacro:** [Tareas concretas]

> No afirmes que una función está implementada si aún no ha sido probada.

## 7. Hallazgos e interpretación · S26–S28

Para cada hallazgo importante, registra:

1. **Evidencia:** [Gráfico, tabla o indicador con enlace]
2. **Qué muestra:** [Describe el comportamiento observado]
3. **Interpretación financiera:** [Explica su significado en relación con la pregunta]
4. **Limitaciones:** [Qué no puedes concluir de los datos]

**Conclusión provisional o final:** [Respuesta sustentada a la pregunta principal]

> Los resultados históricos no garantizan rendimientos futuros.

## 8. Simulacro · S27 (10 de noviembre)

**Guion de sustentación (3–5 minutos):**
- Problema financiero y activos.
- Datos y metodología.
- Demostración de interactividad.
- Hallazgos e interpretación.
- Conclusión y limitaciones.

**Retroalimentación recibida:** [Observaciones del docente o compañeros]

| Ajuste necesario | Responsable | Estado |
|---|---|---|
| [Ajuste] | [Integrante] | [Pendiente / en proceso / resuelto] |

## 9. Presentación final · S28 (12 de noviembre)

- **Enlace funcional de la aplicación:** [URL]
- **Versión final / commit:** [Enlace]
- **Evidencia de presentación:** [Enlace autorizado]
- **Conclusiones finales:** [Síntesis]
- **Limitaciones y posibles mejoras:** [Descripción]

## 10. Bitácora de trabajo y aportes

| Fecha | Integrante(s) | Investigación o decisión | Avance técnico / evidencia | Próximo paso |
|---|---|---|---|---|
| 2026-11-03 | [Nombre] | [Qué investigamos] | [Enlace a código o documento] | [Acción] |
| 2026-11-05 | [Nombre] | [Decisiones] | [Evidencia] | [Acción] |
| 2026-11-10 | [Nombre] | [Retroalimentación] | [Cambio] | [Acción] |

## Recursos de consulta

- [Libro de programación y analítica financiera del curso](https://github.com/vyolete/proyecto_analitica_financiera)
- [Documentación de yfinance](https://ranaroussi.github.io/yfinance/)
- [Documentación de pandas](https://pandas.pydata.org/docs/)
- [Documentación de Streamlit](https://docs.streamlit.io/)
- [Documentación de Shiny para R](https://shiny.posit.co/r/)

**Uso del documento:** En S25 desarrolla especialmente las secciones 2 a 5 y registra tu primera prueba; en S26, S27 y S28 actualiza el mismo README. No dupliques información en entregas separadas.
