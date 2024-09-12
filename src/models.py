import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    password = Column(String(250), nullable = False)
    date = Column(Date, index = True)

    def to_dict(self):
        return {}
    
class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    planeta_origen = Column(Integer, ForeignKey('planeta.id'))
    altura = Column(Float, nullable = False)
    unidades_altura = Column(String(250), nullable = False)
    peso = Column(Float, nullable = False)
    unidades_peso = Column(String(250), nullable = False)

    def to_dict(self):
        return {}
    
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    clima = Column(String(250), nullable = False)
    diametro = Column(Float, nullable = False)
    poblacion = Column(Integer, nullable = False)

    def to_dict(self):
        return {}

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    marca = Column(String(250), nullable = False)
    capacidad = Column(Integer, nullable = False)
    pasajeros = Column(Integer, nullable = False)
    tripulacion = Column(Integer, nullable = False)
    modelo = Column(String(250), nullable = False)

    def to_dict(self):
        return {}
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key = True)
    user = Column(Integer, ForeignKey('user.id'))
    personaje = Column(Integer, ForeignKey('personaje.id'))
    planeta = Column(Integer, ForeignKey('planeta.id'))
    vehiculo = Column(Integer, ForeignKey('vehiculo.id'))

    def to_dict(self):
        return {}


# class Favorite_personaje(Base):
#     __tablename__ = 'favorite_personaje'
#     id = Column(Integer, primary_key = True)
#     user = Column(Integer, ForeignKey('user.id'))
#     personaje = Column(Integer, ForeignKey('personaje.id'))

#     def to_dict(self):
#         return {}
    
# class Favorite_planeta(Base):
#     __tablename__ = 'favorite_planeta'
#     id = Column(Integer, primary_key = True)
#     user = Column(Integer, ForeignKey('user.id'))
#     planeta = Column(Integer, ForeignKey('planeta.id'))

#     def to_dict(self):
#         return {}
    
# class Favorite_vehiculo(Base):
#     __tablename__ = 'favorite_vehiculo'
#     id = Column(Integer, primary_key = True)
#     user = Column(Integer, ForeignKey('user.id'))
#     vehiculo = Column(Integer, ForeignKey('vehiculo.id'))

#     def to_dict(self):
#         return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
