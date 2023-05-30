
"""with open('path','w') as file:
    file.write()

-create_map
<local_path>. """

from funciones import crear_mapa,crear_lugar,crear_persona

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
            with open('mapa.pickle', 'wb') as archivo:
                pickle.dump(mapa, archivo)
                print("-Mapa guardado-")

    else:
        print("Error Mapa ya existente, no se puede crear nuevo mapa")

elif args.load_fix_element:
    nombre = args.load_fix_element[0]
    direccion = args.load_fix_element[1]

    #Verificamos si el mapa existe
    with open('mapa.pickle', 'rb') as archivo:
        print('Cargando Mapa existente')
        mapa_cargado = pickle.load(archivo)
        print('Mapa Cargado exitosamente')

    #Lanzar error si el mapa no existe

    #Verificamos si objetos.pickle existe
    if os.path.isfile('objetos.pickle'):
        with open('objetos_fijos.pickle', 'rb') as archivo:
            print("Cargando Objetos existentes")
            lugares = pickle.load(archivo)
        
        #Usamos la funcion para crear lugares
        lugares = crear_lugar(lugares,nombre,direccion,mapa_cargado)

        #Guardamos
        with open('objetos_fijos.pickle', 'wb') as archivo:
            pickle.dump(lugares, archivo)
            print("-Lugares guardado-") 
            
    else:
        lugares = crear_lugar({},nombre,direccion,mapa_cargado)
        with open('objetos_fijos.pickle', 'wb') as archivo:
            pickle.dump(lugares, archivo)
            print("-Lugares guardado-")


    print(f'Se cargó el elemento fijo "{nombre}" en el mapa con dirección "{direccion}"')


elif args.load_movil_element:
    nombre = args.load_movil_element[0]
    direccion = args.load_movil_element[1]
    monto = args.load_movil_element[2]

    #Verificamos si el mapa existe
    with open('mapa.pickle', 'rb') as archivo:
        print('Cargando Mapa existente')
        mapa_cargado = pickle.load(archivo)
        print('Mapa Cargado exitosamente')
    
    #Lanzar error si mapa no existe

    #Logica
    if nombre[0] == "P":
        if os.path.isfile('objetos_personas.pickle'):
            #Cargamos las Personas
            with open('objetos_personas.pickle', 'rb') as archivo:
                print("Cargando Objetos existentes")
                personas = pickle.load(archivo)
            
            #Usamos la funcion para crear lugares
            personas = crear_persona(personas,nombre,direccion,monto,mapa_cargado)

            #Guardamos
            with open('objetos_personas.pickle', 'wb') as archivo:
                pickle.dump(personas, archivo)
                print("-Personas guardado-") 
                
        else:
            personas = crear_persona({},nombre,direccion,monto,mapa_cargado)
            with open('objetos_personas.pickle', 'wb') as archivo:
                pickle.dump(personas, archivo)
                print("-Personas guardado-")

    elif nombre[0] == "C":
        pass


    print(f'Se cargó el elemento móvil "{nombre}" en el mapa con dirección "{direccion}" y monto {monto}')


#Cargar Mapa ya que existe
"""
with open('mapa.pickle', 'rb') as archivo:
    print("Cargando Mapa existente")
    diccionario_cargado = pickle.load(archivo)

"""