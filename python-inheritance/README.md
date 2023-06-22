# Inheritance

Permite la creación de clases nuevas basadas en clases existentes. Puedes crear una clase que herede los atributos y métodos de otra clase, llamada clase padre o superclase.

Cuando una clase hereda de otra, la clase hija hereda todos los atributos y métodos de la clase padre y puede agregar sus propios atributos y métodos adicionales o modificar los existentes. La clase hija también puede proporcionar implementaciones específicas de los métodos heredados, lo que permite personalizar el comportamiento de la clase para adaptarlo a sus necesidades.

La herencia en Python es un mecanismo que permite crear nuevas clases basadas en clases existentes, facilitando la reutilización de código y la creación de jerarquías de clases en la programación orientada a objetos.

**dir()** recibe un objeto como argumento y devuelve una lista de todos los atributos y métodos asociados con ese objeto. La lista devuelta incluye tanto los atributos y métodos incorporados del objeto como los atributos y métodos definidos en la clase. Ejemplo task 0.

**super()** se utiliza para llamar a un método de la clase base o padre desde una subclase. Puedes llamar al método de la clase base y luego agregar la lógica adicional o las modificaciones necesarias en la subclase. 
Ejemplo task 10 (al método integer_validator() de la clase BaseGeometry, se pasa self como primer argumento para hacer referencia a la instancia actual de Square. Esto permite que el método integer_validator() tenga acceso a los atributos y métodos de la instancia)
