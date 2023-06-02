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
    #Luego borrar
    direccion = eval(direccion)
    #

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
    #Luego borrar
    direccion = eval(direccion)
    #

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
    #Luego borrar
    direccion = eval(direccion)
    #

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


def dijkstra(graph,nodeA,nodeB):
    """Busca la distancia mas corta entre un nodo A y un nodo B"""
    pass

def dijkstra_allnodes(graph,nodeA):
    """Desde un nodo A el camino mas cerano a todos los nodos"""
    pass

# 3-
def encontrar_autos_cercanos(persona):
    """retorna una tupla de los 10 autos mas cercanos"""
    pass

# 4-
def camino_mas_corto(direccion_1,direccion_2):
    """retorna el camino mas corto entre las dos direcciones"""
    pass


def crear_viaje(persona,direccion):
    """Crea el viaje de uber"""
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
    pass