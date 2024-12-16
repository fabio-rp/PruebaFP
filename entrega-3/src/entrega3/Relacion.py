'''
Created on 17 nov 2024

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class Relacion:
    interacciones:int
    dias_activa:int
    id : int
    
    @staticmethod
    def of(interacciones: int, dias_activa: int)->Relacion:
        try:
            Relacion.xx_num += 1 # De esta manera creamos identificadores únicos
        except: Relacion.xx_num:int=1
        return Relacion(interacciones, dias_activa, Relacion.xx_num)
        
    
    def __str__(self):
        return f"{self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones}"
        

if __name__ == '__main__':
    
    """rel1 = Relacion.of(55,65)
    rel2 = Relacion.of(133,700)
    rel3 = Relacion.of(2,5)
    rel4 = Relacion.of(10,50)
    
    
    print(rel1.id,rel2.id,rel3.id,rel4.id, sep="\n")
    print(rel1.xx_num,rel2.xx_num,rel3.xx_num,rel4.xx_num, sep="\n")
    print(rel1.id,rel2.id,rel3.id,rel4.id, sep="\n")
    print(Relacion.xx_num)"""
    