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

def crear_lugar(hash_lugares,nombre,direccion,mapa):
    """retorna el hash con los lugares actualizados"""
    assert direccion in mapa,f'El objeto {nombre}, no se cargo, no existe direccion {direccion} en el mapa'
    assert nombre not in hash_lugares,f'El objeto ya existe dentro del mapa'
    hash_lugares[nombre] = direccion
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
    return hash_movil[objeto_movil]



# 3-
def encontrar_autos_cercanos(persona):
    """retorna una tupla de los 10 autos mas cercanos"""
    pass

# 4-
def camino_mas_corto(direccion_1,direccion_2):
    """retorna el camino mas corto entre las dos direcciones"""
    pass