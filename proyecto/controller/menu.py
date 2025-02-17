##Esta libreria mejor el estilo para el ui
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
        menu_text.append("[2] 📈 Reporte de País que Menos Compró\n", style="blue")
        menu_text.append("[3] ❌ Salir\n", style="red")

        # Mostrar el menú en un panel
        console.print(Panel(menu_text, title="🚀 [bold magenta]Menú Principal[/bold magenta]", expand=False, border_style="yellow"))

        # Solicitar opción al usuario
        opcion = Prompt.ask("[bold yellow]Selecciona una opción[/bold yellow]", choices=["1", "2", "3"], default="3")

        # Manejar la opción elegida
        if opcion == "1":
            IngestDataProducts(app)
            pass
        elif opcion == "2":
            GenerateReportPaisQueMenosCompró(app)
        elif opcion == "3":
            pass
            break  # Sale del bucle y termina el programa
        else:
            print("opción no reconocida") #cabe aclarar que la librería ya se encarga de hacer el else pero igual lo pondremos.
