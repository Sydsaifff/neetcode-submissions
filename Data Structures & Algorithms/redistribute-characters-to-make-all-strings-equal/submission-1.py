class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        word = "".join(words)
        hashmap = Counter(word)
        for i in hashmap:
            if hashmap[i] % len(words) != 0:
                return False
        return True
        


