# Información de un proceso
Este script en Python utiliza la biblioteca `psutil` para obtener información sobre un proceso dado su ID. Se brindan detalles como el nombre del proceso, ID del proceso, ID del proceso padre, usuario propietario, porcentaje de uso de CPU, consumo de memoria, estado y ruta del ejecutable.
## Requisitos
-Python 3.  
-Módulos de python: `sys`, `psutil`.  
-El módulo `psutil` se puede instalar usando `pip install psutil`.  
## Funcionamiento del código
### Bibliotecas
`sys`: Proporciona acceso variables y funciones que usa el intérprete. Se usará para recibir parámetros y salir del programa.  
`psutil`: Permite acceder a procesos y el sistema operativo. Brinda datos como CPU, memoria, etc.   
### Funciones
-**(`obtener_informacion_proceso`):**  
Recibe el ID ingresado y utiliza la biblioteca psutil para obtener información sobre el proceso. Maneja la excepción `psutil.NoSuchProcess` en caso de que no se encuentre un proceso con el ID ingresado. Devuelve un diccionario con la información del proceso o un mensaje de error si no se encuentra el proceso.  
### Bloque principal
-**(`if __name__ == "__main__"`):**  
Verifica si el script se está ejecutando como el programa principal. Comprueba si se ingresó el ID correctamente. Intenta convertir el argumento a un entero (ID del proceso). Maneja el error si el ID ingresado no es un número. Llama a la función `obtener_informacion_proceso` e imprime la información del proceso o un mensaje de error, según sea el caso.  
## Ejemplo de uso
El script espera que se le pase el ID de un proceso como argumento en la línea de comandos.  
Si se tiene un proceso en ejecución (por ejemplo, con ID 1234) y se desea obtener información sobre él se debe hacer lo siguiente:  
-Se guarda el código en un archivo llamado, por ejemplo, `informacion.py`.  
-Se ejecuta el script desde la línea de comandos con el ID del proceso como argumento. Así: `python3 informacion.py 1234`.  
## Salida del programa
Si el ID del proceso es válido y existe, se obtendrá información detallada sobre ese proceso. La salida será algo así:  

`Nombre del proceso: ejemplo.exe`  
`ID del proceso: 1234`  
`Parent process ID: 5678`  
`Usuario propietario: usuario`  
`Porcentaje de uso de CPU: 25.0`  
`Consumo de memoria: 123456789`  
`Estado: en ejecución`  
`Path del ejecutable: C:\ruta\a\e\ejemplo.exe`  

**Nota**: estos datos son diferentes para cada proceso.  
Si el ID del proceso no es válido o no se encuentra ningún proceso con ese ID, se mostrará un mensaje de error, como el siguiente:  

`No se encontró un proceso con el ID 1234`  

---
# Monitoreo de un proceso
## Requisitos
## Funcionamiento del código
### Bibliotecas
### Funciones
### Bloque principal
## Ejemplo de uso
## Salida del programa
---
# Consumo de un proceso
## Requisitos
## Funcionamiento del código
### Bibliotecas
### Funciones
### Bloque principal
## Ejemplo de uso
## Salida del programa
