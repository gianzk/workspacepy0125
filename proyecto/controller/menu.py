from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
## importando funciones de controlador

from controller.function import *
from config.app import *
## import reports

from controller.reports import *

def menu(app:App):
    console = Console()

    while True:
        # Crear el texto del menú con colores y emojis
        menu_text = Text()
        menu_text.append("\n📊 [bold cyan]Proyecto Datux[/bold cyan]\n", style="underline bold")
        menu_text.append("\n[1] 🟢 Ingestar Data\n", style="green")
        menu_text.append("[2] 📈 Reporte de Ventas\n", style="blue")
        menu_text.append("[3] ❌ Salir\n", style="red")

        # Mostrar el menú en un panel
        console.print(Panel(menu_text, title="🚀 [bold magenta]Menú Principal[/bold magenta]", expand=False, border_style="yellow"))

        # Solicitar opción al usuario
        opcion = Prompt.ask("[bold yellow]Selecciona una opción[/bold yellow]", choices=["1", "2", "3"], default="3")

        # Manejar la opción elegida
        if opcion == "1":
            IngestDataProducts(app)
            pass
            # Aquí puedes llamar a una función de ingesta de datos
        elif opcion == "2":
            GenerateReportVentas(app)
            # Aquí puedes llamar a una función para generar el reporte
        elif opcion == "3":
            pass
            break  # Sale del bucle y termina el programa

# Ejecutar el menú



"""
    Examples:
         1. Reporte de Ventas Totales por Categoría
         2. Top 10 Productos Más Rentables
         3. Productos con Más Descuentos Aplicados
         4. Costos de Envío por Prioridad de Orden
         5. Identificar Órdenes con Pérdidas
         6. Mapa de Calor de Ventas por Región y Categoría

"""