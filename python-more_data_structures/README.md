# Data Structures

## Dictionary
Es una estructura de datos que permite almacenar elementos en pares clave-valor. Es similar a una lista, pero en lugar de utilizar índices numéricos para acceder a los elementos, se utilizan claves únicas.
Un diccionario se define utilizando llaves {} y los pares clave-valor se separan por dos puntos :. La clave puede ser de cualquier tipo inmutable, como una cadena de texto o un número, y el valor puede ser de cualquier tipo, incluyendo listas, conjuntos, tuplas u otros diccionarios.

## Operadores:
**^** (Diferencia Simétrica): El operador ^ realiza una diferencia simétrica entre dos conjuntos. Devuelve un nuevo conjunto con elementos que están presentes en uno u otro conjunto, pero no en ambos al mismo tiempo.

**&** (Intersección): El operador & se utiliza para encontrar la intersección entre dos conjuntos. Devuelve un nuevo conjunto que contiene solo los elementos comunes a ambos conjuntos.

## Funciones:
**sum(iterable)**: La función sum se utiliza para calcular la suma de los elementos en un iterable (como una lista o un conjunto) y devuelve el resultado.

**set(iterable)**: La función set se utiliza para crear un nuevo conjunto a partir de un iterable. Elimina los elementos duplicados y devuelve el conjunto resultante.

**len(iterable)**: La función len se utiliza para obtener la longitud (número de elementos) de un iterable, como una lista, un conjunto o una cadena de texto.

**sorted(iterable)**: La función sorted se utiliza para ordenar los elementos de un iterable y devuelve una nueva lista con los elementos ordenados.

**update(iterable)**: El método update se utiliza para agregar elementos a un conjunto existente. Acepta un iterable como argumento y agrega sus elementos al conjunto original.

**pop()**: El método pop se utiliza para eliminar y devolver un elemento de un conjunto. Por defecto, elimina y devuelve un elemento aleatorio, pero también se puede proporcionar un elemento específico a eliminar.

**max(iterable)**: La función max se utiliza para encontrar el valor máximo en un iterable. Devuelve el elemento máximo basado en el criterio de ordenamiento utilizado.

**map(function, iterable)**: La función map se utiliza para aplicar una función a cada elemento de un iterable y devuelve un iterador con los resultados.

**filter(function, iterable)**: La función filter se utiliza para filtrar los elementos de un iterable según una función de filtro dada. Devuelve un iterador con los elementos que cumplen con el criterio de filtrado.

**lambda** arguments: expression: La expresión lambda se utiliza para crear funciones anónimas en Python. Estas funciones son pequeñas y pueden ser definidas en una sola línea. Son útiles cuando se requiere una función rápida y simple sin necesidad de definirla formalmente.

## Metodo
**find()** es un método de las cadenas de texto en Python que se utiliza para encontrar la primera aparición de un subtexto dentro de una cadena. Toma como argumento el subtexto que se desea buscar y devuelve el índice de la primera ocurrencia de ese subtexto en la cadena. Si el subtexto no se encuentra en la cadena, se devuelve -1.
