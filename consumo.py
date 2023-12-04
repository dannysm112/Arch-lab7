import sys
import psutil
import subprocess
import time
import matplotlib.pyplot as plt

def ejecutar_binario(binario):
    try:
        proceso = subprocess.Popen(binario)
        print(f"Ejecutando el binario: {binario}")
        return proceso
    except Exception as e:
        print(f"Error al ejecutar el binario: {e}")
        sys.exit(1)

def registrar_consumo(pid, archivo_log):
    try:
        proceso = psutil.Process(pid)
        tiempo_actual = time.time()
        consumo_cpu = proceso.cpu_percent()
        consumo_memoria = proceso.memory_info().rss

        with open(archivo_log, 'a') as file:
            file.write(f"{tiempo_actual},{consumo_cpu},{consumo_memoria}\n")

    except psutil.NoSuchProcess:
        print(f"El proceso con PID {pid} no existe.")
        sys.exit(1)

def graficar_consumo(archivo_log):
    datos = {'tiempo': [], 'cpu': [], 'memoria': []}

    with open(archivo_log, 'r') as file:
        for linea in file:
            tiempo, cpu, memoria = map(float, linea.strip().split(','))
            datos['tiempo'].append(tiempo)
            datos['cpu'].append(cpu)
            datos['memoria'].append(memoria)

    plt.figure(figsize=(10, 6))
    plt.plot(datos['tiempo'], datos['cpu'], label='CPU (%)')
    plt.plot(datos['tiempo'], datos['memoria'], label='Memoria (bytes)')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Consumo')
    plt.legend()
    plt.title('Consumo de CPU y Memoria a lo largo del tiempo')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <ruta_del_ejecutable>")
        sys.exit(1)

    ruta_ejecutable = sys.argv[1]
    archivo_log = 'registro_consumo.log'

    proceso = ejecutar_binario(ruta_ejecutable)

    try:
        while proceso.poll() is None:
            registrar_consumo(proceso.pid, archivo_log)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Proceso interrumpido manualmente.")

    finally:
        proceso.terminate()
        proceso.wait()
        print("Proceso finalizado.")

    graficar_consumo(archivo_log)
