# Python - if/else, loops, functions

Bucles for anidados:
Los bucles for anidados se utilizan para realizar iteraciones múltiples en una estructura de bucle. Se pueden utilizar para recorrer matrices, listas de listas u otras estructuras de datos anidadas.

Ejemplo:
```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(elemento)
```        
Este código imprimirá cada elemento de la matriz.

Bucle while:
El bucle while se utiliza para repetir un bloque de código mientras se cumpla una condición específica.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```   
Este código imprimirá los números del 0 al 4, ya que se ejecutará mientras la variable contador sea menor que 5.

Sentencia if y else:
La sentencia if se utiliza para ejecutar un bloque de código si se cumple una condición determinada. La sentencia else se utiliza para ejecutar un bloque de código alternativo si la condición del if no se cumple.

Ejemplo:
```python
numero = 10
if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo o cero")
```    
Este código imprimirá "El número es positivo" si numero es mayor que cero, de lo contrario imprimirá "El número es negativo o cero".
