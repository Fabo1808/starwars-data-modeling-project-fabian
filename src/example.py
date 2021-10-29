import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from eralchemy import render_er

Base = declarative_base()

class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    time_estimate = Column(Integer, nullable=False)
    name = Column(String(80), unique=True)
    materials_cost = Column(Float, default=0)
    margin = Column(Float, nullable=False)
    manpower_estimate = Column(Integer, nullable=False)
    certificates = relationship('Certificate', backref='service', uselist=True)

class Worker(Base):
    __tablename__ = 'worker'
    id = Column(Integer, primary_key=True)
    document_number = Column(String(12), unique=True)
    name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    telephone_number = Column(String(15))
    dob = Column(DateTime())
    email = Column(String(120), unique=True)
    address = Column(String(240))
    per_hour = Column(Float, nullable=False)
    certificates = relationship('Certificate', backref='worker', uselist=True)
    
class Certificate(Base):
    __tablename__ = 'certificate'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(), nullable=False)
    number = Column(String(80), nullable=False)
    service_id = Column(Integer, ForeignKey('service.id'), nullable=False)
    worker_id = Column(Integer, ForeignKey('worker.id'), nullable=False)

class Vehicle:
    axes = Column(Integer)
    year = Column(Integer)
    combustion_type = Column(String(80))
    color = Column(String(25))
    brand = Column(String(80))
    model = Column(String(50))

class Car(Vehicle):
    doors = Column(Integer)
    glasses = Column(String(10))

class Sedan(Car, Base):
    __tablename__ = 'sedan'
    id = Column(Integer, primary_key=True)

class Compact(Car, Base):
    __tablename__ = 'compact'
    id = Column(Integer, primary_key=True)

class Truck(Car, Base):
    __tablename__ = 'truck'
    id = Column(Integer, primary_key=True)


## Draw from SQLAlchemy base
render_er(Base, 'exampleDiagram.png')