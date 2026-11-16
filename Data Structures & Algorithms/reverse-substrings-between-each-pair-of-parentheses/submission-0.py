class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ')':
                stack.append(s[i])
            else:
                substring = ''
                while stack and stack[-1] != '(':
                    substring += stack.pop()
                stack.pop()
                stack.extend(substring)
        
        return ''.join(stack)
                    
                    
            


