class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = ''
        temp = 0

        for i , j in count.most_common():
            for a in range(j):
                res += i

        return res


        