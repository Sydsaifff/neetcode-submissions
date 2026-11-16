class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            elif i == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(i))

        return sum(stack)
                

        