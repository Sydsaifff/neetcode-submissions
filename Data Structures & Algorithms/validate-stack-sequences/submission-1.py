class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped.reverse()
        i = 0
        while i < len(pushed):
            stack.append(pushed[i])
            i += 1
            while stack and popped and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()

        if not stack:
            return True
        return False



