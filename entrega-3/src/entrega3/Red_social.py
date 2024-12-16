'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from entrega3.E_grafo import E_grafo, Graph_type, Traverse_type
from entrega3.Usuario import Usuario
from entrega3.Relacion import Relacion
from datetime import time, datetime
from us.lsi.tools.File import lineas_de_fichero, absolute_path


class Red_social(E_grafo[Usuario, Relacion]):
    
    def __init__(self,graph_type:Graph_type, traverse_type:Traverse_type, users:dict[str,Usuario] = {})->None:
        super().__init__(graph_type, lambda r: r.interacciones, traverse_type)
        self.__usuarios_dni:dict[str,Usuario] = users
        
    
    @staticmethod
    def of(self,graph_type:Graph_type = Graph_type.UNDIRECTED, traverse_type:Traverse_type = Traverse_type.BACK) -> Red_social: # TODO: Hay que añadir los parámetros de entrada
        return Red_social(graph_type, traverse_type)
    
    @staticmethod
    def parse(f1:str, f2:str, graph_type:Graph_type = Graph_type.UNDIRECTED, traverse_type: Traverse_type = Traverse_type.BACK) -> Red_social:
        
        
        #LEER USUSARIOS
        users:dict[str,Usuario] = {}
        with open(absolute_path(f1), "r", encoding="UTF-8") as f:
            for line in f.read().split("\n"):
                i=0
                for var in line.split(","):
                    if i==0: dni:str = var
                    if i==1: nombre:str = var
                    if i==2: apellidos:str = var
                    if i==3: fecha_nacimiento:date = datetime.strptime(var, "%Y-%m-%d")
                    i+=1
                users[dni] = Usuario(dni, nombre, apellidos, fecha_nacimiento)
        
        #INCLUIR USUARIOS EN EL GRAFO    
        redsocial_aux:Red_social[Usuario,Relacion] = Red_social(graph_type, traverse_type, users)
        for dni in users.keys():
            redsocial_aux.add_vertex(dni)
            
        #LEER RELACIONES
        
        with open(absolute_path(f2), "r", encoding="UTF-8") as f:
            for line in f.read().split("\n"):
                i=0
                for var in line.split(","):
                    if i==0: dni1:str = var
                    if i==1: dni2:str = var
                    if i==2: interacciones:int = var
                    if i==3: dias_activa:int = var
                    i+=1
                relacion_aux = Relacion.of(interacciones, dias_activa)
                
                if (dni1!=""):redsocial_aux.add_edge(dni1, dni2, relacion_aux)
        #DEVOLVER GRAFO RED SOCIAL (CON EL ATRIBUTO USUARIOS, DNI COMO VERTICES Y RELACIONES COMO ARISTAS)
        return redsocial_aux
                    
        
    @property
    def usuarios_dni(self)->dict[str,Usuario]:
        return self.__usuarios_dni
    
    def __str__(self):
        cadena:str=""
        for relac in self.edge_set():
            cadena += f"{relac._id} - días activa: {relac._dias_activa} - num interacciones {relac._interacciones}\n"
        return cadena


if __name__ == '__main__':
    rrss: Red_social = Red_social.parse('resources/usuarios.txt', 'resources/relaciones.txt')
    print(rrss.plot_graph())