class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = []
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                res.append(num[i])
        
        if res == []:
            return ''
        else:
            return str(max(res)) * 3

 

