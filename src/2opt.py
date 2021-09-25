from py2opt.routefinder import RouteFinder
from utils import Utils
from tour import Tour
import tspsolve
import numpy as np
from pytsp import christofides_tsp
truck_time_matrix = Utils.get_instance().cal_truck_time_matrix()
num_node = len(Utils.get_instance().data)
# cities_names = ['A', 'B', 'C', 'D']
# dist_mat = [[0, 29, 15, 35], [29, 0, 57, 42], [15, 57, 0, 61], [35, 42, 61, 0]]

T = Tour()
T.cities = [0, 3, 5, 6, 9]
T.get_cities_matrix()
# path = tspsolve.nearest_neighbor(np.array(truck_time_matrix))
# path = path.tolist()
# print(path)
#
# route_finder = RouteFinder(truck_time_matrix, path, iterations=20)
# best_distance, best_route = route_finder.solve()
#
# print(best_distance)
# print(best_route)

path = christofides_tsp.christofides_tsp(np.array(T.cities_matrix))
real_path = [T.cities[i] for i in path]
print(path)
print(real_path)