from __future__ import annotations
from typing import TypeVar, Generic, Callable, List
from abc import ABC, abstractmethod

E = TypeVar('E')
P = TypeVar('P')



class Cola_de_prioridad(Generic[E,P]):
    def __init__(self, elements: List[tuple(E,P)] = []):
        self._priorities: List[tuple(E,P)] = sorted( elements, key=lambda x:-x[1] )
        self._elements:List[E] = [t[0] for t in self._priorities]
                                     
    
    def elements(self):
        return self._elements
    
    
    def priorities(self):
        return self._priorities
    
    
    def size(self) -> int:
        return len(self._priorities)
    
    
    def is_empty(self) -> bool:
        return (self._priorities==[])
    
    
    
    def __index_order(self, priority: P) -> int:
        if self._priorities != []:
            for i in range(len(self._priorities)):
                plist = self._priorities[i][1]
                if priority<=plist:
                    return i
        else: return 0
        
    def add(self, e: E, priority: P) -> None: 
        self._priorities.insert(self.__index_order(priority), (e, priority) )
        self._elements.insert(self.__index_order(priority), e )
        
    def add_all(self, ls: list[tuple[E,P]]) -> None:
        for tpl in ls:
            self.add(e=tpl[0], priority=tpl[1])
            
        
    def remove(self) -> E:
        self._priorities.pop(0)
        return self._elements.pop(0)
    
    def remove_all(self) -> list[E]: 
        deleted:List[E] = []
        while self.is_empty == False:
            deleted.append( self._elements.pop(0) )
            self._priorities.pop(0)
        return deleted
    

    def decrease_priority(self, e:E, new_priority:P) -> None: 
        for i in range (len(self._priorities)):
            if self._priorities[i][0]==e and new_priority>0 :
                newtpl = (e,new_priority)
                self._priorities[i] = newtpl
                
                self.__init__(self._priorities)
                

    def print_cola_prioridad(self):
        txt='{0}({1})'
        print(txt.format("ColaPrioridad", self.priorities))
        


