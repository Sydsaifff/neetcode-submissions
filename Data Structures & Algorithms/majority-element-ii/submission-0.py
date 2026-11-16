class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)
        for i in nums:
            cnt[i] += 1
            if len(cnt) <= 2:
                continue
            new_count = defaultdict(int)

            for i, j in cnt.items():
                if j > 1:
                    new_count[i] = j - 1
            cnt = new_count

        res = []
        for n in cnt:
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res




            


        