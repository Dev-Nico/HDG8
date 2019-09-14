from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from leer_documentos import leerArchivoXNNN
from leer_documentos import leerArchivoPP
from leer_documentos import leerArchivoBXXX
from no3 import nodo

def crear_modelo():
    """Stores the data for the problem."""
    data = {}
    lista = []
    vehiculos = 0
    capacidad = 0
    indice = 0
    
    nombreArchivo = "15PP.dat"
    tipoLectura = 2

    #Archivos .txt
    if (tipoLectura == 1):
        lista, vehiculos, capacidad = leerArchivoXNNN(nombreArchivo)
        
    #archivos .dat
    elif (tipoLectura == 2):
        lista, vehiculos, capacidad = leerArchivoPP(nombreArchivo)
        
    #archivos .vrp
    elif (tipoLectura == 3):
        lista, vehiculos, capacidad = leerArchivoBXXX(nombreArchivo)
   
    for cosas in lista:
        lista[indice] = nodo(cosas[0],cosas[1],
                             cosas[2],cosas[3],
                             cosas[4],cosas[5])
        indice += 1

    data['nodos'] = lista
    capacidad_vehiculos = []
    for i in range(vehiculos):
        capacidad_vehiculos.append(capacidad)
    data['capacidad_vehiculos'] = capacidad_vehiculos
    data['numero_vehiculos'] = vehiculos
    data['deposito'] = 0
    return data

def print_solution(data, manager, routing, assignment):
    """Imprimir la asignación en consola."""
    time_dimension = routing.GetDimensionOrDie('Time')
    total_time = 0
    total_load = 0
    print("hello dude")
    for vehicle_id in range(data['numero_vehiculos']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['nodos'][node_index].carga - data['nodos'][node_index].descarga
            time_var = time_dimension.CumulVar(index)
            plan_output += '{0} Time({1},{2}; Load({3}) -> '.format(
                manager.IndexToNode(index), assignment.Min(time_var),
                assignment.Max(time_var), route_load)
            index = assignment.Value(routing.NextVar(index))
        time_var = time_dimension.CumulVar(index)
        plan_output += '{0} Time({1},{2}; ; Load({3})\n'.format(
            manager.IndexToNode(index), assignment.Min(time_var),
            assignment.Max(time_var), route_load)
        plan_output += 'Time of the route: {}min\n'.format(
            assignment.Min(time_var))
        plan_output += 'Load of the route: {}\n'.format(route_load)
        print(plan_output)
        total_time += assignment.Min(time_var)
    print('Total time of all routes: {}min'.format(total_time))

def main():
    """Solve the VRP with time windows."""
    data = crear_modelo()
    manager = pywrapcp.RoutingIndexManager(
        len(data['nodos']), data['numero_vehiculos'], data['deposito'])
    routing = pywrapcp.RoutingModel(manager)

    def time_callback(from_index, to_index):
        """Returns the travel time between the two nodes."""
        # Convert from routing variable Index to time matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        x = abs(data['nodos'][from_node].coordenadaX-data['nodos'][to_node].coordenadaX)
        y = abs(data['nodos'][from_node].coordenadaY-data['nodos'][to_node].coordenadaY)
        return x+y

    transit_callback_index = routing.RegisterTransitCallback(time_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['nodos'][from_node].carga - data['nodos'][from_node].descarga

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        30,  # null capacity slack
        data['capacidad_vehiculos'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')
 
    time = 'Time'
    routing.AddDimension(
        transit_callback_index,
        3000,  # allow waiting time
        3000,  # maximum time per vehicle
        False,  # Don't force start cumul to zero.
        time)
    time_dimension = routing.GetDimensionOrDie(time)
    # Add time window constraints for each location except depot.
    for location_idx in range (len(data['nodos'])):
        if location_idx == 0:
            continue
        index = manager.NodeToIndex(location_idx)
        time_dimension.CumulVar(index).SetRange(data['nodos'][location_idx].llegada,
                                                data['nodos'][location_idx].ida)
    # Add time window constraints for each vehicle start node.
    for vehicle_id in range(data['numero_vehiculos']):
        index = routing.Start(vehicle_id)
        time_dimension.CumulVar(index).SetRange(data['nodos'][0].llegada,
                                                data['nodos'][0].ida)
    print("hello dude")
    for i in range(data['numero_vehiculos']):
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.Start(i)))
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.End(i)))

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.TABU_SEARCH)
    
    search_parameters.time_limit.seconds = 30
    search_parameters.log_search = True
  
    assignment = routing.SolveWithParameters(search_parameters)

    if assignment:
        print_solution(data, manager, routing, assignment)

if __name__ == '__main__':
  main()
