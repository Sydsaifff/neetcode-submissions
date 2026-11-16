class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ''
        hash_map = Counter(s)
        for i in order:
            if hash_map[i] != 0:
                for j in range(hash_map[i]):
                    res += i
                    s = s.replace(i, '')

                    


          
        return res + s





            

        
        