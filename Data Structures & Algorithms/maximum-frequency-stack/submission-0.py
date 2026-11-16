class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.max_cnt = 0
        self.stacks = {}
    def push(self, val: int) -> None:
        valcnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valcnt
        if valcnt > self.max_cnt:
            self.max_cnt = valcnt
            self.stacks[valcnt] = []
        self.stacks[valcnt].append(val)
    def pop(self) -> int:
        res = self.stacks[self.max_cnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.max_cnt]:
            self.max_cnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()