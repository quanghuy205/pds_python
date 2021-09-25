

class List:

    def __init__(self, num_node):
        self.list = [[] for i in range(num_node + 2)]

    def addWithDominance(self, index, label):
        is_discard = False

        for i in range(len(self.list[index])):
            if self.dominance(label, self.list[i] == 0):
                self.list.remove(i)
            elif self.dominance(label, self.list[i] == 1):
                is_discard = True

        if not is_discard:
            self.list[index].append(label)

    def dominance(self, label1, label2):
        if (label1[0] < label2[0] and label1[1] <= label2[1]) or (label1[0] <= label2[0] and label1[1] < label2[1]):
            return 0
        elif (label1[0] > label2[0] and label1[1] >= label2[1]) or (label1[0] >= label2[0] and label1[1] > label2[1]):
            return 1
        else:
            return 2



