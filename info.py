import os
import sys

def obtener_info_proceso(pid):
    # Comando para obtener información del proceso
    comando = f"ps -p {pid} -o comm,pid,ppid,user,%cpu,%mem,stat,cmd"

    try:
        # Ejecutar el comando y capturar la salida
        salida = os.popen(comando).readlines()[1]
        
        # Dividir la salida en campos
        campos = salida.split()
        
        # Extraer la información requerida
        nombre_proceso = campos[0]
        id_proceso = campos[1]
        id_proceso_padre = campos[2]
        usuario_propietario = campos[3]
        porcentaje_cpu = campos[4]
        consumo_memoria = campos[5]
        estado = campos[6]
        path_ejecutable = campos[7]

        # Imprimir la información
        print(f"Nombre del proceso: {nombre_proceso}")
        print(f"ID del proceso: {id_proceso}")
        print(f"Parent process ID: {id_proceso_padre}")
        print(f"Usuario propietario: {usuario_propietario}")
        print(f"Porcentaje de uso de CPU: {porcentaje_cpu}")
        print(f"Consumo de memoria: {consumo_memoria}")
        print(f"Estado: {estado}")
        print(f"Path del ejecutable: {path_ejecutable}")

    except Exception as e:
        print(f"Error al obtener información del proceso {pid}: {e}")

if __name__ == "__main__":
    # Verificar que se proporcione un argumento (ID del proceso)
    if len(sys.argv) != 2:
        print("Uso: python script.py <PID>")
        sys.exit(1)

    # Obtener el PID desde el argumento de línea de comandos
    pid = sys.argv[1]

    # Llamar a la función para obtener información del proceso
    obtener_info_proceso(pid)
