class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        total_odd = 0
        total_even = 0
        cur_sum = 0
        res = 0
        for i in arr:
            cur_sum += i
            if cur_sum % 2 != 0:
                total_odd += 1
                res += 1
                res += total_even
            else:
                total_even += 1
                res += total_odd

        return res

        


            