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
