import os

def limpiar_consola():
    """
    Limpia la pantalla de la consola según el sistema operativo.
    """
    if os.name == "nt":   # Windows
        os.system("cls")
    else:                 # Linux / macOS
        os.system("clear")


def pausar_consola():
    """
    Pausa la ejecución hasta que el usuario presione ENTER.
    """
    input("\nPresione ENTER para continuar...")
