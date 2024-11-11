from src.entrega2.tipos.Pila import *

pila = Pila()

pila.add("Hola")
pila.print_pila()
print("\n----------------------------\n")
pila.of()
pila.print_pila()
print("\n----------------------------\n")
pila.add_all(["a","b","c","d"])
pila.print_pila()
print("\n----------------------------\n")
pila.remove()
pila.print_pila()
print("\n----------------------------\n")
pila.remove_all()
pila.print_pila()
print("\n----------------------------\n")