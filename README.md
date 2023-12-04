# Información de un proceso
Este script en Python permite obtener información sobre un proceso específico. Se brindan detalles como el nombre del proceso, ID del proceso, ID del proceso padre, usuario propietario, porcentaje de uso de CPU, consumo de memoria, estado y ruta del ejecutable.
## Requisitos
-Python 3.  
-Módulos de python: `sys`, `psutil`.  
-El módulo `psutil` se puede instalar usando `pip install psutil`.  
## Funcionamiento del código
### Bibliotecas
-**(`sys`):** Permite acceso variables y funciones que usa el intérprete. Se usará para recibir parámetros y salir del programa.  
-**(`psutil`):** Permite acceder a procesos y el sistema operativo. Brinda datos como CPU, memoria, etc.   
### Funciones
-**(`obtener_informacion_proceso`):**  
Recibe el ID ingresado y utiliza la biblioteca psutil para obtener información sobre el proceso. Maneja la excepción `psutil.NoSuchProcess` en caso de que no se encuentre un proceso con el ID ingresado. Devuelve un diccionario con la información del proceso o un mensaje de error si no se encuentra el proceso.  
### Bloque principal
-**(`if __name__ == "__main__"`):**  
Verifica si el script se está ejecutando como el programa principal. Comprueba si se ingresó el ID correctamente e intenta convertir el argumento a un entero (ID del proceso). Maneja los posibles errores en ambas acciones. Llama a la función `obtener_informacion_proceso` e imprime la información del proceso o un mensaje de error, según sea el caso.  
## Ejemplo de uso
El script espera que se le pase el ID de un proceso como argumento en la línea de comandos. Si se tiene un proceso en ejecución (por ejemplo, con ID 1234) y se desea obtener información sobre él se debe hacer lo siguiente:  
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
`Path del ejecutable: \ruta\ejemplo.exe`  

**Nota:** estos datos son diferentes para cada proceso. Además, se deben tener permisos suficientes para acceder a la información del proceso.  
Si el ID del proceso no es válido o no se encuentra ningún proceso con ese ID, se mostrará un mensaje de error, como el siguiente:  

`No se encontró un proceso con el ID 1234`  

---
# Monitoreo de un proceso
Este script en Python permite monitorear un proceso específico. Si el proceso no está en ejecución se inicia y, luego, se revisa periódicamente el estado del proceso. Si se detuvo, se inicia nuevamente.
## Requisitos
Python 3.  
Módulos de python: `sys`, `psutil`, `subprocess`, `time`.  
El módulo psutil se puede instalar usando `pip install psutil`.  
## Funcionamiento del código
### Bibliotecas
-**(`sys`):** Permite acceso variables y funciones que usa el intérprete. Se usará para recibir parámetros y salir del programa.  
-**(`psutil`):** Permite acceder a procesos y el sistema operativo. Brinda datos como CPU, memoria, etc.  
-**(`subprocess`):** Permite iniciar nuevos procesos y obtener procesos.  
-**(`time`):** Permite utilizar tiempo. Se utilizará para las revisiones periódicas.  
### Funciones
-**(`ejecutar_proceso`):**  
Se encarga de iniciar un nuevo proceso con el comando ingresado. Utiliza `subprocess.Popen` para iniciar el proceso y devuelve el objeto del proceso.  
-**(`monitorear_proceso`):**  
Verifica si un proceso con el nombre dado (`nombre_proceso`) está en ejecución. Itera sobre todos los procesos en ejecución y devuelve `True` si encuentra el proceso y sino devuelve `False`.  
### Bloque principal
-**(`if __name__ == "__main__"`):**
Verifica si el script se está ejecutando como el programa principal. Comprueba si se proporcionan los argumentos correctamente y maneja los posibles errores. Obtiene el nombre del proceso y el comando para ejecutarlo a partir de los argumentos de línea de comandos. En cada iteración del bucle verifica si el proceso está en ejecución. Si el proceso no está en ejecución, lo inicia utilizando la función `ejecutar_proceso`. Luego, espera 5 segundos antes de realizar la siguiente verificación. El programa se interrumpe al ingresar `(Ctrl + C)`.  
## Ejemplo de uso  
El script espera que se le pase el ID de un proceso como argumento en la línea de comandos. Si se tiene un proceso, por ejemplo, con el nombre de `proceso_de_prueba` que dura 6 segundos en ejecución y se desea monitorear su estado se debe hacer lo siguiente:  
-Se guarda el código en un archivo llamado, por ejemplo, `monitoreo.py`.  
-Se ejecuta el script desde la línea de comandos con el nombre del proceso y el comando para ejecutarlo como argumentos. Así: `python3 monitoreo.py proceso_de_prueba "\ruta\proceso_de_prueba.exe"`.  
## Salida del programa
Si el proceso (`proceso_de_prueba`) no está en ejecución, se vería algo como lo siguiente:  
`El proceso proceso_de_prueba no está en ejecución. Iniciando...`  
`El proceso proceso_de_prueba está en ejecución.`  
`El proceso proceso_de_prueba no está en ejecución. Iniciando...`  
`El proceso proceso_de_prueba está en ejecución.`  
`...`
Hasta que se ingrese la entrada `(Ctrl + C)` y se mostrará un mensaje como el siguiente:
`Programa finalizado por el usuario`

**Nota:** La salida se repetirá cada 5 segundos (según el intervalo de espera especificado en `time.sleep(5)`) mientras el programa esté en ejecución. Además, dependiendo del sistema operativo puede ser necesario ajustar el comando para iniciar el proceso y el nombre del proceso. 

---
# Consumo de un proceso
## Requisitos
## Funcionamiento del código
### Bibliotecas
### Funciones
### Bloque principal
## Ejemplo de uso
## Salida del programa
