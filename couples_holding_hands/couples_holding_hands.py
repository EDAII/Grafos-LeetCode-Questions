from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0
        
        for i in range(0, len(row), 2):
            person = row[i]
            partner = person ^ 1
            
            if row[i + 1] != partner:
                swaps += 1
                j = pos[partner]
                row[i + 1], row[j] = row[j], row[i + 1]
                pos[row[i + 1]] = i + 1
                pos[row[j]] = j
        
        return swaps