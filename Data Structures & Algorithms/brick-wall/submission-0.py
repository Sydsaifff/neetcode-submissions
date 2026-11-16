class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        count_gap = defaultdict(int)
        rows = len(wall)
        total_width = sum(wall[0])

        for i in wall:
            width = 0
            for j in i:
                width += j
                if width < total_width:
                    count_gap[width] += 1
                else: 
                    count_gap[width] = 0
        
        return rows - max(count_gap.values())

        