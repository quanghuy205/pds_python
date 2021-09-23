import numpy as np
from utils import Utils
from ortools.linear_solver import pywraplp
from tour import Tour
from list import List
import tspsolve


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
        self.T_op_drone = [Tour() for i in range(self.num_node)]

    def valid_arc(self, j, i):
        for k in range(j + 1, i):
            if self.drone_time_matrix[self.T.cities[k] == 0]:
                return False
            else:
                return True

    def solve_tsp(self):
        pass

    def solve_pms(self):
        pass

    def compute_drone_cost(self, j, i):
        cost = 0.0
        for k in range(j+1, i):
            cost += self.drone_time_matrix(self.T.cities(k))

    def dynamic_programming(self):

        i = 0;
        while i < self.num_node + 1:
            i += 1
            for j in range(i):
                if self.valid_arc(j, i):
                    for l in range(len(self.list_label[j])):
                        temp = [self.list_label[j][l][0] + self.truck_time_matrix[self.T.cities[j], self.T.cities[j]],
                                self.list_label[j][l][1] + self.compute_drone_cost(j, i)]

                        self.list.addWithDominance(i, temp)


def main():

    pdstsp = MainPDS()
    
    path = tspsolve.nearest_neighbor(np.array(pdstsp.truck_time_matrix))
    new_path = tspsolve.two_opt(np.array(pdstsp.truck_time_matrix), path, verbose=True)


    print(path)
    print(new_path)

if __name__ == "__main__":
    main()
