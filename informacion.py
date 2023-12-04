import sys
import psutil

def obtener_informacion_proceso(pid):
    try:
        proceso = psutil.Process(pid)

        nombre = proceso.name()
        pid = proceso.pid
        ppid = proceso.ppid()
        propietario = proceso.username()
        uso_cpu = proceso.cpu_percent()
        consumo_memoria = proceso.memory_info().rss
        estado = proceso.status()
        path_ejecutable = proceso.exe()

        return {
            'Nombre del proceso': nombre,
            'ID del proceso': pid,
            'Parent process ID': ppid,
            'Usuario propietario': propietario,
            'Porcentaje de uso de CPU': uso_cpu,
            'Consumo de memoria': consumo_memoria,
            'Estado': estado,
            'Path del ejecutable': path_ejecutable
        }

    except psutil.NoSuchProcess:
        return f'No se encontró un proceso con el ID {pid}'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <ID_del_proceso>")
        sys.exit(1)

    pid = int(sys.argv[1])
    informacion = obtener_informacion_proceso(pid)

    if isinstance(informacion, str):
        print(informacion)
    else:
        for clave, valor in informacion.items():
            print(f"{clave}: {valor}")
