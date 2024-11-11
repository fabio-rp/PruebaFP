from src.entrega2.tipos.Lista_ordenada import *

lista_ord = Lista_ordenada()
lista_ord.of(lambda x:x)
lista_ord.add(3)
lista_ord.add_all([1,2])
lista_ord.print_list()
print("\n----------------------------\n")
print(lista_ord.remove())
print("\n----------------------------\n")
print(lista_ord.remove_all())
print("\n----------------------------\n")
lista_ord.add_all([3,65,3,-1,6,76,5,3])
lista_ord.print_list()
print("\n----------------------------\n")
lista_ord.of(lambda x:-x) #del revés
lista_ord.print_list()
print("\n----------------------------\n")