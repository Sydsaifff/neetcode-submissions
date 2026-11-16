class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        i = 0
        map_hnd = {}
        res = []

        while i < len(positions):
            map_hnd[positions[i]] = [healths[i], directions[i]]
            i += 1
        i = 0
        sorted_pos = sorted(positions)
        while i < len(sorted_pos):
            if map_hnd[sorted_pos[i]][1] == 'R' or not stack:
                stack.append(sorted_pos[i])
                i += 1
            else:
                while stack and i < len(sorted_pos) and map_hnd[sorted_pos[i]][1] == 'L':
                    if map_hnd[stack[-1]][1] == 'R':
                        if map_hnd[stack[-1]][0] > map_hnd[sorted_pos[i]][0]:
                            i += 1
                            map_hnd[stack[-1]][0] -= 1
                        elif map_hnd[stack[-1]][0] < map_hnd[sorted_pos[i]][0]:
                            stack.pop()
                            map_hnd[sorted_pos[i]][0] -= 1
                        else:
                            stack.pop()
                            i += 1
                    else:
                        stack.append(sorted_pos[i])
                        i += 1

        alive = set(stack)

        for p in positions:  
            if p in alive:
                res.append(map_hnd[p][0])

        return res

        


                    
