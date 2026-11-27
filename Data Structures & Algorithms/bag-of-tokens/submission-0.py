class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = 0
        score = 0
        tokens.sort()
        i,j = 0 , len(tokens) - 1

        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break

        return res

        
