"""
1. Cargar nuevos lugares, personas y autos dentro del mapa
2. Conocer, dado un lugar, persona o auto la dirección del mismo.
3. Conocer, dado una persona que se encuentra en el mapa cuáles son los 10 autos
más cercanos que esa persona puede pagar.
4. Conocer, dado dos direcciones en el mapa cual es el camino más cercano para llegar
de uno a otro
"""

def crear_mapa(vertices,aristas):
    """Retorna un hash con el grafo mapa"""
    mapa = {}
    for v in vertices:
        mapa[v] = []
    
    for arista in aristas:
        #Extraemos desde la arista v1 = vertice_1 , v2 = vertice_2 , c = costo
        v1 , v2 , c = arista 
        mapa[v1].append((v2,c))
    
    return mapa

def validar_lugares(lugar):
    """Verifica si es un Hospital,Almacen,Tienda,Supermercado,Escuela,Kiosco o Iglesia"""
    lugares_validos = ('H','A','T','S','E','K','I')
    if lugar[0] in lugares_validos:
        return True
    else:
        return False

def crear_lugar(hash_lugares,nombre,direccion,mapa):
    """retorna el hash con los lugares actualizados"""

    direccion_final = list(direccion)

    for d in direccion:
        if d[0] not in mapa:
            direccion_final.remove(d)
    assert direccion_final,f'El Lugar Fijo: {nombre}, no se cargo, no existe {direccion} en el mapa'
    assert nombre not in hash_lugares,f'El objeto ya existe dentro del mapa'
    hash_lugares[nombre] = direccion_final
    return hash_lugares


def crear_persona(hash_personas,nombre,direccion,monto,mapa):
    """retorna el hash con las personas actualizadas"""
    direccion_final = list(direccion)

    for d in direccion:
        if d[0] not in mapa:
            direccion_final.remove(d)

    assert direccion_final,f'La persona {nombre}, no se cargo, no existe {direccion} en el mapa'
    assert nombre not in hash_personas,f'La persona ya existe dentro del mapa'
    hash_personas[nombre] = [direccion_final,monto]
    return hash_personas

def crear_auto(hash_autos,nombre,direccion,monto,mapa):
    """retorna el hash con los autos actualizados"""
    direccion_final = list(direccion)

    for d in direccion:
        if d[0] not in mapa:
            direccion_final.remove(d)
    
    assert direccion_final,f'El auto {nombre}, no se cargo, no existe {direccion} en el mapa'
    assert nombre not in hash_autos,f'El Auto ya existe dentro del mapa'
    hash_autos[nombre] = [direccion_final,monto]
    return hash_autos

# 2-
def conocer_ubicacion(objeto_movil,hash_movil):
    """retorna la ubicacion del mismo sea auto,lugar o persona"""
    if objeto_movil in hash_movil:
        return hash_movil[objeto_movil]
    else:
        return f'No existe el objeto {objeto_movil}'
    
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCIONES PARA DIJKSTRA(INICIO) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
class nodeVertex:
    value = None
    parent = None
    distance = 0
    
def DefinedVertexDijkstra(v,ListNode):
    #Definir cada vértice del grafo como un nodo con sus atributos.
    vertexNode = nodeVertex()
    vertexNode.value = v
    ListNode.append(vertexNode)
    return ListNode

def relax(u, tupleV, listNodes):
    #Obtener el vértice adyacente de u en forma de nodo. 
    for node in listNodes:
        if node.value == tupleV[0]:
            adjVertex = node        
            #Realizar relajo
            #REVISAR --> HICE ARREGLO PROVISIONAL INT()
            if adjVertex.distance > (u.distance + int(tupleV[1])):
                adjVertex.distance = u.distance + int(tupleV[1])
                adjVertex.parent = u    
            return

def initRelax(listNodes, v1):
    #Iniciar el relajamiento para cada vértice(nodo) del grafo.
    for node in listNodes:
        node.distance = 999999999
        node.parent = None
    v1.distance = 0
    return
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCIONES PARA DIJKSTRA(FINAL) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

