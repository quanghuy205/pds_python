from utils import Utils

class Tour():

    def __init__(self):
        self.cities = []
        self.truck_time_matrix = Utils.get_instance().cal_truck_time_matrix()
        self.drone_time_matrix = Utils.get_instance().cal_drone_time_matrix()
        self.cities_matrix = [[]]

    def add_city(self, city):
        self.cities.append(city)

    def get_cities_matrix(self):
        self.cities_matrix = [[self.truck_time_matrix[self.cities[i]][self.cities[j]]
                               for i in range(len(self.cities))] for j in range(len(self.cities))]

    def length(self):
        return len(self.cities)

    def tour_vehicle_cost(self):
        cost = 0.0
        num_cities = len(self.cities)
        for i in range(1, num_cities):
            cost += self.truck_time_matrix[self.cities[i - 1]][self.cities[i]]
        cost += self.truck_time_matrix[self.cities[num_cities-1][0]]
        return cost

    def tour_drone_cost(self):
        cost = 0.0
        num_cities = len(self.cities)
        for i in range(num_cities):
            cost += self.drone_time_matrix[self.cities[i]]
        return cost

    def reset(self):
        self.cities.clear()
