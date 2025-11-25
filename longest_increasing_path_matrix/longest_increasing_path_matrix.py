from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        
        # Direções: Cima, Baixo, Esquerda, Direita
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(row, col):
            if memo[row][col] != 0:
                return memo[row][col]
            
            max_path = 1 
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < m and 
                    0 <= new_col < n and 
                    matrix[new_row][new_col] > matrix[row][col]):
                    
                    length = 1 + dfs(new_row, new_col)
                    max_path = max(max_path, length)
            
            memo[row][col] = max_path
            return max_path

        return max(dfs(i, j) for i in range(m) for j in range(n))