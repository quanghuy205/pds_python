from tour import Tour




class Solution:
    def __init__(self):
        self.VehicleTour = Tour()
        self.DroneTour = [Tour()]


    def isBetterSolution(self, solutionB):

        CostOfA = max(self.VehicleCost(), self.DroneCost())

        CostOfB = max(solutionB.VehicleCost(), solutionB.DroneCost())

        if ((CostOfA < CostOfB) or ((CostOfA == CostOfB) and (
                min(self.VehicleCost(), self.DroneCost()) < min(solutionB.VehicleCost(), solutionB.DroneCost()))))
                    return True;
                 else
                     return False;
    def VehicleCost(self):
        return self.VehicleTour.cost()
