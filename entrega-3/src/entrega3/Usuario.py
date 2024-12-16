'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
import re


@dataclass(frozen=True)
class Usuario:
    def __init__(self, dni:str, nombre:str, apellidos:str, fecha_nacimiento:date)->None:
        self._dni:str
        self._nombre:str
        self._apellidos:str
        self._fecha_nacimiento:date
           
    @staticmethod
    def of(dni:str, nombre:str, apellidos:str, fecha_nacimiento:date) -> Usuario:
        #check dni
        try: int(dni[7]); raise ValueError("El DNI es debe finalizar con una letra")
        except: checkdni:bool = (len(dni) == 8 )
        if not checkdni: raise ValueError("El DNI debe tener 8 dígitos")
        #check fecha
        checkfecha:bool = (fecha_nacimiento < datetime.now())
        if not checkfecha: raise ValueError("La fecha debe ser anterior a la actual")
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    @staticmethod
    def parse(linea:str) -> Usuario:
        splitted = linea.split(",")
        dni:str = splitted[0]
        nombre:str = splitted[1]
        apellidos:str = splitted[2]
        fecha_nacimiento:date = datetime.strptime(splitted[3], "%Y-%m-%d")
        
        #check dni
        try: int(dni[7]); raise ValueError("El DNI es debe finalizar con una letra")
        except: checkdni:bool = (len(dni) == 8 )
        if not checkdni: raise ValueError("El DNI debe tener 8 dígitos")
        #check fecha
        checkfecha:bool = (fecha_nacimiento < datetime.now())
        if not checkfecha: raise ValueError("La fecha debe ser anterior a la actual")
        
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
         
    def __str__(self):
        return '{0} - {1}'.format(self._dni,self._nombre)
    
    @property
    def dni(self):
        return self._dni
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellidos(self):
        return self._apellidos
    @property
    def fecha(self):
        return self._fecha

if __name__ == '__main__':
    linea:str = "45718832U,Carlos,Lopez,1984-01-14"
    usuario: Usuario = Usuario.parse(linea)
    print(usuario)