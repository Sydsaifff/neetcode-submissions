class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        compute = 0
        while i < len(asteroids):
            stack.append(asteroids[i])
            i += 1
            while i < len(asteroids) and stack and asteroids[i] < 0 and stack[-1] > 0:
                compute = stack[-1] + asteroids[i]
                if compute > 0:
                    i += 1
                elif compute < 0:
                    stack.pop()
                else:
                    stack.pop()
                    i += 1

        return stack

                

