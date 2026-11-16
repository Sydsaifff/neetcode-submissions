class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        final_array = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                else:
                    if words[i] in words[j]:
                        final_array.append(words[i])
                        break

        return final_array

            
        




            



        