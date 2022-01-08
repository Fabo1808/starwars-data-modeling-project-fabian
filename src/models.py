import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id=Column(Integer, primary_key=True)
    user_name=Column(String(40), unique = True)
    first_name=Column(String(20), nullable=False)
    last_name=Column(String(20), nullable=False)
    email=Column(String (50), unique=True)
    sign_in_date=Column(DateTime(), nullable=True)
    favorites= relationship('favorites', backref='user', uselist=True)
    favorite_id=Column(Integer, ForeignKey('favorite.id'), nullable=False)

class Favorite(Base):
    __tablename__= 'favorite'
    id=Column(Integer, primary_key=True)
    character_id=Column(Integer, ForeignKey('character.id'), nullable=False)
    planet_id=Column(Integer, ForeignKey('planet.id'), nullable=False)
    vehicle_id=Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    favorites=relationship('favorites', backref='user', uselist=True)

class Character(Base):
    __tablename__= 'character'
    id=Column(Integer, primary_key=True)
    name=Column(String(50), nullable=False)
    race=Column(String(30), nullable=False)
    gender=Column(String(30), nullable=False)
    skills=Column(String(200), nullable=False)
    personality=Column(String(200), nullable=False)
    
class Planet(Base):
    __tablename__= 'planet'
    id=Column(Integer, primary_key=True)
    name=Column(String(40), nullable=False)
    type=Column(String(30), nullable=False)
    constellation=Column(String(50), nullable=False)
    composition=Column(String(70), nullable=False)
    dominant_race=Column(String(40), nullable=False)
    government_system=Column(String(40), nullable=False)


class Vehicle(Base):
    __tablename__='vehicle'
    id=Column(Integer, primary_key=True)
    name=Column(String(50), nullable=False)
    type=Column(String(200), nullable=False)
    constructor=Column(String(30), nullable=False)
    functionality=Column(String(100), nullable=False)
    length=Column(String(30), nullable=False)
    



    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')