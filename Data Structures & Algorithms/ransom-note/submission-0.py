class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        cnt = Counter(magazine)
        res = ''
        for i in ransomNote:
            if i in cnt and cnt[i] != 0:
                cnt[i] -= 1
                res += i
        
        if ransomNote == res:
            return True
        else: 
            return False

            

        