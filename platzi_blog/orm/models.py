from sqlalchemy import Column, Integer, String, TIMESTAMP
from personal_admon_backend.orm.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True)
    password = Column(String)
    nickname = Column(String)
    email = Column(String, unique=True)


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_categoria = Column(String, unique=True)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    fecha_publicacion= Column(TIMESTAMP)
    contenido = Column(String)
    estatus = Column(String)
    usuario_id = Column(Integer)
    categoria_id = Column(Integer)
