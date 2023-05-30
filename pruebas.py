def dijkstra(graph, start , objetos_moviles):
    graph[start_node] = objetos_moviles[start_node]
    graph['A1'] = objetos_moviles['A1']
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

    return distances

# Ejemplo de grafo dirigido de prueba
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'C': 1, 'D': 3},
    'C': {'D': 2},
    'D': {'E': 4},
    'E': {}
}

objetos_moviles = {
    'P1' : {'A':3,'D':1},
    'A1' : {'D':3,'E':2}
}

start_node = 'P1'
distances = dijkstra(graph, start_node , objetos_moviles)

print("Distancias más cortas desde el nodo de inicio (", start_node, "):")
for node, distance in distances.items():
    print("Nodo:", node, ", Distancia:", distance)