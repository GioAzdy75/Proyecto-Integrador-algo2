#Importamos los Modulos
from funciones import crear_mapa,crear_lugar,crear_persona,crear_auto,conocer_ubicacion,validar_lugares,crear_viaje
from funciones import preprocesando_mapa
import os
import argparse
import pickle


###- Para invocar las funciones desde la consola
parser = argparse.ArgumentParser(description='Comandos para Proyecto Uber')
# Comando create_map
parser.add_argument('-create_map',nargs=1,metavar=('path'), help='Crear mapa')
# Comando load_fix_element
parser.add_argument('-load_fix_element', nargs=2, metavar=('nombre', 'direccion'), help='Carga un elemento fijo en el mapa')
# Comando load_movil_element
parser.add_argument('-load_movil_element', nargs=3, metavar=('nombre', 'direccion', 'monto'), help='Carga un elemento móvil en el mapa')
# Comando location_element
parser.add_argument('-location_element', nargs=1, metavar=('nombre'), help='Muestra la ubicacion del elemento')
# Comando create_trip
parser.add_argument('-create_trip', nargs=2, metavar=('nombre','direccion/elemento'), help='Crea el viaje')
#
args = parser.parse_args()

###- Creamos el Mapa
if args.create_map:
    #Verificamos si el mapa existe
    ruta_archivo = "pickle/mapa.pickle"
    assert not (os.path.exists(ruta_archivo)),f'Error, Mapa creado anteriormente'
    #Verificamos si el archivo mapa.txt existe
    assert (os.path.exists(f'{args.create_map[0]}.txt')),f'Error, No se encuentra {args.create_map[0]}.txt'
    #Verificamos que la carpeta exista sino la creamos
    if not os.path.exists('pickle'):
        os.makedirs('pickle')
        print(f"Se creó la carpeta '{'pickle'}'")
        
    if True:
        with open(f'./{args.create_map[0]}.txt', 'r') as file:
            #Dividimos las lineas del archivo
            primer_linea = file.readline()
            segunda_linea = file.readline()
            #Incia el proceso
            print('-Leyendo Mapa-')
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
            print("-Parseando Mapa-")
            
            #Empezamos con el mapa
            print("-Creando mapa-")
            mapa = crear_mapa(esquinas,calles)
            print("-Mapa creado-")
            ##Hay que guardar el mapa
            with open('pickle/mapa.pickle', 'wb') as archivo:
                pickle.dump(mapa, archivo)
                print("-Mapa guardado-")

            ##Procesando al azar el mapa
            mapa_procesado = preprocesando_mapa(mapa)
            print('Preprocesando Mapa')
            with open('pickle/mapa_preprocesado.pickle', 'wb') as archivo:
                pickle.dump(mapa, archivo)
                print("-MapaProcesado guardado-")
            print('#######################')
            print('map created successfully')

###- Cargamos los elementos fijos
elif args.load_fix_element:
    nombre = args.load_fix_element[0]
    direccion = args.load_fix_element[1]

    #Parsear Direccion
    tupla = []
    for elemento in direccion.split():
        valores = elemento.strip("<>").split(",")
        tupla.append((valores[0], int(valores[1])))

    direccion = tupla

    #Lanzar error si el lugar fijo no es un almacen,kiosco,etc
    assert validar_lugares(nombre),f'No es valida la etiqueta: {nombre}'

    #Verificamos si el mapa existe
    ruta_archivo = "pickle/mapa.pickle"
    assert os.path.exists(ruta_archivo),f'Error al cargar el mapa, Verifique si creo el mapa'

    #Cargamos el mapa
    with open('pickle/mapa.pickle', 'rb') as archivo:
        print('Cargando Mapa existente')
        mapa_cargado = pickle.load(archivo)
        print('Mapa Cargado exitosamente')

    #Verificamos si objetos.pickle existe
    if os.path.isfile('pickle/objetos_fijos.pickle'):
        with open('pickle/objetos_fijos.pickle', 'rb') as archivo:
            print("Cargando Objetos existentes")
            lugares = pickle.load(archivo)
        
        #Usamos la funcion para crear lugares
        lugares = crear_lugar(lugares,nombre,direccion,mapa_cargado)

        #Guardamos
        with open('pickle/objetos_fijos.pickle', 'wb') as archivo:
            pickle.dump(lugares, archivo)
            print("-Lugares guardado-") 
            
    else:
        lugares = crear_lugar({},nombre,direccion,mapa_cargado)
        with open('pickle/objetos_fijos.pickle', 'wb') as archivo:
            pickle.dump(lugares, archivo)
            print("-Lugares guardado-")

    print(f'Se cargó el elemento fijo : {nombre} -->,{lugares[nombre]}')

