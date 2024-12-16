from __future__ import annotations
from src.entrega2.tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar, Generic, Callable, List
from abc import ABC, abstractmethod

E = TypeVar('E')



class Pila(Agregado_lineal):
    def __init__(self, elements: E = []):
        super().__init__(elements)

    @classmethod
    def of(cls, elements: E = []) -> Pila:
        return cls(elements)
    

    
    def add(self, e: E) -> None: 
            self._elements.insert(0, e)
        
    def print_pila(self):
        txt='{0}({1})'
        if self.is_empty:
            print("'empty'")
            return None
        print(txt.format("Pila", self.elements[0]))
        
        
