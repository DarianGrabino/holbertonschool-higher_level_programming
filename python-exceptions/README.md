# Python - Exceptions
Las excepciones son utilizadas para manejar errores y situaciones excepcionales que pueden ocurrir durante la ejecución de un programa. Permiten capturar y controlar errores de manera estructurada.

**try**: El bloque try se utiliza para contener el código que puede generar una excepción. Dentro de este bloque, se ejecutan una o varias instrucciones que podrían producir un error.

**except**: El bloque except se utiliza para capturar y manejar una excepción específica que puede ocurrir dentro del bloque try. En este bloque, se define el código que se ejecutará si se produce la excepción especificada.

Ejemplo de uso de try y except:

```python
try:
    # Código que puede generar una excepción
    resultado = dividir(10, 0)
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("No se puede dividir entre cero. Por favor, ingrese otro valor.")
```

### Excepciones en Python:
En Python, existen diversos tipos de excepciones integradas que se utilizan para manejar errores y situaciones excepcionales durante la ejecución de un programa. Algunos ejemplos comunes de excepciones incluyen:

**TypeError**: Se produce cuando se realiza una operación en un tipo incorrecto de objeto.
**ValueError**: Se produce cuando una función recibe un argumento con un valor incorrecto.
**ZeroDivisionError**: Se produce cuando se intenta dividir un número por cero.
**IndexError**: Se produce cuando se intenta acceder a un índice inválido en una secuencia (como una lista o una cadena).
**FileNotFoundError**: Se produce cuando se intenta abrir un archivo que no existe.

Uso de la cláusula **finally**:
La cláusula finally se utiliza junto con los bloques try y except para proporcionar un código que se ejecutará sin importar si se produjo una excepción o no. El código dentro del bloque finally se ejecutará siempre, ya sea que se haya capturado una excepción o no.
