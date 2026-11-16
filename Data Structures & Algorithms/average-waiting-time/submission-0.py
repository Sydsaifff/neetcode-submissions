class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = customers[0][0]
        taken = []
        for i in range(len(customers)):
            time = max(customers[i][0] + customers[i][1], time + customers[i][1])
            taken.append(time - customers[i][0])

        return sum(taken)/len(customers)


        