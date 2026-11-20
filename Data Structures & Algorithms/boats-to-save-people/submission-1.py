class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        res = 0
        while i <= j:
            if i == j and people[i] <= limit:
                res += 1
                j -= 1
            elif people[i] + people[j] == limit:
                res += 1
                i += 1
                j -= 1
            elif people[i] + people[j] > limit:
                res += 1
                j -= 1
            else:
                res += 1
                i += 1
                j -= 1
        
        return res
            
                
            
                
        
        