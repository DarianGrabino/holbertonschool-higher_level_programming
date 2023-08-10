# Python - Object-relational mapping

Un Object-Relational Mapper (ORM) es una herramienta de programación que se utiliza para facilitar la interacción y comunicación entre una base de datos relacional y una aplicación orientada a objetos. En el contexto del desarrollo de software, las bases de datos relacionales almacenan datos en tablas con filas y columnas, mientras que las aplicaciones orientadas a objetos utilizan clases y objetos para representar datos y lógica de negocio.

El objetivo principal de un ORM es eliminar o reducir la brecha entre estos dos paradigmas diferentes, permitiendo que los desarrolladores trabajen con datos almacenados en la base de datos utilizando objetos de programación en lugar de consultas SQL directas. De esta manera, se facilita el manejo y la manipulación de datos, ya que el desarrollador puede utilizar el lenguaje de programación y la sintaxis familiar para realizar operaciones CRUD.

## MySQLdb
## Conectar a una datebase y realizar una consulta
```python
import MySQLdb
# Definir los parametros de conexion 
host = "localhost"
user = "tu_usuario"
password = "tu_contraseña"
database = "nombre_de_la_database"

# Crear la coneccion a la base de datos
db_conection = MySQLdb.conect(
    host = host,
    user = user,
    password = password
    db = database 
)

# Crear un cursor para realizar operaciones en la base de datos
cursor = db_conection.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM tabla")

# Obtener los resultados
results = cursor.fetchall()

# Imprimir los resultados
for row in results:
    print(row)

# Cerrar cursor y conexion
cursor.close()
db_conection.close()
```
- Un cursor es un objeto que permite interactuar y manipular los resultados de una consulta realizada a una base de datos. El cursor actúa como un puntero que recorre los registros devueltos por una consulta, uno por uno, permitiendo así acceder a los datos de manera secuencial.

- fetchall() es un método utilizado con un cursor para recuperar todos los registros (filas) resultantes de una consulta a una base de datos. Este método se llama en el objeto cursor después de haber ejecutado una consulta con el método execute().


## La inyección SQL
Es un tipo de ataque informático que se produce cuando un atacante inserta o "inyecta" código SQL malicioso en una consulta SQL legítima que se envía a una base de datos. Esto puede tener diversas consecuencias negativas, como robo de datos confidenciales, modificación no autorizada de datos, eliminación de datos, acceso no autorizado al sistema y más. Para prevenir los ataques de inyección SQL, es esencial utilizar prácticas de programación seguras, como la parametrización de consultas SQL, la validación y el filtrado adecuado de entradas de usuario y la implementación de medidas de seguridad en la capa de aplicación y en la base de dato

## SQLAlchemy
SQLAlchemy proporciona una función llamada declarative_base() que se utiliza para crear una clase base para todas las clases ORM que definirás. Esta clase base actúa como un intermediario entre tus clases y las tablas de la base de datos. Al definir Base = declarative_base(), estás creando una clase base personalizada que todas tus clases ORM heredarán. Esta clase base también lleva la información necesaria para realizar el mapeo entre las clases y las tablas de la base de datos.

```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
```

### create_engine 
Es una función proporcionada por SQLAlchemy que se utiliza para crear una instancia de conexión a una base de datos. Esta función se utiliza para establecer la conexión entre tu aplicación y la base de datos que deseas utilizar.

```python
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db))
connection = engine.connect()
```

### Session
Una sesión en SQLAlchemy es una abstracción que te permite trabajar con objetos Python en lugar de consultas SQL directas para interactuar con una base de datos. Proporciona una forma más sencilla y eficiente de interactuar con una base de datos utilizando el enfoque de ORM. La sesión se encarga de muchas tareas relacionadas con la administración de transacciones, la persistencia de objetos y la comunicación con la base de datos.

```python
from sqlalchemy.orm import sessionmaker

Session = sessioinmaker(bind=engine)
session = Session()
states = session.query(State).all()

for state in states:
    print(f"{state.id}: {state.name}")

session.close()
```

## relationship
Se utiliza para definir y gestionar las relaciones entre objetos en un sistema orientado a objetos y las tablas en una base de datos relacional. Esta función se utiliza dentro de una clase de modelo para definir cómo los objetos de esa clase están relacionados con objetos de otra clase. La relación puede ser de varios tipos, como "uno a uno", "uno a muchos" y "muchos a muchos". 

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')
```


## Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed.
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

## Install SQLAlchemy module version 1.4.x
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
