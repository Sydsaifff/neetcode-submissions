class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        res = [0] * len(nums)        

        for x in range(len(nums) - 1, - 1 , -1):
            if abs(nums[i]) > nums[j]:
                res[x] = nums[i] ** 2
                i += 1
            else:
                res[x] = nums[j] ** 2
                j -= 1
                
        return res