class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_digit = len(str(low))
        high_digit = len(str(high))
        res = []

        for i in range(low_digit, high_digit + 1):
            for current in range(1, 9):
                if current + i > 10:
                    break
                num = current
                prev = current
                for j in range(i - 1):
                    num = num * 10
                    prev += 1
                    num += prev
                if low <= num <= high:
                    res.append(num)

        return res
        