############Estas son las funciones para buscar los autos más cercanos y verificar que puedan llegar a la persona############
"""~~~~~~~~~~~~~~~~~~~~ Nuevas funciones agregadas para el funcionamiento de los dijktras(INICIO) ~~~~~~~~~~~~~~~~~~~~"""
#Cargar elementos fijos y moviles al mapa.
def updateMap(map, name, direction):
    """Crear una función para agregar lugares fijos y objetos moviles al mapa"""
    #Ingresar en el mapa si no se encuetra dentro el elemento.
    if name not in map:
        if type(direction) is not list: #Ingresar la dirección al mapa como lista en caso de que no lo sea.
            map[name] = list(direction)
        else:
            map[name] = direction
    for key in map:
        if key == direction[0][0]:
            map[key].append((name,direction[0][1]))
        elif key == direction[1][0]:
            map[key].append((name,direction[1][1]))
    return  

#Dijktra que sirve para verificar que el auto pueda llegar a la posición de la persona.
def dijkstra(Graph,car,person):
    """Busca la distancia mas corta entre un nodo A y un nodo B"""
    assert Graph != {}, f"El mapa está vacío"
    #Verificar que los vértices v1 y v2 existen dentro del mapa.
    assert person in Graph, f"La persona {person} no sé encuentra en el mapa."
    assert car in Graph, f"El auto {car} no sé encuentra en el mapa."
    assert person in Graph and car in Graph, f"La persona {person} y el auto {car} no sé encuentran en el mapa."
    #Crear la lista de nodos(pasar los vértices a class = Node()).
    listVertex = list(Graph.keys())
    listTypeNodes = []
    for vertex in listVertex:
        listTypeNodes = DefinedVertexDijkstra(vertex, listTypeNodes)
    #Init relax
    for vertexNode in listTypeNodes:
        if vertexNode.value == car:
            initRelax(listTypeNodes, vertexNode)
            break
    #Definir lista de nodos visitados.
    listVisited = []
    #Ordenar la cola de nodos por su distancia.
    Queue = sorted(listTypeNodes, key=lambda node:node.distance)
    while Queue != []:
        #Obtener el vértice de la cola.
        u = Queue.pop(0)
        #Retorno True, si se cumple que puede llegar el auto a la persona.
        if u.value == person:
           return True
        #Agregar el vértice a la lista de visitados.
        listVisited.append(u.value)
        #Obtener los vértices adyacentes de u.
        adjacencyNodes = Graph[u.value]
        #Recorrer la lista de adyacencia de u.
        if adjacencyNodes != None:
            for vertex in adjacencyNodes:
                if vertex[0] not in listVisited:
                    relax(u,vertex, listTypeNodes)
        #Ordenar la cola de nodos por su distancia.
        sorted(listTypeNodes, key=lambda node:node.distance)
    #Retorno False ya que recorrí todo el mapa y nunca pude llegar a la persona.
    return False

#Dijkstra que sirve para buscar los autos más cercanos a la persona.
def dijkstra_allnodes(Graph, person, hash_movil_element):
    """Desde un nodo A el camino mas cerano a todos los nodos"""
    assert Graph != {}, f"El mapa está vacío"
    #Verificar que la persona existe dentro del mapa.
    assert person in Graph, f"La persona {person} no se encuentra en el mapa."
    #Crear la lista de nodos(pasar los vértices a class = Node()).
    listVertex = list(Graph.keys())
    listTypeNodes = []
    for vertex in listVertex:
        listTypeNodes = DefinedVertexDijkstra(vertex, listTypeNodes)
    #Init relax
    for vertexNode in listTypeNodes:
        if vertexNode.value == person: #Buscar persona e iniciar relajo.
            initRelax(listTypeNodes, vertexNode)
            break
    #Definir lista de nodos visitados.
    listVisited = []
    #Ordenar la cola de nodos por su distancia.
    Queue = sorted(listTypeNodes, key=lambda node:node.distance)
    #Definir una lista donde almacenamos el auto y la distancia del auto a la persona.
    list_Distance_And_Cars = []
    while Queue != []:
        #Obtener el primer vértice de la cola.
        u = Queue.pop(0)
        #Agregar el vértice a la lista de visitados.
        listVisited.append(u.value)
        #Obtener los vértices adyacentes de u. Ej: [('e1', 4), ('e2', 6)]
        adjacencyNodes = Graph[u.value]
        #Recorrer la lista de adyacencia de u.
        if adjacencyNodes != None:
            for tuple in adjacencyNodes:
                if tuple[0] not in listVisited:
                    relax(u, tuple, listTypeNodes)
        #Ordenar la cola de nodos por su distancia.
        sorted(listTypeNodes, key=lambda node:node.distance) 
        #Verificar quu el auto cercano pueda llegar a la persona.
        if u.value[0] == "C":
            if dijkstra(Graph, u.value, person) == True:
                #Agregamos a la lista los autos que la persona puede pagar.
                if hash_movil_element[person][1] >= ((u.distance + hash_movil_element[u.value][1]) / 4):  #Ej del hash: [[("e1",4),("e2",6)], 1500]
                    list_Distance_And_Cars.append((u.value,u.distance))
            if len(list_Distance_And_Cars) == 3: 
                return list_Distance_And_Cars  #Devolver la lista con el ranking de los 3 autos más cercanos que la persona puede pagar.  
    #En el peor de los casos es que no hayan al menos 3 autos, devolver error.
    assert list_Distance_And_Cars == 3, f"No sé pudieron devolver al menos tres autos."
