
class Tour():
    cities = []

    def __init__(self):
        self.cities = None

    def add_city(self, city):
        self.cities.append(city)

    def length(self):
        return len(self.cities)

    def cost(self, truck_time_matrix):
        sum = 0
        for i in range(1, len(self.cities)):
            sum += truck_time_matrix[self.cities[i - 1]][self.cities[i]]
        return sum
