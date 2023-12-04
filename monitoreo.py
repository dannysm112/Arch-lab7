import sys
import psutil
import subprocess
import time

def ejecutar_proceso(nombre_proceso, comando):
    try:
        proceso = subprocess.Popen(comando.split())
        print(f"Proceso {nombre_proceso} iniciado con PID {proceso.pid}")
        return proceso
    except Exception as e:
        print(f"Error al iniciar el proceso {nombre_proceso}: {e}")
        sys.exit(1)

def verificar_proceso(nombre_proceso):
    for proceso in psutil.process_iter(['pid', 'name']):
        if proceso.info['name'] == nombre_proceso:
            return True
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <nombre_del_proceso> <comando>")
        sys.exit(1)

    nombre_proceso = sys.argv[1]
    comando = sys.argv[2]

    while True:
        if not verificar_proceso(nombre_proceso):
            print(f"El proceso {nombre_proceso} no está en ejecución. Iniciando...")
            proceso = ejecutar_proceso(nombre_proceso, comando)
        time.sleep(5) 
