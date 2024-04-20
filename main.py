import subprocess

def ejecutar_comando():
    comando = "shiny run --reload --launch-browser app.py"
    proceso = subprocess.run(comando, shell=True, capture_output=True, text=True)

    # Verifica si hubo errores
    if proceso.returncode != 0:
        print("Ocurrió un error al ejecutar el comando:")
        print(proceso.stderr)
    else:
        print("El comando se ejecutó correctamente.")
        print("Salida:")
        print(proceso.stdout)

# Llamada a la función para ejecutar el comando
ejecutar_comando()
