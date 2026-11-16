class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()

        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            if sequence in seen:
                res.add(sequence)
            seen.add(sequence)
        
        return list(res)
