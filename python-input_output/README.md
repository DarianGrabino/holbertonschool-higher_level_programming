# Input/Output

El uso del bloque **with** es una práctica recomendada al trabajar con archivos en Python. Proporciona una forma segura y eficiente de manejar la apertura y el cierre del archivo, incluso en situaciones excepcionales. El bloque with se encargará automáticamente de cerrar el archivo una vez que se salga del bloque, sin necesidad de llamar explícitamente al método **close()** del objeto de archivo.

La opción "open" se utiliza en muchos lenguajes de programación para abrir archivos y trabajar con ellos. Al usarla junto con las operaciones de "read" y "write", puedes leer y escribir datos en un archivo específico.

```python
archivo = open("nombre_archivo.txt", "r")
contenido = archivo.read()
```

```python
archivo = open("nombre_archivo.txt", "w")
archivo.write("This is a example")
```
Es importante cerrar el archivo después de terminar de leer o escribir en él.
```python
archivo.close()
```

El parámetro **encoding="utf-8"** se utiliza al leer o escribir en un archivo para especificar la codificación de caracteres que se utilizará
Si el archivo contiene caracteres no ASCII, acentos, caracteres especiales o pertenece a un idioma diferente al inglés, es importante utilizar encoding="utf-8" para asegurarte de que los caracteres se interpreten correctamente. UTF-8 es una codificación ampliamente utilizada y compatible con una amplia gama de caracteres, por lo que es una elección común al leer o escribir archivos de texto.

La opción **"a"** en el contexto de apertura de archivos significa "append". Cuando se abre un archivo en modo **"a"**, se posiciona el puntero de escritura al final del archivo. Esto permite que cualquier contenido nuevo que se escriba se agregue al final del archivo existente, en lugar de sobrescribir el contenido anterior.
```python
open(filename, "a", encoding="utf-8")
```


## JSON 
Es un formato de intercambio de datos ligero y legible por humanos. Es ampliamente utilizado en el desarrollo de aplicaciones para transmitir y almacenar datos estructurados.

Estructura: JSON se basa en una estructura de pares clave-valor. Los datos se organizan en objetos y arrays. Los objetos consisten en pares de clave y valor encerrados entre llaves {}. Por ejemplo: {"nombre": "Juan", "edad": 30}. Los arrays son listas de valores encerrados entre corchetes []. Por ejemplo: [1, 2, 3, 4]. Estos objetos y arrays pueden anidarse para representar estructuras más complejas.

Tipos de datos: JSON admite varios tipos de datos, incluyendo cadenas de texto, números, booleanos, objetos, arrays y valores nulos. Las cadenas de texto deben ir entre comillas dobles, por ejemplo: "Hola, mundo". Los números no requieren comillas, por ejemplo: 42. Los booleanos son representados como true o false. Los objetos y arrays pueden contener otros objetos o arrays, permitiendo la creación de estructuras jerárquicas.

La función **json.dumps()** se utiliza para convertir un objeto de Python en una cadena de texto en formato JSON. 
_Serialización_: Durante el proceso de conversión, json.dumps() realiza la serialización del objeto. La serialización es el proceso de convertir una estructura de datos en una representación que pueda ser almacenada o transmitida. En este caso, se convierte la estructura de datos de Python en una cadena de texto JSON.

La función **json.loads()** se utiliza para cargar una cadena de texto en formato JSON y convertirla en un objeto de Python.
_Deserialización_: Durante el proceso de conversión, json.loads() realiza la deserialización del JSON. La deserialización es el proceso de convertir una representación serializada (en este caso, una cadena de texto JSON) en una estructura de datos en memoria que el programa puede utilizar y manipular

El módulo **sys** proporciona acceso a la lista sys.argv, que es una lista que contiene los argumentos de línea de comandos pasados al script. Example task 7
```
python my_script.py arg1 arg2 arg3
```

El método **get()** es una forma segura de obtener el valor de una clave de un diccionario. Si la clave no existe en el diccionario, en lugar de lanzar una excepción, get() devuelve un valor predeterminado (por defecto None). Example task 11
