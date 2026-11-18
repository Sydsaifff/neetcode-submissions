class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        pivot_num = []
        greater = []

        for i in nums:
            if i < pivot:
                lesser.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                pivot_num.append(i)
        
        return lesser + pivot_num + greater
