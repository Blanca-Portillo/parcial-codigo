import plotly.graph_objects as go
from plotly.subplots import make_subplots


meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
#Datos de ventas 
ventas_clavos = [200, 180, 220, 210, 250, 230, 270, 240, 260, 280, 300, 250]  
ventas_tornillos = [180, 190, 170, 200, 210, 190, 230, 220, 210, 250, 240, 230] 
ventas_herramientas = [150, 140, 160, 170, 180, 160, 190, 200, 180, 220, 210, 200]  

# Crear subplots (gráficos múltiples en un solo tablero)
fig = make_subplots(
    rows=3, cols=2,  
    subplot_titles=("VENTAS DE HERRAMIENTAS POR MES", "VENTAS DE CLAVOS POR MES", 
                    "VENTAS DE TORNILLOS POR MES", "VENTAS TOTALES POR MES",
                    "COMPARACION DE VENTAS DE CADA PRODUCTO DE CADA MES ")
)

# Gráfico de barras para Ventas 
fig.add_trace(go.Bar(x=meses, y=ventas_herramientas, name="Herramientas", marker_color='orange'), row=1, col=1)
fig.add_trace(go.Bar(x=meses, y=ventas_clavos, name="Clavos", marker_color='blue'), row=1, col=2)
fig.add_trace(go.Bar(x=meses, y=ventas_tornillos, name="Tornillos", marker_color='green'), row=2, col=1)


# Gráfico de línea de la tendencia total de ventas 
total_ventas = [a + b + c for a, b, c in zip(ventas_clavos, ventas_tornillos, ventas_herramientas)]
fig.add_trace(go.Scatter(x=meses, y=total_ventas, mode='lines', name="Total Ventas", line=dict(color='purple', width=4)), row=2, col=2)

# Gráfico de dispersión para comparar los tres productos 
fig.add_trace(go.Scatter(x=meses, y=ventas_clavos, mode='lines+markers', name="Clavos"), row=3, col=1)
fig.add_trace(go.Scatter(x=meses, y=ventas_tornillos, mode='lines+markers', name="Tornillos"), row=3, col=1)
fig.add_trace(go.Scatter(x=meses, y=ventas_herramientas, mode='lines+markers', name="Herramientas"), row=3, col=1)

# diseño del tablero
fig.update_layout(
    title_text="Análisis de Ventas Mensuales de Ferreteria Super Santa Helena", 
    height=900, 
    showlegend=True,
    title_font_size=24
)


fig.show()