"""~~~~~~~~~~~~~~~~~~~~ Nuevas funciones agregadas para el funcionamiento de los dijktras(FINAL) ~~~~~~~~~~~~~~~~~~~~"""

# 3- 
def encontrar_autos_cercanos(map, persona, hash_movil_element):
    """retorna una tupla de los 3 autos mas cercanos"""
    assert persona[0] == "P", f"Incorrecto, {persona} no es una persona"
    direction = hash_movil_element[persona][0] 
    #Se ingresa la persona al mapa.
    updateMap(map, persona, direction)
    #Se buscan los tres autos que puede pagar más cercanos a la persona.
    listNearbyCars = dijkstra_allnodes(map, persona, hash_movil_element)
    return listNearbyCars #Devuelve una lista como por ej: [('C1',30),('C2',40),('C3',50)]

# 4- 
def camino_mas_corto(Graph, direction_1, direction_2): #¿Para direcciones de tipo {("e3",7),("e5",8)}?
    """retorna el camino mas corto entre las dos direcciones"""
    assert Graph != {}, f"El mapa está vacío"
    #Verificar que las esquinas de las direcciones existen dentro del mapa.
    direction_1 = list(direction_1)
    direction_2 = list(direction_2)
    assert direction_1[0][0] in Graph, f"La esquina {direction_1[0][0]} de la {direction_1} no sé encuentra en el mapa"
    assert direction_1[1][0] in Graph, f"La esquina {direction_1[1][0]} de la {direction_1} no sé encuentra en el mapa" 
    assert direction_2[0][0] in Graph, f"La esquina {direction_2[0][0]} de la {direction_2} no sé encuentra en el mapa"
    assert direction_2[1][0] in Graph, f"La esquina {direction_2[1][0]} de la {direction_2} no sé encuentra en el mapa" 
    #Obtener los nombres de la direcciones inicial y final.
    listVertex = list(Graph.keys())
    final_destination = "Destino Final" #Se actualiza a un lugar fijo en el caso de que la dirección esté asignada a este.
    for key in listVertex:
        if Graph[key] == direction_1:
            person = key
        elif Graph[key] == direction_2:
            final_destination = key
    #En el caso de que el destino no sé encuentre en el mapa lo ingreso.
    if final_destination == "Destino Final":
        updateMap(Graph, final_destination, direction_2)
        listVertex = list(Graph.keys())
    #Crear la lista de nodos(pasar los vértices a class = Node()).
    listTypeNodes = []
    for vertex in listVertex:
        listTypeNodes = DefinedVertexDijkstra(vertex, listTypeNodes)
    #Init relax
    for vertexNode in listTypeNodes:
        if vertexNode.value == person:
            initRelax(listTypeNodes, vertexNode)
            break
    #Definir lista de nodos visitados.
    listVisited = []
    #Ordenar la cola de nodos por su distancia.
    Queue = sorted(listTypeNodes, key=lambda node:node.distance)
    while Queue != []:
        #Obtener el vértice de la cola.
        u = Queue.pop(0)
        #Si se cumple es que llegue a la dirección de destino.
        if u.value == final_destination:
           #Obtener el camino más corto de "D1" a "D2".
                listShortestPath = []
                while u.parent != None:
                    listShortestPath.insert(0, u.value)
                    u = u.parent
                listShortestPath.insert(0, u.value)
                return listShortestPath #Retorna una lista como está ['D1', 'e1', 'e3', 'e5', 'e7', 'e8', 'e10', 'D2']
        #Agregar el vértice a la lista de visitados.
        listVisited.append(u.value)
        #Obtener los vértices adyacentes de u.
        adjacencyNodes = Graph[u.value]
        #Recorrer la lista de adyacencia de u.
        if adjacencyNodes != None:
            for vertex in adjacencyNodes:
                if vertex[0] not in listVisited:
                    relax(u,vertex, listTypeNodes)
        #Ordenar la cola de nodos por su distancia.
        sorted(listTypeNodes, key=lambda node:node.distance)
    #Retorno False ya que recorrí todo el mapa y nunca pude llegar a la dirección de destino.
    return False

