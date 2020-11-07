import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from random import randrange

# Código para gerar uma entrada semelhante a do problema Dengue do SPOJ
def gerarEntrada():
    confirmacao = False
    vilas = randrange(1, 2)
    entrada = []
    graf = []
    for n in range(vilas):
        if(vilas != 0):
            nvertices = randrange(1, 3)
            if(nvertices != 0):
                G = nx.random_tree(nvertices)
                plt.figure(n)
                nx.draw_networkx(G)
                plt.show()
                el = nx.to_numpy_array(G)
                vertices = int(sqrt(el.size))
                contL = 0
                contC = 0
                arestas = []
                for x in el:
                    contC = 0
                    for y in x:
                        if(y == 1.0):
                            arestas.append([contL, contC])
                        contC += 1
                    contL += 1
                for el in arestas:
                    for el2 in arestas:
                        if(el[0] == el2[1] and el[1] == el2[0]):
                            arestas.remove(el2)
                graf.append(arestas)
                print(vertices)
                entrada.append(f"{vertices}")
                for el in arestas:
                    print(f"{el[0]} {el[1]}")
                    entrada.append(f"{el[0]} {el[1]}")
                confirmacao = True
    if(confirmacao == True):
        print(0)
    else:
        print(0)
    return entrada
 
# TRANSFORMANDO ENTRADA (LISTA DE STRING) EM LISTA DE GRAFOS
def transformarEntradaGrafo(entrada):
    grafos = []
    for idx, el in enumerate(entrada):
        vert = el.split(" ")
        if(len(vert)==1):
            if(int(vert[0])==0):
                break
            elif(int(vert[0])==1):
                G = nx.Graph()
                grafos.append(G)
            else:
                G = nx.Graph()
        else:
            G.add_edge(int(vert[0]), int(vert[1]))
            if(len(entrada[(idx + 1) % len(entrada)].split(" "))==1):
                grafos.append(G)
    return grafos

# TRANSFORMANDO ENTRADA PARA UMA LISTA COM OS VÉRTICES E SUA ORDEM DE SURGIMENTO
def transformarEntradaOrdem(entrada):
    ordens = []
    for idx, el in enumerate(entrada):
        vert = el.split(" ")
        if(len(vert)==1):
            if(int(vert[0])==0):
                break
            elif(int(vert[0])==1):
                ordem = []
                ordem.append([0])
                ordens.append(ordem)
            else:
                ordem = []
        else:
            if int(vert[0]) not in ordem:
                ordem.append(int(vert[0]))
            if int(vert[1]) not in ordem:
                ordem.append(int(vert[1]))
            if(len(entrada[(idx + 1) % len(entrada)].split(" "))==1):
                ordens.append(ordem)
    return ordens
 
# PRODUZINDO A SAÍDA
def gerarSaida(grafos, ordens):
    teste = 0
    for x in grafos:
        teste += 1
        if (len(x)==0):
            print(f"Teste {teste}\n0\n")
        else:
            try:
                dist = nx.floyd_warshall_numpy(x)
                excentricidade = []
                print(dist)
                for edge in dist:
                    excentricidade.append(np.amax(edge))
                centros = np.argwhere(excentricidade == np.amin(excentricidade))
                centros = centros.flatten().tolist()
                print(excentricidade)
                if(len(centros) == 1):
                    print(centros)
#                    print(ordens)
#                    print(teste)
                    print(ordens[(teste-1)])
                    cont = 0
                    for el in ordens[(teste-1)]:
#                        print(el)
                        if (int(centros[0]) == cont):
                            centros[0] = el
                            break
                        cont += 1
                    print(f"Teste {teste}\n{centros[0]}\n")
                else:
                    print(centros)
#                    print(ordens)
#                    print(teste)
                    print(ordens[(teste-1)])
                    ocr = False
                    cont = 0
                    for el in ordens[(teste-1)]:
                        if (int(centros[0]) == cont and ocr == False):
                            ocr = True
                            centros[0] = el
                        if ((centros[1]) == cont and ocr == True):
                            ocr = False
                            centros[1] = el
                            break
                        cont += 1
                    print(f"Teste {teste}\n{centros[0]} {centros[1]}\n")
            except:
                continue
            
if __name__ == "__main__":
    entrada = gerarEntrada()
    grafos = transformarEntradaGrafo(entrada)
    ordens = transformarEntradaOrdem(entrada)
    gerarSaida(grafos, ordens)