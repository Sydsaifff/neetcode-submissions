from collections import defaultdict, Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter_2 = defaultdict(int)
        res = []

        for i in words2:
            count_of_words = Counter(i)
            for j, cnt in count_of_words.items():
                counter_2[j] = max(counter_2[j], cnt)

        for i in words1:
            count_of_words = Counter(i)
            flag = True
            for j, cnt in counter_2.items():
                if count_of_words[j] < cnt:
                    flag = False
                    break
            if flag == True:
                res.append(i)

        return res
