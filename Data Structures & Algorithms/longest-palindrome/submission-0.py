class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = set()
        res = 0

        for i in s:
            if i in count:
                count.remove(i)
                res +=2
            else:
                count.add(i)

        
        if count:
            return res + 1
        else:
            return res
        
        
        