"""
def dijkstra(graph, start , objetos_moviles):
    #graph[start_node] = objetos_moviles[start_node]
    #graph['A1'] = objetos_moviles['A1']
    # Inicializar distancias a infinito para todos los nodos excepto el nodo de inicio
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Crear un conjunto de nodos no visitados
    unvisited_nodes = set(graph)

    while unvisited_nodes:
        # Obtener el nodo con la distancia mínima
        min_node = min(unvisited_nodes, key=lambda node: distances[node])

        # Eliminar el nodo mínimo del conjunto de nodos no visitados
        unvisited_nodes.remove(min_node)

        # Calcular las distancias mínimas para los nodos vecinos del nodo mínimo
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                print(neighbor,'nodo final',distance)

    return distances

# Ejemplo de grafo dirigido de prueba
graph = {
    'e1': {'e2': 5, 'e3': 2},
    'e2': {'e3': 1, 'e4': 3},
    'e3': {'e4': 2},
    'e4': {'e5': 4},
    'e5': {}
}

objetos_moviles = {
    'P1' : {'e1':3,'e4':1},
    'A1' : {'e4':3,'e5':2}
}

######
hash_distancias_calculadas = {('e1','e5') : [('e1','e2','e5'),5]}


start_node = 'e1'
distances = dijkstra(graph, start_node , objetos_moviles)
print(distances)
print("Distancias más cortas desde el nodo de inicio (", start_node, "):")
for node, distance in distances.items():
    print("Nodo:", node, ", Distancia:", distance)


"""

"""
import heapq

def dijkstra(graph, start):
    # Inicializar las distancias y los caminos de todos los nodos como infinito excepto el nodo inicial
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    paths = {node: [] for node in graph}
    paths[start] = [start]

    # Usar una cola de prioridad (heap) para mantener un seguimiento de los nodos no visitados
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Si ya hemos procesado el nodo actual, saltamos a la siguiente iteración
        if current_distance > distances[current_node]:
            continue

        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Si encontramos un camino más corto hacia el vecino, actualizamos la distancia y el camino
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(queue, (distance, neighbor))

    return distances, paths

# Ejemplo de uso
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 3},
    'C': {'B': 1, 'D': 1},
    'D': {}
}

start_node = 'A'
shortest_distances, shortest_paths = dijkstra(graph, start_node)

print("Camino más corto desde el nodo inicial:")
for node, distance in shortest_distances.items():
    print(f'{node}: {distance}')
    print(f'Recorrido: {" -> ".join(shortest_paths[node])}')
    print()
"""

import heapq

def dijkstra_preprocesos(graph, start, recorridos_guardados):

    recorrido_final = {}
    recorrido_final_v2 = {}

    # Inicializar las distancias, los caminos y los subcaminos de todos los nodos como infinito excepto el nodo inicial
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    paths = {node: [] for node in graph}
    subpaths = {node: [] for node in graph}
    paths[start] = [start]
    subpaths[start] = [start]

    # Usar una cola de prioridad (heap) para mantener un seguimiento de los nodos no visitados
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Si ya hemos procesado el nodo actual, saltamos a la siguiente iteración
        if current_distance > distances[current_node]:
            continue

        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            # Verificar si la arista va en la dirección correcta (grafo dirigido)
            if weight < 0:
                continue

            distance = current_distance + weight

            # Si encontramos un camino más corto hacia el vecino, actualizamos la distancia, el camino y el subcamino
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]

                diferencial = len(paths[neighbor]) - 1

                #Significa que hay 3 elementos
                lista_paths = paths[neighbor]
                count = 1
                while diferencial != count:
                    node_d = lista_paths[count] 
                    distancia_d = (distances[neighbor] - recorrido_final[node_d][1])
                    print(node_d,'---->',lista_paths[count:],recorrido_final[node_d][1])
                    if node_d in recorrido_final_v2:
                        recorrido_final_v2[node_d].update({lista_paths[-1]:[lista_paths[count:],distancia_d]})
                    else:
                        recorrido_final_v2[node_d] = {lista_paths[-1]:[lista_paths[count:],distancia_d]}
                    count = count + 1
                recorrido_final[neighbor] = [paths[neighbor],distances[neighbor]]
                recorrido_final_v2[start] = recorrido_final
                heapq.heappush(queue, (distance, neighbor))



    
    return recorrido_final_v2

'''
# Ejemplo de grafo dirigido de prueba
graph = {
    'e1': {'e2': 5, 'e3': 2},
    'e2': {'e3': 1, 'e4': 3},
    'e3': {'e4': 3},
    'e4': {'e5': 6},
    'e5': {}
}

start_node = 'e1'
recorridos_guardados = {}
shortest_distances = dijkstra(graph, start_node,recorridos_guardados)

print(shortest_distances)
print('e5' in shortest_distances)
print(shortest_distances['e1']['e5'])

"""
print(f"Camino más corto desde {start_node} a todos los nodos finales:")
for end_node in shortest_paths:
    print(f'Nodo final: {end_node}')
    print(f'Recorrido: {" -> ".join(shortest_paths[end_node])}')
"""
'''





#IMPRIMIR MAPA

##Imprimir Mapa Imagen
#Requiere (pip install networkx) y (pip install matplotlib)
"""
def imprimir_mapa():
    import networkx as nx
    import matplotlib.pyplot as plt
    


    with open(f'./mapa.txt', 'r') as file:
            #Dividimos las lineas del archivo
            primer_linea = file.readline()
            segunda_linea = file.readline()
            #Mostramos el Original en Pantalla
            print("####ORIGINAL####")
            print(primer_linea)
            print(segunda_linea)
            #Parseamos las Esquinas
            primer_linea = primer_linea[3:-2] #quitamos los caracteres del principio y final
            primer_linea = primer_linea.replace('"','') #quitamos las comillas demas
            segunda_linea = segunda_linea.replace(' ','')
            esquinas = primer_linea.split(',')
            #Parseamos las Calles
            segunda_linea = segunda_linea.split('{')[1].split('}')[0] #quitamos los caracteres del principio y final
            segunda_linea = segunda_linea.replace(' ','')
            segunda_linea = segunda_linea.replace('<','"')
            segunda_linea = segunda_linea.replace('>','"')
            segunda_linea = "[" + segunda_linea + "]"
            segunda_linea = eval(segunda_linea)
            calles = []
            for elemento in segunda_linea:
                valores = elemento.split(',')
                tupla = tuple(valores)
                calles.append(tupla)

            #Mostramos el Parseo hecho
            print("####Convertido####")
            print(esquinas)
            print(calles)


    G = nx.DiGraph()
    for e in esquinas:
        G.add_node(e)

    for c in calles:
        e1,e2,c = c
        G.add_edge(e1,e2,weight=c)

    pos = nx.spring_layout(G, k=0.5, iterations=100)  # Ajusta los valores de 'k' e 'iterations' para separar los nodos más

    nx.draw(G, pos, with_labels=True, arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5)
    plt.show()

imprimir_mapa()



"""
