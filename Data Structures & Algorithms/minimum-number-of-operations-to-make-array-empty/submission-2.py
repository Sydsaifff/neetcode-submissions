class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for j in count.values():
            if j == 1:
                return -1
            elif j % 3 == 0:
                res += j / 3
            else:
                if (j % 3) % 2 == 0:
                    res += j // 3
                    res += 1
                else:
                    res += j // 3 - 1
                    res += 2
        
        return int(res)

                
            

        