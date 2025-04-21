import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(page_title="Campaña de Matriculaciones", layout="wide")

# Título
st.title("Dashboard de Campaña de Matriculaciones (21/04/25 - 31/07/25)")

# Cargar datos (sustituir por conexión a Google Sheets o CSV desde CRM)
@st.cache_data
def load_data():
    # Ejemplo de datos (reemplazar con datos reales)
    data = pd.DataFrame({
        "Fecha": pd.date_range(start="2025-04-21", end="2025-07-31", freq="D"),
        "Leads_Total": [50, 60, 70, 80, 100, 120, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500, 3550, 3600, 3650, 3700, 3750, 3800, 3850, 3900, 3950, 4000, 4050, 4100, 4150, 4200, 4250, 4300, 4350, 4400, 4450, 4500, 4550, 4600, 4650, 4700, 4750, 4800, 4850, 4900, 4950, 5000, 5050],
        "Leads_B2C": [30, 35, 40, 45, 60, 70, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470, 1500, 1530, 1560, 1590, 1620, 1650, 1680, 1710, 1740, 1770, 1800, 1830, 1860, 1890, 1920, 1950, 1980, 2010, 2040, 2070, 2100, 2130, 2160, 2190, 2220, 2250, 2280, 2310, 2340, 2370, 2400, 2430, 2460, 2490, 2520, 2550, 2580, 2610, 2640, 2670, 2700, 2730, 2760, 2790, 2820, 2850, 2880, 2910, 2940, 2970, 3000, 3030],
        "Leads_B2B": [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020],
        "Leads_NdP": [5, 5, 5, 5, 5, 10, 15, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000],
        "Matriculaciones_Total": [0, 0, 0, 0, 0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960],
        "Matriculaciones_BIM": [0, 0, 0, 0, 0, 3, 5, 7, 8, 10, 12, 13, 15, 17, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 53, 57, 60, 63, 67, 70, 73, 77, 80, 83, 87, 90, 93, 97, 100, 103, 107, 110, 113, 117, 120, 123, 127, 130, 133, 137, 140, 143, 147, 150, 153, 157, 160, 163, 167, 170, 173, 177, 180, 183, 187, 190, 193, 197, 200, 203, 207, 210, 213, 217, 220, 223, 227, 230, 233, 237, 240, 243, 247, 250, 253, 257, 260, 263, 267, 270, 273, 277, 280, 283, 287, 290, 293, 297, 300, 303, 307, 310, 313, 317, 320],
        "Matriculaciones_Energias": [0, 0, 0, 0, 0, 3, 5, 7, 8, 10, 12, 13, 15, 17, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 53, 57, 60, 63, 67, 70, 73, 77, 80, 83, 87, 90, 93, 97, 100, 103, 107, 110, 113, 117, 120, 123, 127, 130, 133, 137, 140, 143, 147, 150, 153, 157, 160, 163, 167, 170, 173, 177, 180, 183, 187, 190, 193, 197, 200, 203, 207, 210, 213, 217, 220, 223, 227, 230, 233, 237, 240, 243, 247, 250, 253, 257, 260, 263, 267, 270, 273, 277, 280, 283, 287, 290, 293, 297, 300, 303, 307, 310, 313, 317, 320],
        "Matriculaciones_Medioambiental": [0, 0, 0, 0, 0, 4, 5, 6, 9, 10, 11, 14, 15, 16, 20, 24, 26, 30, 34, 36, 40, 44, 46, 50, 54, 56, 60, 64, 66, 70, 74, 76, 80, 84, 86, 90, 94, 96, 100, 104, 106, 110, 114, 116, 120, 124, 126, 130, 134, 136, 140, 144, 146, 150, 154, 156, 160, 164, 166, 170, 174, 176, 180, 184, 186, 190, 194, 196, 200, 204, 206, 210, 214, 216, 220, 224, 226, 230, 234, 236, 240, 244, 246, 250, 254, 256, 260, 264, 266, 270, 274, 276, 280, 284, 286, 290, 294, 296, 300, 304, 306, 310, 314, 316, 320],
        "Visitas_Landing": [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1320, 1340, 1360, 1380, 1400, 1420, 1440, 1460, 1480, 1500, 1520, 1540, 1560, 1580, 1600, 1620, 1640, 1660, 1680, 1700, 1720, 1740, 1760, 1780, 1800, 1820, 1840, 1860, 1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020, 2040, 2060, 2080, 2100, 2120, 2140, 2160, 2180],
        "Empresas_Contactadas": [10, 12, 14, 16, 18, 20, 22, 24, 26,  LY, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218],
        "Publicaciones_RRSS": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        "NdP_Enviadas": [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218]
    })
    return data

