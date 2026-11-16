class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_sequence = 0

        for i in numSet:
            if i - 1 not in numSet:
                sequence = 0
                while (i + sequence) in numSet:
                    sequence += 1
                if sequence > max_sequence:
                    max_sequence = sequence

        return max_sequence
            
                
                    
                


        