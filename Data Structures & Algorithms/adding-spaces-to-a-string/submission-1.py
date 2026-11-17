class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modify = list(s)
        for i in spaces:
            modify[i] = ' ' + modify[i]

        return ''. join(modify)
        