#5-
def crear_viaje(map, person, direction, hash_movil_element, hash_fix_element):
    ####ARREGLANDO COSAS
    for e in hash_movil_element:
        if e[0] == 'C':
            dire = hash_movil_element[f'{e}'][0]
            updateMap(map,e,dire)

    """Crea el viaje de uber"""
    print(f'------ Bienvenido {person} ------')
    #Validar la dirección.
    direction = eval("direction")
    if type(direction) is str: #Dirección de lugar fijo, por ej: "S1", "A5", "H2".
        assert validar_lugares(direction) is True, f"Dirección Inválida"
        direction = hash_fix_element[direction] #Obtener la dirección de un lugar fijo.
    else: #Dirección de lugar fijo, por ej: {("e3",7),("e5",8)}.
        direction = list(direction)
        assert direction[0][0] in map, f"La esquina {direction[0][0]} de la {direction} no sé encuentra en el mapa"
        assert direction[1][0] in map, f"La esquina {direction[1][0]} de la {direction} no sé encuentra en el mapa" 
    #Buscar los tres autos que la persona puede pagar más cercanos.
    autos_cercanos = encontrar_autos_cercanos(map, person, hash_movil_element)
    #Casos 1 -> No hay autos cercanos
    if not autos_cercanos:
        print('-- No hay autos cercanos que puedan realizar el viaje --')
        return
    #Caso 2 -> Muestra una lista de autos cercanos
    print('####Estos son los autos mas cercanos####')
    print('Elegir entre:')
    indice = 0
    for auto in autos_cercanos:
        if indice == 0:
            print('|Autos|Costo|')
        print(auto)
        indice += 1
    #Elije el auto
    auto = str(input('Elija un auto: '))
    auto = auto.upper()
    #Validación del auto
    while (auto[0] != "C") or (int(auto[1]) > indice):
        print('// Auto Invalido, vuelva a ingresar //')
        auto = str(input('Elija un auto: '))
        auto = auto.upper()
    #Crea el camino hacia destino.
    direction_person = hash_movil_element[person][0]
    camino_destino = camino_mas_corto(map, direction_person, direction)
    #Actualizar direcciones en el mapa de la persona y el auto.
    map[auto] = direction
    map[person] = direction
    #Actualizar direcciones en el hash de la persona y el auto.
    hash_movil_element[auto][0] = direction
    hash_movil_element[person][0] = direction 
    #Actualizar monto de la persona en el hash.
    for car in autos_cercanos:
        if car[0] == auto:
            distance = car[1] #Obtengo la distancia (auto --> persona)
    hash_movil_element[person][1] = (hash_movil_element[person][1] - ((distance +  hash_movil_element[auto][1]) / 4))
    #Validar que el camino de destino exista.
    if camino_destino != False:
        return camino_destino
    else:
        return
    
#La comenté por las dudas pero arriba estaría la función de crear el viaje.
"""def crear_viaje(persona,direccion):
    #Crea el viaje de uber
    print(f'------ Bienvenido {persona} ------')
    #Validar la direccion

    autos_cercanos = encontrar_autos_cercanos(persona)

    autos_cercanos = [('C1',30),('C2',40),('C3',50)]#Borrar una vez implementada la funcion
    #Casos 1 -> No hay autos cercanos
    if not autos_cercanos:
        print('-- No hay autos cercanos que puedan realizar el viaje --')
        return
    #Caso 2 -> Muestra una lista de autos cercanos
    
    print('####Estos son los Autos mas Cercanos####')
    print('elejir entre:')
    indice = 0
    for auto in autos_cercanos:
        if indice == 0:
            print('|Autos|Costo|')
        print(auto,'-->',indice)
        indice += 1
    #Elije el auto
    auto = int(input('elijo el auto: '))
    #Validacion del auto
    while auto >= indice:
        print('// Auto Invalido, vuelva a ingresar //')
        auto = int(input('elijo el auto: '))



    #Crea el camino hacia destino
    #camino_destino = camino_mas_corto()

    return None #camino_destino
    pass"""