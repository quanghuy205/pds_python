from utils import Utils

class Tour():

    def __init__(self):
        self.cities = None
        self.truck_time_matrix = Utils.get_instance().cal_truck_time_matrix()
        self.drone_time_matrix = Utils.get_instance().cal_drone_time_matrix()

    def add_city(self, city):
        self.cities.append(city)

    def length(self):
        return len(self.cities)

    def cost(self):
        sum = 0
        for i in range(1, len(self.cities)):
            sum += truck_time_matrix[self.cities[i - 1]][self.cities[i]]
        return sum
