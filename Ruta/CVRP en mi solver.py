def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = [
        [
            0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354,
            468, 776, 662
        ],
        [
            548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674,
            1016, 868, 1210
        ],
        [
            776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164,
            1130, 788, 1552, 754
        ],
        [
            696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822,
            1164, 560, 1358
        ],
        [
            582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708,
            1050, 674, 1244
        ],
        [
            274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628,
            514, 1050, 708
        ],
        [
            502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856,
            514, 1278, 480
        ],
        [
            194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320,
            662, 742, 856
        ],
        [
            308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662,
            320, 1084, 514
        ],
        [
            194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388,
            274, 810, 468
        ],
        [
            536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764,
            730, 388, 1152, 354
        ],
        [
            502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114,
            308, 650, 274, 844
        ],
        [
            388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194,
            536, 388, 730
        ],
        [
            354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0,
            342, 422, 536
        ],
        [
            468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536,
            342, 0, 764, 194
        ],
        [
            776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274,
            388, 422, 764, 0, 798
        ],
        [
            662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730,
            536, 194, 798, 0
        ],
    ]
    data['demands'] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    data['vehicle_capacity'] = 15
    data['num_vehicles'] = 4
    data['depot'] = 0
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
            output += "\n\n La ruta para el vehiculo {} :\n 0 ".format(numero)
            numero += 1 
        else:
            output += "-> {} ".format(camino[i])
    print (output)
    
def main():
    data = create_data_model()

    arcos = vecinoMasCercano(data)

    imprimirCamino (data, arcos)
    
main()























