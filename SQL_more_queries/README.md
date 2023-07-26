# SQL more queries

### ¿Cómo crear un nuevo usuario en MySQL?
Para crear un nuevo usuario en MySQL, debes tener privilegios de administrador para realizar esta tarea. Utilizaremos el comando CREATE USER para crear al usuario y luego asignaremos los privilegios necesarios. 

```sql
CREATE USER 'nuevo_usuario'@'localhost' IDENTIFIED BY 'tu_contrasena';
```
En este ejemplo, hemos creado un nuevo usuario llamado "nuevo_usuario" con contraseña "tu_contrasena". El @'localhost' indica que este usuario solo puede conectarse desde el servidor MySQL en el mismo equipo.

¿Cómo gestionar privilegios para un usuario en una base de datos o tabla?
Para otorgar privilegios a un usuario en una base de datos o tabla, utilizamos el comando GRANT.

```sql
GRANT SELECT, INSERT, UPDATE ON nombre_de_base_de_datos.* TO 'nuevo_usuario'@'localhost';
```
En este ejemplo, hemos otorgado al usuario "nuevo_usuario" permisos SELECT, INSERT y UPDATE en todas las tablas de la base de datos nombre_de_base_de_datos. Con estos privilegios, el usuario podrá realizar consultas SELECT, insertar nuevos registros y actualizar datos en la base de datos.

### ¿Cómo usar las restricciones NOT NULL y UNIQUE?
Las restricciones NOT NULL y UNIQUE se utilizan para asegurar la integridad de los datos en una tabla.

NOT NULL: Se utiliza para asegurar que un campo no contenga valores nulos (vacíos). Por ejemplo:
```sql
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```
En este ejemplo, la columna nombre y email no pueden estar vacías (NULL), deben tener un valor en cada registro.

UNIQUE: Se utiliza para asegurar que un campo tenga valores únicos en la tabla. Por ejemplo:
```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    username VARCHAR(20) UNIQUE,
    email VARCHAR(100) UNIQUE
);
```
En este caso, tanto username como email deben ser únicos en cada registro de la tabla.

### JOIN:

La cláusula JOIN se utiliza para combinar filas de dos o más tablas basadas en una columna común entre ellas. Hay varios tipos de JOIN, pero el más común es el INNER JOIN, que solo muestra las filas que tienen coincidencias en ambas tablas.

Supongamos que tenemos dos tablas: empleados y departamentos. La tabla empleados contiene información sobre los empleados de una empresa, y la tabla departamentos contiene información sobre los departamentos en los que trabajan los empleados. Ambas tablas tienen una columna llamada departamento_id, que es la que utilizaremos para combinar las tablas.

Tabla "empleados":

```diff
+----+-----------+---------------+
| id | nombre    | departamento_id|
+----+-----------+---------------+
| 1  | Juan      | 1             |
| 2  | Maria     | 2             |
| 3  | Pedro     | 1             |
+----+-----------+---------------+
```

Tabla "departamentos":

```diff
+----+---------------+
| id | nombre        |
+----+---------------+
| 1  | Ventas        |
| 2  | Contabilidad  |
+----+---------------+
```
Para obtener una lista que muestre el nombre de cada empleado junto con el nombre de su departamento, utilizamos el siguiente INNER JOIN:

```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
JOIN departamentos ON empleados.departamento_id = departamentos.id;
```
Resultado:

```diff
+---------+---------------+
| nombre  | departamento  |
+---------+---------------+
| Juan    | Ventas        |
| Maria   | Contabilidad  |
| Pedro   | Ventas        |
+---------+---------------+
```
En este ejemplo, hemos utilizado JOIN para combinar las filas de las tablas empleados y departamentos en base a la columna departamento_id en empleados y la columna id en departamentos. El resultado muestra el nombre de cada empleado junto con el nombre de su departamento.

### UNION:

La cláusula UNION se utiliza para combinar el resultado de dos o más consultas en un solo conjunto de resultados. Las consultas deben tener la misma cantidad de columnas y tipos de datos correspondientes.

Supongamos que tenemos dos tablas: clientes1 y clientes2. Ambas tablas contienen información sobre clientes, y queremos combinar los resultados de ambas tablas en una sola lista.
Para obtener una lista combinada de todos los nombres de clientes de ambas tablas, utilizamos el siguiente UNION:

```sql
SELECT nombre FROM clientes1 UNION SELECT nombre FROM clientes2;
```
