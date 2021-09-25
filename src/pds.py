import numpy as np
from pytsp import christofides_tsp

from utils import Utils
from ortools.linear_solver import pywraplp
from tour import Tour
from list import List
import tspsolve
from py2opt.routefinder import RouteFinder


# %%


# %%
class MainPDS:
    def __init__(self):

        self.num_node = len(Utils.get_instance().data)
        self.num_drone = Utils.get_instance().num_drones
        self.C_d = Utils.get_instance().get_nodes_can_served_by_drone()
        self.drone_time_matrix = Utils.get_instance().cal_drone_time_matrix()
        self.truck_time_matrix = Utils.get_instance().cal_truck_time_matrix()
        self.list_label = List(self.num_node)
        self.T = Tour()
        self.T_vehicle = Tour()
        self.T_drone = Tour()
        self.T_opt_vehicle = Tour()
        self.T_opt_drone = [Tour() for i in range(self.num_node)]

    def valid_arc(self, j, i):
        for k in range(j + 1, i):
            if self.drone_time_matrix[self.T.cities[k] == 0]:
                return False
            else:
                return True

    def two_opt(self):

        route_finder = RouteFinder(self.T_opt_vehicle.cities_matrix, self.T_opt_vehicle.cities, iterations=10)

        best_distance, self.T_opt_vehicle.cities = route_finder.solve()

    def ctf(self):

        path = christofides_tsp.christofides_tsp(np.array(self.T_opt_vehicle.cities_matrix))

        real_path = [self.T_opt_vehicle.cities[i] for i in path]

        self.T_opt_vehicle.cities = real_path

    def solve_tsp(self):

        self.T_opt_vehicle.cities = self.T_vehicle.cities
        self.T_opt_vehicle.get_cities_matrix()
        self.ctf()
        self.two_opt()

    def solve_pms(self):
        pass

    def compute_drone_cost(self, j, i):
        cost = 0.0
        for k in range(j+1, i):
            cost += self.drone_time_matrix(self.T.cities(k))
        return cost

    def dynamic_programming(self):
        i = 0;
        while i < self.num_node + 1:
            i += 1
            for j in range(i):
                if self.valid_arc(j, i):
                    for l in range(len(self.list_label[j])):

                        temp = [self.list_label[j][l][0] + self.truck_time_matrix[self.T.cities[j], self.T.cities[i]],
                                self.list_label[j][l][1] + self.compute_drone_cost(j, i)]
                        self.list.addWithDominance(i, temp)

        best_label = self.list_label.find_best_label()
        best_label_index = best_label[1]

        tmp = self.list_label[self.num_node+1][best_label_index]

        i = self.num_node + 1
        j = 0

        while i >= 1:
            j = i - 1
            stop_check = False
            while not stop_check:
                if not self.list_label[j]:
                    self.T_drone.add_city(self.T.cities[j])
                    j -= 1
                else:
                    for v in range(len(self.list_label[j])):
                        if (tmp[0] == self.list_label[j][v][0] + self.drone_time_matrix[self.T.cities[j]][self.T.cities[i]]) and (tmp[1] == self.list_label[j][v][1] + self.compute_drone_cost(j, i)):
                                tmp[0] = self.list_label[j][v][0]
                                tmp[1] = self.list_label[j][v][1]
                        if j != 0:
                            self.T_vehicle.add_city(self.T.cities[j])
                        stop_check = True
                    if not stop_check:
                        self.T_drone.add_city(self.T.cities[j])
                        j -= 1
            i = j
        self.T_vehicle.cities.reverse()
        self.T_drone.cities.reverse()



def main():

    pdstsp = MainPDS()

    TSP = christofides.compute(pdstsp.truck_time_matrix)

    # path = tspsolve.nearest_neighbor(np.array(pdstsp.truck_time_matrix))
    #
    # new_path = tspsolve.two_opt(np.array(pdstsp.truck_time_matrix), path, verbose=True)
    #
    #
    # print(path)


if __name__ == "__main__":
    main()
