class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_number = []
        hashmap = defaultdict(int)
        for i in arr:
            hashmap[i] += 1
        for i in hashmap:
            if i == hashmap[i]:
                lucky_number.append(i)

        if lucky_number == []:
            return -1
        else:
            return max(lucky_number)
        

        