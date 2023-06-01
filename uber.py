
"""with open('path','w') as file:
    file.write()

-create_map
<local_path>. """

from funciones import crear_mapa,crear_lugar,crear_persona,crear_auto

def hola():
    print ("Bienvenido Harpomaxx")



#Inicio Programa
####Logica
import os

ruta_archivo = "mapa.pickle"  # Reemplaza con la ruta del archivo que deseas verificar

mapa_existe = False
""" Parte de la logica de create MAP
if os.path.isfile(ruta_archivo):
    print("Mapa Anteriormente Creado")
    mapa_existe = True
"""
### Crea el Mapa
import argparse

parser = argparse.ArgumentParser(description='Comandos para Proyecto Uber')
# Comando create_map
parser.add_argument('-create_map',nargs=1,metavar=('path'), help='Crear mapa')
# Comando load_fix_element
parser.add_argument('-load_fix_element', nargs=2, metavar=('nombre', 'direccion'), help='Carga un elemento fijo en el mapa')
# Comando load_movil_element
parser.add_argument('-load_movil_element', nargs=3, metavar=('nombre', 'direccion', 'monto'), help='Carga un elemento móvil en el mapa')
#
args = parser.parse_args()

#Para serializar y guardar
import pickle

#local path = /mapa_ejemplo
if args.create_map:
    if mapa_existe == False:
        with open(f'./{args.create_map[0]}.txt', 'r') as file:
            #Dividimos las lineas del archivo
            primer_linea = file.readline()
            segunda_linea = file.readline()
            #Parseamos las Esquinas
            primer_linea = primer_linea[3:-2] #quitamos los caracteres del principio y final
            primer_linea = primer_linea.replace('"','') #quitamos las comillas demas
            segunda_linea = segunda_linea.replace(' ','')
            esquinas = primer_linea.split(',')
            #Parseamos las Calles
            segunda_linea = segunda_linea.split('{')[1].split('}')[0] #quitamos los caracteres del principio y final
            segunda_linea = segunda_linea.replace(' ','')
            segunda_linea = segunda_linea.split('),(')
            calles = []
            for valor in segunda_linea:
                if valor[0] == '(':
                    valor += ')'
                elif valor[-1] == ')':
                    valor = '(' + valor
                else:
                    valor = '(' + valor + ')'
                
                tupla = eval(valor)
                calles.append(tupla)

            print("-Creando mapa-")
            mapa = crear_mapa(esquinas,calles)
            print("-Mapa creado-")
            ##Hay que guardar el mapa
            with open('pickle/mapa.pickle', 'wb') as archivo:
                pickle.dump(mapa, archivo)
                print("-Mapa guardado-")

    else:
        print("Error Mapa ya existente, no se puede crear nuevo mapa")

elif args.load_fix_element:
    nombre = args.load_fix_element[0]
    direccion = args.load_fix_element[1]

    #Lanzar error si el mapa no existe

    #Cargamos el mapa
    with open('mapa.pickle', 'rb') as archivo:
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


    print(f'Se cargó el elemento fijo "{nombre}" en el mapa con dirección "{direccion}"')


elif args.load_movil_element:
    nombre = args.load_movil_element[0]
    direccion = args.load_movil_element[1]
    monto = args.load_movil_element[2]

    funciona = False
    #Verificamos si el mapa existe
    ruta_archivo = "pickle/mapa.pickle"

    assert os.path.exists(ruta_archivo),f'Error al cargar el mapa, Verifique si creo el mapa'

    #Cargamos el mapa
    with open('pickle/mapa.pickle', 'rb') as archivo:
        print('Cargando Mapa existente')
        mapa_cargado = pickle.load(archivo)
        print('Mapa Cargado exitosamente')
        funciona = True

    #Logica
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

    


#Cargar Mapa ya que existe
"""
with open('mapa.pickle', 'rb') as archivo:
    print("Cargando Mapa existente")
    diccionario_cargado = pickle.load(archivo)

"""