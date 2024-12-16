from entrega3.E_grafo import *
from entrega3.Recorrido_en_profundidad import *
from entrega3.Recorrido_en_anchura import Recorrido_en_anchura

if __name__=="__main__":
    grafo1 = E_grafo(Graph_type.DIRECTED, lambda x:1)
    grafo1.add_vertex("a")
    grafo1.add_vertex("b")
    grafo1.add_vertex("c")
    grafo1.add_vertex("d")
    grafo1.add_vertex("e")
    grafo1.add_vertex("f")
    grafo1.add_vertex("g")
    grafo1.add_vertex("h")
    grafo1.add_vertex("i")
    grafo1.add_vertex("j")
    grafo1.add_vertex("k")
    grafo1.add_vertex("l")
    grafo1.add_vertex("m")
    grafo1.add_vertex("n")
    
    grafo1.add_edge("a", "b", 1)
    grafo1.add_edge("a", "c", 2)
    grafo1.add_edge("a", "d", 3)
    grafo1.add_edge("b", "e", 4)
    grafo1.add_edge("b", "f", 5)
    grafo1.add_edge("e", "j", 6)
    grafo1.add_edge("f", "k", 7)
    grafo1.add_edge("f", "l", 8)
    grafo1.add_edge("f", "h", 9)
    grafo1.add_edge("c", "g", 10)
    grafo1.add_edge("d", "g", 11)
    grafo1.add_edge("d", "h", 12)
    grafo1.add_edge("d", "i", 13)
    grafo1.add_edge("i", "m", 14)
    grafo1.add_edge("i", "n", 15)

    #grafo1.plot_graph()
    
    """
    recor = Recorrido_en_anchura.of(grafo1)
    recor.traverse("a")
    print(recor.path())
    for i in recor.tree():
        print (f'{i} : {recor.tree()[i]}')
    FUNCIONAMIENTO ANCHURA CORRECTO
    """
    
    """
    recor = Recorrido_en_profundidad.of(grafo1)
    recor.traverse("a")
    print(recor.path())
    for i in recor.tree():
        print (f'{i} : {recor.tree()[i]}')
    FUNCIONAMIENTO EN PRFUNDIDAD CORRECTO
    """