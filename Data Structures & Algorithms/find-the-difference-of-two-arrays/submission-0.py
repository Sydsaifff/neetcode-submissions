class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        distinct1 = set(nums1)
        distinct2 = set(nums2)
        res1 = []
        res2 = []

        for i in distinct1:
            if i not in distinct2:
                res1.append(i)

        for i in distinct2:
            if i not in distinct1:
                res2.append(i)

        return [res1, res2]

        