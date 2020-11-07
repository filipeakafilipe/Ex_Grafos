import networkx as nx
import matplotlib.pyplot as plt

def GerarEntrada():
    entrada = []
    
    G = nx.Graph()
    G.add_weighted_edges_from([(0, 1, 1),
                               (0, 2, 3),
                               (0, 3, 9),
                               (1, 3, 2),
                               (2, 3, 2)])
    entrada.append(G)
    
    G = nx.Graph()
    G.add_weighted_edges_from([(0, 1, 1),
                               (0, 3, 4),
                               (0, 4, 2),
                               (1, 2, 5),
                               (1, 5, 3),
                               (2, 5, 5),
                               (3, 4, 2),
                               (3, 5, 5),
                               (4, 5, 8)])
    entrada.append(G)

    G = nx.Graph()
    G.add_weighted_edges_from([(0, 1, 8),
                               (0, 2, 2),
                               (1, 3, 2,),
                               (1, 5, 13),
                               (2, 3, 2),
                               (2, 4, 5),
                               (3, 4, 1),
                               (3, 5, 6),
                               (3, 6, 3),
                               (4, 5, 1),
                               (5, 6, 2),
                               (5, 7, 3),
                               (6, 7, 6)])
    entrada.append(G)



    return entrada

def GerarSaida(entrada):
    for G in entrada:
        penhasco = min(G.nodes)
        acampamento = max(G.nodes)
        DesenharGrafo(G)
        print(f"{nx.dijkstra_path_length(G, penhasco, acampamento)}")
        MostrarCaminho(G)

def MostrarCaminho(G):
    penhasco = min(G.nodes)
    acampamento = max(G.nodes)
    print(f"{nx.dijkstra_path(G, penhasco, acampamento)}")

def DesenharGrafo(G):
    plt.figure(1)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()

if __name__ == "__main__":
    entrada = GerarEntrada()
    GerarSaida(entrada)
