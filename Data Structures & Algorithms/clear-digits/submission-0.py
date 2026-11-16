class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if stack and s[i].isdigit():
                stack.pop()
            else:
                stack.append(s[i])
            i += 1

        return ''.join(stack)
        
