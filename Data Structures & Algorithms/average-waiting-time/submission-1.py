class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = customers[0][0]
        taken = 0
        for i in range(len(customers)):
            time = max(customers[i][0] + customers[i][1], time + customers[i][1])
            taken += (time - customers[i][0])

        return taken/len(customers)


        