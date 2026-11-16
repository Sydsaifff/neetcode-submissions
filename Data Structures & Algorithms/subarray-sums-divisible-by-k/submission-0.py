class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        current_sum = 0 
        res = 0 
        prefix_sum = {0 : 1}

        for i in nums:
            current_sum += i
            remainder = current_sum % k
            res += prefix_sum.get(remainder, 0)
            prefix_sum[remainder] = 1 + prefix_sum.get(remainder, 0)

        return res
            



        