###- Carga de elementos Moviles
elif args.load_movil_element:
    nombre = args.load_movil_element[0]
    direccion = args.load_movil_element[1]
    monto = int(args.load_movil_element[2])
    
    #Parseamos la direccion
    tupla = []
    for elemento in direccion.split():
        valores = elemento.strip("<>").split(",")
        tupla.append((valores[0], int(valores[1])))
    direccion = tupla

    #Verificamos si el mapa existe
    ruta_archivo = "pickle/mapa.pickle"
    assert os.path.exists(ruta_archivo),f'Error al cargar el mapa, Verifique si creo el mapa'

    #Cargamos el mapa
    with open('pickle/mapa.pickle', 'rb') as archivo:
        print('Cargando Mapa existente')
        mapa_cargado = pickle.load(archivo)
        print('Mapa Cargado exitosamente')

    #Si se carga una Persona
    if nombre[0] == "P":
        if os.path.isfile('pickle/objetos_personas.pickle'):
            #Cargamos las Personas
            with open('pickle/objetos_personas.pickle', 'rb') as archivo:
                print("Cargando Objetos existentes")
                personas = pickle.load(archivo)
            
            #Usamos la funcion para crear la nueva persona
            personas = crear_persona(personas,nombre,direccion,monto,mapa_cargado)

            #Guardamos
            with open('pickle/objetos_personas.pickle', 'wb') as archivo:
                pickle.dump(personas, archivo)
                print("-Personas guardado-") 
            
            print(f'Se cargó el elemento móvil Persona = {nombre} -->,{personas[nombre]}')
                
        else:
            personas = crear_persona({},nombre,direccion,monto,mapa_cargado)
            with open('pickle/objetos_personas.pickle', 'wb') as archivo:
                pickle.dump(personas, archivo)
                print("-Personas guardado-")
                
            print(f'Se cargó el elemento móvil Persona = {nombre} -->,{personas[nombre]}')

    #Si se carga un Auto
    elif nombre[0] == "C":
        if os.path.isfile('pickle/objetos_autos.pickle'):
            #Cargamos los autos
            with open('pickle/objetos_autos.pickle', 'rb') as archivo:
                print("Cargando Autos existentes")
                autos = pickle.load(archivo)
            
            #Usamos la funcion para crear el auto nuevo
            autos = crear_auto(autos,nombre,direccion,monto,mapa_cargado)

            #Guardamos
            with open('pickle/objetos_autos.pickle', 'wb') as archivo:
                pickle.dump(autos, archivo)
                print("-Autos guardado-") 
            
            print(f'Se cargó el elemento móvil Persona = {nombre} -->,{autos[nombre]}')
        else:
            autos = crear_auto({},nombre,direccion,monto,mapa_cargado)
            with open('pickle/objetos_autos.pickle', 'wb') as archivo:
                pickle.dump(autos, archivo)
                print("-Auto guardado-")
            print(f'Se cargó el elemento móvil Persona = {nombre} -->,{autos[nombre]}')

