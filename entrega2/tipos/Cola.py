from __future__ import annotations
from src.entrega2.tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar, Generic, Callable, List
from abc import ABC, abstractmethod

E = TypeVar('E')



class Cola(Agregado_lineal):
    def __init__(self, elements: List[E] = []):
        super().__init__(elements)

    def of(self) -> Cola:
        self._elements = []
        return self
    

    
    def add(self, e: E) -> None: 
            self._elements.append(e)
        
    def print_cola(self):
        txt='{0}({1})'
        print(txt.format("Cola", self.elements))
        
        

"""
cola = Cola([3,5,6,4,3,2])
cola.print_cola()
cola.of()
cola.add(3)
cola.add_all([3,5])
cola.print_cola()
"""