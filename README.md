# Proyecto de analítica financiera | IX Concurso ITM 2026 |

> **Plantilla de trabajo para estudiantes.** Crea una copia de este archivo en el repositorio de tu equipo y reemplaza los textos entre corchetes. Conserva las preguntas como apoyo durante la investigación. No publiques claves de acceso ni información privada.

**Curso:** Lenguajes de Programación · Ingeniería Financiera  
**Concurso:** 12 de noviembre de 2026  
**Simulacro:** 10 de noviembre de 2026  
**Tecnología:** [Python + Streamlit / R + Shiny / otra interfaz en Python o R]

## 1. Identificación del proyecto

- **Nombre de la aplicación:** Risk IT All 4u
- **Equipo e integrantes:** Samuel David Peinado Guerrero
- **Enlace a la aplicación:** [Pendiente / URL]
- **Repositorio del proyecto:** 
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

**Primera prueba:** [Enlace al notebook o archivo que descarga o consulta datos; indica qué funcionó y qué no]

## 4. Metodología de análisis · S25–S26

**Investiga:** ¿qué indicadores permiten responder la pregunta principal? ¿cómo se calculan? ¿qué interpretación y limitaciones tienen?

| Indicador / técnica | ¿Qué mide? | ¿Por qué lo necesitamos? | Implementación |
|---|---|---|---|
| [Indicador 1] | [Concepto y fórmula, si aplica] | [Relación con la pregunta] | [Archivo o celda] |
| [Indicador 2] | [Concepto y fórmula, si aplica] | [Justificación] | [Pendiente / enlace] |

No es necesario utilizar todos los indicadores estudiados en clase. Selecciona y justifica únicamente los pertinentes.

### Visualizaciones previstas

| Gráfico | Pregunta que ayuda a responder | Variables | Interpretación esperada |
|---|---|---|---|
| [Gráfico 1] | [Pregunta] | [Variables] | [Qué se podrá observar] |
| [Gráfico 2] | [Pregunta] | [Variables] | [Qué se podrá comparar] |

**Primer resultado verificable:** [Enlace a un cálculo o gráfico realizado con datos reales y una interpretación breve]

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
