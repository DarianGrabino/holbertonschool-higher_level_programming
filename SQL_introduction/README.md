# SQL

### ¿Qué es una base de datos?
Una base de datos es una colección organizada de información que se almacena de forma estructurada y puede ser accedida, gestionada y actualizada fácilmente.

### ¿Qué es una base de datos relacional?
Una base de datos relacional es un tipo de base de datos que organiza los datos en tablas con filas y columnas. Establece relaciones entre tablas utilizando claves primarias y claves foráneas.

### Crear base de datos
```sql
CREATE DATABASE nombre_de_la_base_de_datos;
```

### Mostrar base de datos
```sql
SHOW DATABASES;
```

### Eliminar base de datos
```sql
DROP DATABASE nombre_de_la_base_de_datos;
```

### Clave Primaria (Primary Key):

Una clave primaria es una columna o un conjunto de columnas que identifica de forma única cada fila en una tabla. Sus principales características son:

- Unicidad: Cada valor de la clave primaria debe ser único en la tabla. Esto significa que no puede haber dos filas con el mismo valor en la columna de la clave primaria.

- No nulidad: La clave primaria no puede contener valores nulos. Cada fila debe tener un valor válido para la clave primaria.

- Indexación: La clave primaria suele tener un índice asociado, lo que acelera las búsquedas y las operaciones que involucran la clave primaria.

### Clave Foránea (Foreign Key):

Una clave foránea es una columna o un conjunto de columnas que establece una relación entre dos tablas. La clave foránea en una tabla se refiere a la clave primaria de otra tabla. Sus características principales son:

- Relación entre tablas: La clave foránea crea una relación entre la tabla que contiene la clave foránea (tabla secundaria o hija) y la tabla cuya clave primaria se referencia (tabla principal o padre).

- Mantenimiento de la Integridad Referencial: La clave foránea garantiza que los datos relacionados entre tablas sean consistentes. Esto significa que un valor en la clave foránea debe existir en la tabla referenciada o ser nulo si la relación es opcional.

- Acciones en cascada: Algunas bases de datos permiten definir acciones en cascada cuando se modifican o eliminan registros en la tabla principal. Por ejemplo, puedes configurar que al eliminar una fila en la tabla principal, se eliminen automáticamente las filas relacionadas en la tabla secundaria.

### ¿Qué significa SQL?
SQL significa "Structured Query Language" (Lenguaje de Consulta Estructurado), y es un lenguaje de programación utilizado para gestionar bases de datos relacionales.

### ¿Qué es MySQL?
MySQL es un sistema de gestión de bases de datos relacional de código abierto, muy utilizado en aplicaciones web y de servidor para almacenar y recuperar datos.

### DDL (Data Definition Language):

DDL (Lenguaje de Definición de Datos) es un conjunto de comandos en SQL que se utilizan para definir y gestionar la estructura de una base de datos. Estos comandos permiten crear, modificar y eliminar objetos de la base de datos, como tablas, índices, vistas y otros elementos. Algunos ejemplos de comandos DDL son:

CREATE: Se usa para crear objetos en la base de datos, como tablas, vistas, índices, etc.

Ejemplo de creación de una tabla:

```sql
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    salario DECIMAL(10, 2)
);
```

ALTER: Permite modificar la estructura de la base de datos, como agregar o eliminar columnas de una tabla.

Ejemplo de agregar una columna a una tabla existente:

``` sql
ALTER TABLE empleados
ADD fecha_contrato DATE;
```

DROP: Se utiliza para eliminar objetos de la base de datos, como tablas o vistas.

Ejemplo de eliminación de una tabla:

``` sql
DROP TABLE empleados;
```

### DML (Data Manipulation Language):


DML (Lenguaje de Manipulación de Datos) es otro conjunto de comandos SQL que se utilizan para gestionar los datos dentro de las tablas. Estos comandos permiten insertar, actualizar y eliminar registros en la base de datos. Algunos ejemplos de comandos DML son:

INSERT: Se usa para agregar nuevos registros a una tabla.

Ejemplo de inserción de datos en la tabla "empleados":

``` sql
INSERT INTO empleados (id, nombre, salario)
VALUES (1, 'Juan Pérez', 3500.00);
```

UPDATE: Permite actualizar registros existentes en una tabla.

Ejemplo de actualización del salario para un empleado específico:

```sql
UPDATE empleados
SET salario = 4000.00
WHERE id = 1;
```

DELETE: Se utiliza para eliminar registros de una tabla.

Ejemplo de eliminación de un empleado específico de la tabla:

``` sql
DELETE FROM empleados
WHERE id = 1;
```

Es importante recordar que DDL se utiliza para definir la estructura de la base de datos y sus objetos, mientras que DML se utiliza para gestionar los datos dentro de las tablas. Ambos conjuntos de comandos son fundamentales en SQL para administrar y trabajar con bases de datos relacionales.


### Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update

$ sudo apt install mysql-server

$ mysql --version

$ sudo service mysql status

$ sudo service mysql start

$ sudo mysql

$ mysql -hlocalhost -uroot -p



*mysql*: abrirá la interfaz de línea de comandos de MySQL y estarás listo para ingresar consultas y comandos SQL.

*-hlocalhost*: Es el parámetro que especifica el host (servidor) al que te quieres conectar. En este caso, localhost indica que te estás conectando al servidor de MySQL que se está ejecutando en la misma máquina en la que estás trabajando. Si el servidor de MySQL está en otra máquina, debes proporcionar su dirección IP o nombre de host en lugar de localhost

*-uroot*: Es el parámetro que indica el nombre de usuario con el que te quieres conectar al servidor de MySQL. En este caso, estás utilizando el usuario "root", que es el superusuario con todos los privilegios en el servidor de MySQL.

*-p*: Es el parámetro que indica que se requiere una contraseña para la conexión. Al incluir -p, se le solicitará que ingreses la contraseña del usuario "root" de MySQL para poder acceder a la interfaz de línea de comandos de MySQL.
