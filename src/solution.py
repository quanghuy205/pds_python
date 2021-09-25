from tour import Tour


class Solution:
    def __init__(self):
        self.VehicleTour = Tour()
        self.DroneTour = [Tour()]

    def isBetterSolution(self, solutionB):

        CostOfA = max(self.VehicleCost(), self.DroneCost())

        CostOfB = max(solutionB.VehicleCost(), solutionB.DroneCost())

        if ((CostOfA < CostOfB) or ((CostOfA == CostOfB) and (
                min(self.VehicleCost(), self.DroneCost()) < min(solutionB.VehicleCost(), solutionB.DroneCost())))):
            return True
        else:
            return False

    def vehicle_cost(self):
        return self.VehicleTour.tour_vehicle_cost()

    def drone_cost(self):
        drone_cost_list = []
        size = len(self.DroneTour)
        if size == 0:
            return 0.0
        for i in range(size):
            drone_cost_list.append(self.DroneTour[i].tour_drone_cost())

        return max(drone_cost_list)

    def cost(self):
        return max(self.vehicle_cost(), self.drone_cost())

    def reset(self):
        self.VehicleTour.reset()
        for i in range(len(self.DroneTour)):
            self.DroneTour[i].reset()
