class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt_1 = 0
        cnt_0 = 0
        res = 0
        diff_index = {}

        for i , n in enumerate(nums):
            if n == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1
            
            if cnt_1 - cnt_0 not in diff_index:
                diff_index[cnt_1 - cnt_0] = i
            
            if cnt_1 == cnt_0:
                res = cnt_1 + cnt_0
            else:
                index = diff_index[cnt_1 - cnt_0]
                res = max(res, i - index)

        return res
            

