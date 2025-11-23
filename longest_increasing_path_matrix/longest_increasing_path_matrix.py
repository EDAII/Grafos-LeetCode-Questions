from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        # Inicializa a tabela de memoização com 0
        # memo[i][j] armazenará o comprimento do maior caminho a partir de (i, j)
        memo = [[0] * n for _ in range(m)]
        
        # Direções: Cima, Baixo, Esquerda, Direita
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(row, col):
            # Se já calculamos esse valor, retorne-o (Cache)
            if memo[row][col] != 0:
                return memo[row][col]
            
            max_path = 1 # O caminho mínimo é a própria célula (1)
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Verifica limites e se o valor vizinho é maior (estritamente crescente)
                if (0 <= new_row < m and 
                    0 <= new_col < n and 
                    matrix[new_row][new_col] > matrix[row][col]):
                    
                    # Chama a recursão
                    length = 1 + dfs(new_row, new_col)
                    max_path = max(max_path, length)
            
            # Salva no cache antes de retornar
            memo[row][col] = max_path
            return max_path

        # Itera sobre todas as células para garantir que encontramos o maior caminho global
        # Utiliza uma compreensão de lista dentro do max() para ser mais "Pythonico"
        return max(dfs(i, j) for i in range(m) for j in range(n))