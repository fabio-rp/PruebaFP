from __future__ import annotations
from src.entrega2.tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar, Generic, Callable, List
from abc import ABC, abstractmethod

E = TypeVar('E')
R = TypeVar('R')


class Lista_ordenada(Agregado_lineal, Generic[E,R]):
    def __init__(self, elements: List[E] = [], order: Callable[[E], R]=lambda x:x):
        super().__init__(elements)
        
        self._order: Callable([E],R) = order
        self._elements = sorted(self.elements, key=order)
               

    def of(self, order: Callable[[E], R] ) -> Lista_ordenada[E, R]:
        self._order: Callable([E],R) = order
        self._elements = sorted(self.elements, key=order)
        return self
    
    
    def __index_order(self, e: E) -> int:
        for elem in self.elements:
            if self._order(e) <= self._order(elem):
                return self.elements.index(elem)
        return(len(self.elements))

    
    def add(self, e: E) -> None: 
        self._elements.insert(self.__index_order(e), e)
        
    def print_list(self):
        txt='{0}({1})'
        print(txt.format("ListaOrdenada", self.elements))
        
        
""" 
ord = Lista_ordenada([0,4,2,5])
print(ord.elements)
print(ord.of(lambda x:x).elements)
ord.add(4)
ord.add_all([4,5,8,2,4,9,60])
print(ord.elements)
ord.print_list()
"""