###- Te da la ubicacion de los Objetos
elif args.location_element:
    nombre = args.location_element[0]

    #Verificamos si el mapa existe
    ruta_archivo = "pickle/mapa.pickle"
    assert os.path.exists(ruta_archivo),f'Error al cargar el mapa, Verifique si creo el mapa'

    #Cargamos el mapa
    mapa_cargado = {}

    #Locacion Personas
    if nombre[0] == 'P':
        #verificamos que exista el hash de personas
        ruta_archivo = "pickle/objetos_personas.pickle"
        assert os.path.exists(ruta_archivo),f'Error al cargar las personas, Verifique si anadio personas'
        
        with open('pickle/objetos_personas.pickle', 'rb') as archivo:
            print('Cargando Objetos Moviles existente')
            mapa_cargado = pickle.load(archivo)
            print('Objetos Moviles cargados exitosamente')
    
    #Locacion Autos
    elif nombre[0] == 'C':
        #verificamos que exista el hash de personas
        ruta_archivo = "pickle/objetos_autos.pickle"
        assert os.path.exists(ruta_archivo),f'Error al cargar los autos, Verifique si anadio autos'
        
        with open('pickle/objetos_autos.pickle', 'rb') as archivo:
            print('Cargando Objetos Moviles existente')
            mapa_cargado = pickle.load(archivo)
            print('Objetos Moviles cargados exitosamente')
    
    #Locacion Lugares Fijos
    elif validar_lugares(nombre[0]):
        #verificamos que exista el hash de personas
        ruta_archivo = "pickle/objetos_fijos.pickle"
        assert os.path.exists(ruta_archivo),f'Error al cargar los lugares, Verifique si anadio lugares'
        
        with open('pickle/objetos_fijos.pickle', 'rb') as archivo:
            print('Cargando Objetos Fijos existente')
            mapa_cargado = pickle.load(archivo)
            print('Objetos Fijos cargados exitosamente')
        
    print(conocer_ubicacion(nombre,mapa_cargado))
    
elif args.create_trip:
    #Verificamos si el mapa existe
    ruta_archivo = "pickle/mapa.pickle"
    assert os.path.exists(ruta_archivo),f'Error al cargar el mapa, Verifique si creo el mapa'

    #Cargamos el mapa
    with open('pickle/mapa.pickle', 'rb') as archivo:
        print('Cargando Mapa existente')
        mapa_cargado = pickle.load(archivo)
        print('Mapa Cargado exitosamente')

    #Verificamos si existe los objetos fijos
    ruta_archivo = "pickle/objetos_fijos.pickle"
    assert os.path.exists(ruta_archivo),f'Error al cargar los lugares, Verifique si anadio lugares'
        
    with open('pickle/objetos_fijos.pickle', 'rb') as archivo:
        print('Cargando Objetos Fijos existente')
        hash_fijos = pickle.load(archivo)
        print('Objetos Fijos cargados exitosamente')

    #verificamos que exista los autos
    ruta_archivo = "pickle/objetos_autos.pickle"
    assert os.path.exists(ruta_archivo),f'Error al cargar los autos, Verifique si anadio autos'
        
    with open('pickle/objetos_autos.pickle', 'rb') as archivo:
        print('Cargando Objetos Moviles existente')
        hash_autos = pickle.load(archivo)
        print('Objetos Moviles cargados exitosamente')

    #verificamos que exista el hash de personas
    ruta_archivo = "pickle/objetos_personas.pickle"
    assert os.path.exists(ruta_archivo),f'Error al cargar las personas, Verifique si anadio personas'
        
    with open('pickle/objetos_personas.pickle', 'rb') as archivo:
        print('Cargando Objetos Moviles existente')
        hash_personas = pickle.load(archivo)
        print('Objetos Moviles cargados exitosamente')

    persona = args.create_trip[0]
    direccion = args.create_trip[1]
    
    hash_moviles = {}
    hash_moviles.update(hash_personas)
    hash_moviles.update(hash_autos)

    #Parsear Direccion
    if not validar_lugares(direccion):
        tupla = []
        for elemento in direccion.split():
            valores = elemento.strip("<>").split(",")
            tupla.append((valores[0], int(valores[1])))
        direccion = tupla
    
    ##Mapa Preprocesado
    mapa_procesado = {}
    with open('pickle/mapa_preprocesado.pickle', 'rb') as archivo:
        mapa_procesado = pickle.load(archivo)
    
    viaje_final = crear_viaje(mapa_cargado,persona,direccion,hash_moviles,hash_fijos,mapa_procesado)

    #Verificamos si es un str
    if isinstance(viaje_final, str):
        print(viaje_final)
    else:
        #Actualizamos los archivos pickle
        with open('pickle/objetos_autos.pickle', 'wb') as archivo:
            pickle.dump(hash_autos, archivo)
            print("-hash autos actualizados-") 
        with open('pickle/objetos_personas.pickle', 'wb') as archivo:
            pickle.dump(hash_personas, archivo)
            print("-hash personas actualizados-")
        
        print(viaje_final)