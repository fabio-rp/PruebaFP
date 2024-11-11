from __future__ import annotations
from typing import TypeVar, Generic, List
from abc import ABC, abstractmethod

E = TypeVar('E')

class Agregado_lineal(ABC, Generic[E]):
    
    #PROPIEDADES
    def __init__(self,elements: List[E]):
        self._elements = elements
    
    @property
    def size(self)->int:
        return (len(self._elements) )
    
    @property
    def is_empty(self)->bool:
        return ( len(self._elements) == 0 )
    
    @property
    def elements(self)->list[E]:
        return self._elements
    
    #OTROS MÉTODOS
    @abstractmethod
    def add(self, e: E)->None:
        pass
    
    
    def add_all(self, ls: list[E])->None:
        for var in ls:
            self.add(var)

    def remove(self)->E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self)->list[E]:
        eliminados:list[E] = []
        if not self.is_empty:
            for size in range(len(self._elements)):
                eliminados.append(self.remove())
        return eliminados