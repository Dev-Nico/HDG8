#Para poder hacer funcionar se necesita del comadndo:
#python -m pip install --upgrade --user ortools
from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def create_data_model():
  """Stores the data for the problem."""
  archivo = open ("matriz_tiempo.txt", "r")
  archivo2 = open ("ventana_tiempo.txt", "r")
  data = {}
  capacidad = 6 #Cantidad de pacientes que puede visitar cada vehiculo
  data['num_vehicles'] = 3
  
  #Creación de matriz de tiempo segun input
  data['time_matrix'] = []
  for linea in archivo.readlines ():
        linea = linea.split(",")
        lista = []
        for dato in linea:
            lista.append(int(dato))
        data['time_matrix'].append(lista)

  #Definición de ventanas de tiempo
  data['time_windows'] = []
  for linea in archivo2.readlines ():
    linea = linea.split(",")
    data['time_windows'].append((int(linea[0]),int(linea[1])))

  print (data['time_windows'])
  """for i in range (len(data['time_matrix'])):
    data['time_windows'].append((0,1440))"""

  #La capacidad de cada vehiculo determina la cantidad de pacientes a visitar
  data['capacidad'] = []
  for i in range(data['num_vehicles']):
    data['capacidad'].append(capacidad)

  #La demanda es reemplazada por la cantidad de visitas que se realizan en una ruta
  data['demanda'] = []
  for i in range (len(data['time_matrix'])):
    if (i == 0):
      data['demanda'].append(0)
    else:
      data['demanda'].append(1)
      
  data['depot'] = 0
  archivo.close()
  return data

def print_solution(data, manager, routing, assignment):
    """Prints assignment on console."""
    output = open ("output.txt", "w")
    time_dimension = routing.GetDimensionOrDie('Time')
    total_time = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        while not routing.IsEnd(index):
            time_var = time_dimension.CumulVar(index)
            output.write(str(manager.IndexToNode(index)) + ', ')#insert mio
            plan_output += '{0} Time({1},{2}) -> '.format(
                manager.IndexToNode(index), assignment.Min(time_var),
                assignment.Max(time_var))
            index = assignment.Value(routing.NextVar(index))
        time_var = time_dimension.CumulVar(index)
        output.write(str(manager.IndexToNode(index)) + '\n')#insert mio
        plan_output += '{0} Time({1},{2})\n'.format(manager.IndexToNode(index),
                                                    assignment.Min(time_var),
                                                    assignment.Max(time_var))
        plan_output += 'Time of the route: {}min\n'.format(
            assignment.Min(time_var))
        print(plan_output)
        total_time += assignment.Min(time_var)
    output.close()
    print('Total time of all routes: {}min'.format(total_time))

def main():
    """Solve the VRP with time windows."""
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['time_matrix']),
                                           data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def time_callback(from_index, to_index):
        """Returns the travel time between the two nodes."""
        # Convert from routing variable Index to time matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['time_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(time_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demanda'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        30,  # null capacity slack
        data['capacidad'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')
    
    time = 'Time'
    routing.AddDimension(
        transit_callback_index,
        60,  # allow waiting time
        1440,  # maximum time per vehicle
        False,  # Don't force start cumul to zero.
        time)
    time_dimension = routing.GetDimensionOrDie(time)
    # Add time window constraints for each location except depot.
    for location_idx, time_window in enumerate(data['time_windows']):
        if location_idx == 0:
            continue
        index = manager.NodeToIndex(location_idx)
        time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])
    # Add time window constraints for each vehicle start node.
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        time_dimension.CumulVar(index).SetRange(data['time_windows'][0][0],
                                                data['time_windows'][0][1])
    for i in range(data['num_vehicles']):
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.Start(i)))
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.End(i)))
        
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.TABU_SEARCH)
    
    search_parameters.time_limit.seconds = 10
    search_parameters.log_search = True
    
    assignment = routing.SolveWithParameters(search_parameters)
    
    if assignment:
        print_solution(data, manager, routing, assignment)

if __name__ == '__main__':
  main()
