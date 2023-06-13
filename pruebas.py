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








##Pruebas del Juani

"""
E = ["e1","e2","e3","e4","e5","e6","e7","e8","e9","e10","e11","e12"]
C = [("e1","e2",10),("e2","e1",10),("e1","e3",8),("e3","e1",8),("e2","e4",8),("e4","e2",8),("e3","e5",15),("e5","e3",15),("e4","e6",15),("e6","e4",15),("e5","e6",5),("e5","e7",10),("e7","e5",10),("e7","e8",10),("e8","e7",10),("e8","e9",10),("e9","e8",10),("e8","e10",10),("e10","e8",10),("e9","e11",10),("e11","e9",10),("e10","e5",10),("e11","e10",10),("e10","e11",10),("e12","e10",10),("e10","e12",10)]
maph = crear_mapa(E,C)
print(maph)
"""



######### Funciones que use para cargar elementos en el mapa :), pd: las comenté por las dudas. ######### 
"""
#2. Crear los hash de elementos fijos y moviles. 
hash_fixed_element = {}
hash_movil_element = {}

#2.1. Cargar elementos fijos 
def load_fix_element(map, name, direction, hash_fixed):
    #Validar entradas.
    if name == "" or direction == []:
        return "Datos no validos"
    #Validar elemento fijo.
    assert validar_lugares(name) == True, f" Incorrecto, no es posible cargar esté lugar"
    #Validar que la dirección exista dentro del mapa.
    direction = list(direction)
    assert direction[0][0] in map, f"La esquina {direction[0][0]} no sé encuentra en el mapa"
    assert direction[1][0] in map, f"La esquina {direction[1][0]} no sé encuentra en el mapa" 
    #Agregar al hash en caso de que no exista.
    assert name not in hash_fixed, f"Elemento repetido, el lugar {name} ya se encuentra cargado en el mapa"
    hash_fixed[name] = direction
    updateMap(map, name, direction)
    return hash_fixed
      
load_fix_element(map, "H1", {("e3",7),("e5",8)}, hash_fixed_element)
load_fix_element(map, "A1", {("e1",6),("e2",4)}, hash_fixed_element)
load_fix_element(map, "T1", {("e10",5),("e11",5)}, hash_fixed_element)  
load_fix_element(map, "S1", {("e5",1),("e6",4)}, hash_fixed_element)

#2.2. Cargar elementos moviles.
def load_movil_element(map ,name, direction, amount, hash_movil):
    #Validar entradas.
    if name == "" or direction == []:
        return "Datos no validos"
    #Validar elemento movil.
    if name[0] != "P" or name[0] != "C":
        assert f"Elemento móvil incorrecto, no es posible cargar {name}"
    #Validar que la dirección exista dentro del mapa.
    direction = list(direction)
    assert direction[0][0] in map, f"La esquina {direction[0][0]} no sé encuentra en el mapa"
    assert direction[1][0] in map, f"La esquina {direction[1][0]} no sé encuentra en el mapa" 
    #Agregar al hash en caso de que no exista.
    assert name not in hash_movil or name[0] == "C", f"Elemento repetido, la persona {name} ya se encuentra cargado en el mapa"
    assert name not in hash_movil or name[0] == "P", f"Elemento repetido, el auto {name} ya se encuentra cargado en el mapa"
    hash_movil[name] = [direction,amount]
    #Agregar los autos al mapa(las personas serán ingresadas luego cuando se validen los viajes).
    if name[0] == "C":
        updateMap(map, name, direction)
    return hash_movil

load_movil_element(map ,"P1", {("e1",4),("e2",6)}, 1200, hash_movil_element)
load_movil_element(map, "P2", {("e3",4),("e1",4)}, 500, hash_movil_element)
load_movil_element(map, "C1", {("e5",3),("e7",7)}, 2500, hash_movil_element)
load_movil_element(map, "C2", {("e12",1),("e10",9)}, 2500, hash_movil_element)
load_movil_element(map, "C3", {("e8",5),("e9",5)}, 2500, hash_movil_element)
load_movil_element(map, "C4", {("e2",3.5),("e4",4.5)}, 2500, hash_movil_element)
"""

"""
hash_fixed_element = {}
crear_lugar(hash_fixed_element, "H1", {("e3",7),("e5",8)}, maph)
crear_lugar(hash_fixed_element, "A1", {("e1",6),("e2",4)}, maph)
crear_lugar(hash_fixed_element, "T1", {("e10",5),("e11",5)}, maph)  
diccFix = crear_lugar(hash_fixed_element, "S1", {("e5",1),("e6",4)}, maph)
print(maph)

"""