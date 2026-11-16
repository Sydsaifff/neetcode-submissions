class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        from collections import defaultdict
        res = 0
        wordMap = defaultdict(set)
        for i in ideas:
            wordMap[i[0]].add(i[1:])
        
        for char1 in wordMap:
            for char2 in wordMap:
                if char1 == char2:
                    continue
                duplicates = 0
                for i in wordMap[char1]:
                    if i in wordMap[char2]:
                        duplicates += 1
                
                distinct1 = len(wordMap[char1]) - duplicates
                distinct2 = len(wordMap[char2]) - duplicates
            
                res += distinct1 * distinct2

        return res
