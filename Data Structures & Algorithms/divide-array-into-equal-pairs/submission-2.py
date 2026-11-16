class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pairs = defaultdict(int)
        for i in nums:
            pairs[i] += 1
        
        for i in pairs:
            if pairs[i] % 2 == 0:
                continue
            else:
                return False
        
        return True


        

            