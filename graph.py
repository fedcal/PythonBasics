import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Semplice grafo non orientato
    G = nx.Graph()

    # Grafo direzionale
    # G = nx.DiGraph()

    # Grafo con molteplici collegamenti non direzionali tra i nodi
    # G = nx.MultiGraph()

    # Grafo con molteplici collegamenti direzionali tra i nodi
    # G = nx.MultiDiGraph()

    # Si crea un arco tra 1 e 2, se i nodi non esistono vengono creati
    G.add_edge(1,2)
    G.add_edge(2,3, weight=0.9)
    G.add_node(4)

    nx.draw_spring(G,with_labels = True)
    plt.show()

    # Creazione grafo da numpy
    G = nx.from_numpy_array(np.array([[0,1,0],
                                     [1,0,1],
                                     [1,1,1]]))
    nx.draw_spring(G, with_labels=True)
    plt.show()

    # Possiamo aggiungere nodi da una lista
    lista_nodi = [(8,9),(9,5),(9,6),(6,5)]
    G.add_edges_from(lista_nodi)
    nx.draw_spring(G, with_labels=True)
    plt.show()

    # Ottenere il grado di un nodo
    print(dict(G.degree)[9])
