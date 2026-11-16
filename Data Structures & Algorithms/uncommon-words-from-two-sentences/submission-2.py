class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sentence = s1.split() + s2.split()
        unique = set()
        repeated = set()
        for i in sentence:
            if i in repeated:
                continue
            if i in unique:
                unique.remove(i)
                repeated.add(i)
            else:
                unique.add(i)

        return list(unique)
