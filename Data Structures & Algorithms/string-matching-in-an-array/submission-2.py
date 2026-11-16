class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        final_array = []
        sorted_words = sorted(words, key=len)

        for word in sorted_words:
            if sorted_words.index(word) == len(sorted_words) - 1:
                return final_array
            else:
                for i in range(sorted_words.index(word) + 1 , len(sorted_words)):
                    if word in sorted_words[i] and word not in final_array:
                        final_array.append(word)
            
        




            



        