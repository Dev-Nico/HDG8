def create_data_model():
    #Se crean todos los datos importantes para ocupar en el programa
    """Stores the data for the problem."""
    archivo = open ("matriz_distancia.txt", "r")
    data = {}
    data['distance_matrix'] = []   
    for linea in archivo.readlines ():
        linea = linea.split(",")
        lista = []
        for dato in linea:
            lista.append(int(dato))
        data['distance_matrix'].append(lista)
    
    data['demands'] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    data['vehicle_capacity'] = 15
    data['num_vehicles'] = 4
    data['depot'] = 0
    archivo.close()
    return data

def minimo (data, arcos, demanda_total):
    vehiculos = data['num_vehicles']
    arcos_temporal = arcos[:] #Slicing para obtener una copia de la lista
    arco_posible = (0,0)    #Variable auxiliar para probar distintos arcos
    solucion = (0,0)        #Donde se almacena el arco final encontrado como nueva conexion
    origen = []             #Lista con todos los indices de los nodos de origen de cada arco
    destino = []            #Lista con todos los indices de los nodos de destino de cada arco
    minimo = 99999          #Distancia minima para hacer comparación
    demanda_camino = 0

    #Se llenan las listas de origen y destino (Se agrega el deposito a la lista destino)
    for arco in arcos:
        origen.append(arco[0])
        destino.append(arco[1])
    destino.append(0)

    for vehiculo in range(vehiculos):
        if (arcos_temporal): #Si existe al menos un arco para seguir revisando (arcos_temporal no está vacio)
            while(arco_posible[1] in origen): #Mientras la coordenada y del arco a revisar se encuentre en la lista de origen
                #print ("Arco posible y origen: ",arco_posible, origen)
                indice = origen.index(arco_posible[1])
                arco_posible = arcos_temporal[indice]
                origen.pop(indice)
                arcos_temporal.pop(indice)
            #Buscar el vecino más cercano de arco_posible legal (no visitado, es decir, no está en la lista destino)
            #Comparar con la distancia más corta encontrada y escoger el menor de ambos (guardar el menor en minimo)
            for i in range (len(data['distance_matrix'])):
                if ((data['distance_matrix'][arco_posible[1]][i]<minimo) and (i not in destino)
                    and (demanda_total[arcos.index(arco_posible)] + data['demands'][i] <= data['vehicle_capacity'])):
                    minimo = (data['distance_matrix'][arco_posible[1]][i])
                    solucion = (arco_posible[1] ,i)
                    demanda_camino = demanda_total[arcos.index(arco_posible)] + data['demands'][i]
            #El indice encontrado no debe estar en destino para no ser un nodo visitado
            arco_posible = (0,0) #Resetear el arco se hace al final

        else: #Si no quedan arcos por revisar en arcos_temporal o es el primer arco (arcos_temporal está vacío)
            for i in range (len(data['distance_matrix'])):
                if ((data['distance_matrix'][arco_posible[1]][i]<minimo) and
                    (i not in destino) and
                    ((data['distance_matrix'][arco_posible[1]][i]) != 0)):
                    minimo = (data['distance_matrix'][arco_posible[1]][i])
                    solucion = (arco_posible[1] ,i)
                    demanda_camino = data['demands'][i]
    #print (solucion, demanda_camino)
    return solucion, demanda_camino
                              

def vecinoMasCercano(data):
    arcos = [] #arcos que generan la solucion
    conexion_nueva = (0,0)
    demanda_total = []
    nueva_demanda = 0
    
    #Mientras no existan tantos arcos como nodos posibles
    while (len(arcos) < len(data['distance_matrix'])-1):
        conexion_nueva, nueva_demanda = minimo(data, arcos, demanda_total)
        arcos.append(conexion_nueva)
        demanda_total.append(nueva_demanda)
        #Agregar la distancia de cada conexion tambien es una buena idea
    return arcos


def imprimirCamino(data, arcos):
    f = open("test.txt","w")
    camino = []
    numero = 1

    #Formatear el camino en una lista de facil lectura
    for vehiculo in range(data['num_vehicles']):
        indice = 0
        camino.append(indice)
        for i in range (len(arcos)):
            if (indice in arcos[i]) and not (arcos[i][1] in camino):
                camino.append(arcos[i][1])
                indice = arcos[i][1]

    #dejar todo el camino en la variable output
    output = ''
    for i in range(len(camino)):
        if (camino[i] == 0):
            output += "\nLa ruta para el vehiculo {}:\n0".format(numero)
            numero += 1 
        else:
            output += " -> {}".format(camino[i])
    f.write(output)
    print (output)
    f.close()
    
def main():  
    data = create_data_model()

    arcos = vecinoMasCercano(data)
    
    imprimirCamino (data, arcos)
        
main()
