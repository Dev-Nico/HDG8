from no3 import nodo

#Continuar con el otro formato de texto
def leerArchivoXNNN(nombreTexto):
    archivo = open(nombreTexto,"r")
    lista = []
    modo = 0
    vehiculos = 0
    capacidad = 0
    #Separar la matriz y agregarla como enteros a la lista en el formato deseado
    for linea in archivo.readlines():
        linea = linea.split()
        if (linea):
            if(linea[0] == "NUMBER"):
                modo = 1
            elif (linea[0] == "CUST"):
                modo = 2
            elif (modo == 1):
                vehiculos = int(linea[0])
                capacidad = int(linea[1])
                modo = 0
            elif (modo == 2):
                lista.append([int(linea[1]), int(linea[2]),
                              int(linea[3]), 0,
                              int(linea[4]), int(linea[5])]) 
    archivo.close()
    return (lista, vehiculos, capacidad)


def leerArchivoPP(nombreTexto):
    archivo = open(nombreTexto,"r")
    lista = []
    vehiculos = 200
    capacidad = 100
    #Separar la matriz y agregarla como enteros a la lista en el formato deseado
    for linea in archivo.readlines():
        linea = linea.split()
        lista.append([int(linea[1]), int(linea[2]),
                      int(linea[7]), 0,
                      int(linea[3]), int(linea[4])]) 
    archivo.close()
    return (lista, vehiculos, capacidad)


def leerArchivoBXXX(nombreTexto):
    archivo = open(nombreTexto,'r')
    lista = []
    #Cambiar de modo para permitir diferente tipo de cambio de procesamiento de texto
    modo = 0
    capacidad = 0
    vehiculos = 130
    for linea in archivo.readlines ():
        linea = linea.split()
        if (linea[0] == "NODE_COORD_SECTION"):
            modo = 1
        elif (linea[0] == "DEMAND_SECTION" or
              linea[0] == "PICKUP_SECTION"):
            modo =2
        elif(linea[0] == "TIME_WINDOW_SECTION"):
            modo = 3
            #Por default el nodo deposito no tiene ventana de tiempo definida
            lista[0].append(0)
            lista[0].append(9999)
        elif(linea[0] == "CAPACITY_VOL"):
            capacidad = int(linea[2])
        elif (linea[0] == "STANDTIME_SECTION"):
            modo = 4
        elif (modo == 1):
            lista.append([int(linea[1]),int(linea[2])])
        elif (modo == 2):
            lista[int(linea[0])-1].append(int(linea[1]))
        elif (modo == 3):
            #separador[0] sieempre contiene un indice, separador[1] es el que contiene el dato a separar
            for separador in enumerate(linea):    
                if (separador[0] != 0):               
                    aux = separador[1].split(':')
                    hora = int(aux[0])*60
                    minutos = hora + int(aux[1])
                    if (separador[0] == 1):
                        llegada = minutos
                    elif (separador [0] == 2):
                        ida = minutos
            lista[int(linea[0])-1].append(llegada)
            lista[int(linea[0])-1].append(ida)
    archivo.close()
    return (lista, vehiculos, capacidad)
