class Solution:
    def calculate(self, s: str) -> int:

        clean_text = s.replace(" ", "")
        stack = []
        i = 0

        def read_num(i):
            num = 0
            while i < len(clean_text) and clean_text[i].isdigit():
                num = num * 10 + int(clean_text[i])
                i += 1
            return num, i

        num, i = read_num(i)
        stack.append(num)

        
        while i < len(clean_text):
            op = clean_text[i]
            i += 1
            num, i = read_num(i)

            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            else:  
                stack.append(int(stack.pop() / num))

        return sum(stack)
            

        