data = load_data()

# Filtros
st.sidebar.header("Filtros")
period = st.sidebar.selectbox("Período", ["Diario", "Semanal", "Mensual", "Total"])
channel = st.sidebar.multiselect("Canal", ["Todos", "B2C", "B2B", "NdP"], default="Todos")
course = st.sidebar.multiselect("Curso", ["Todos", "BIM", "Energías Renovables", "Gestión Medioambiental"], default="Todos")
date_range = st.sidebar.date_input("Rango de fechas", [datetime(2025, 4, 21), datetime(2025, 7, 31)])

# Filtrar datos
filtered_data = data[(data["Fecha"] >= pd.to_datetime(date_range[0])) & (data["Fecha"] <= pd.to_datetime(date_range[1]))]

# Resumen General
st.header("Resumen General")
col1, col2, col3 = st.columns(3)
col1.metric("Matriculaciones", f"{filtered_data['Matriculaciones_Total'].sum()}/3100", f"{filtered_data['Matriculaciones_Total'].sum()/3100*100:.1f}%")
col2.metric("Leads", f"{filtered_data['Leads_Total'].sum()}/7750", f"{filtered_data['Leads_Total'].sum()/7750*100:.1f}%")
col3.metric("Visitas Landing", f"{filtered_data['Visitas_Landing'].sum()}/15500", f"{filtered_data['Visitas_Landing'].sum()/15500*100:.1f}%")

# Barra de progreso
fig_progress = go.Figure(go.Indicator(
    mode="gauge+number",
    value=filtered_data["Matriculaciones_Total"].sum(),
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Progreso Matriculaciones"},
    gauge={'axis': {'range': [0, 3100]}, 'bar': {'color': "blue"}, 'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 3100}}
))
st.plotly_chart(fig_progress)

# Gráfico circular por curso
fig_course = px.pie(
    values=[filtered_data["Matriculaciones_BIM"].sum(), filtered_data["Matriculaciones_Energias"].sum(), filtered_data["Matriculaciones_Medioambiental"].sum()],
    names=["BIM", "Energías Renovables", "Gestión Medioambiental"],
    title="Distribución por Curso"
)
st.plotly_chart(fig_course)

# Progreso Diario
if period == "Diario":
    st.header("Progreso Diario")
    fig_daily = px.line(filtered_data, x="Fecha", y=["Leads_Total", "Matriculaciones_Total", "Visitas_Landing"], title="Tendencias Diarias")
    st.plotly_chart(fig_daily)
    st.dataframe(filtered_data[["Fecha", "Leads_Total", "Matriculaciones_Total", "Visitas_Landing", "Empresas_Contactadas", "Publicaciones_RRSS", "NdP_Enviadas"]])

# Progreso Semanal
if period == "Semanal":
    st.header("Progreso Semanal")
    weekly_data = filtered_data.resample("W", on="Fecha").sum().reset_index()
    fig_weekly = px.bar(weekly_data, x="Fecha", y=["Leads_B2C", "Leads_B2B", "Leads_NdP"], title="Leads por Canal (Semanal)")
    st.plotly_chart(fig_weekly)
    st.dataframe(weekly_data[["Fecha", "Leads_Total", "Matriculaciones_Total", "Visitas_Landing"]])

# Progreso Mensual
if period == "Mensual":
    st.header("Progreso Mensual")
    monthly_data = filtered_data.resample("M", on="Fecha").sum().reset_index()
    fig_monthly = px.area(monthly_data, x="Fecha", y="Matriculaciones_Total", title="Matriculaciones Acumuladas (Mensual)")
    st.plotly_chart(fig_monthly)
    st.dataframe(monthly_data[["Fecha", "Leads_Total", "Matriculaciones_Total", "Visitas_Landing"]])

# Detalles por Canal
st.header("Detalles por Canal")
fig_channel = px.pie(
    values=[filtered_data["Leads_B2C"].sum(), filtered_data["Leads_B2B"].sum(), filtered_data["Leads_NdP"].sum()],
    names=["B2C", "B2B", "NdP"],
    title="Distribución de Leads por Canal"
)
st.plotly_chart(fig_channel)

# Embudo de Chatbot
st.header("Embudo de Chatbot")
fig_funnel = go.Figure(go.Funnel(
    y=["Visitas Landing", "Leads Total", "Matriculaciones Total"],
    x=[filtered_data["Visitas_Landing"].sum(), filtered_data["Leads_Total"].sum(), filtered_data["Matriculaciones_Total"].sum()],
    textinfo="value+percent initial"
))
st.plotly_chart(fig_funnel)