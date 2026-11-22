class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        j = i + 1
        res = 0
        
        while i < len(colors) and j < len(colors):
            if colors[i] == colors[j]:
                if neededTime[i] < neededTime[j]:
                    res += neededTime[i]
                    i = j
                else:
                    res += neededTime[j]
                j += 1
            else:
                i = j
                j += 1

        return res
                
                    
                    