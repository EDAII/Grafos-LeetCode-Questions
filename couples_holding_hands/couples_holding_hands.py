from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2 #0, 3, 1, 2
        
        graph = [[] for _ in range(n)]
        
        for i in range(0, len(row), 2):
            person1 = row[i]
            person2 = row[i + 1]
            
            couple1 = person1 // 2
            couple2 = person2 // 2
            
            if couple1 != couple2:
                graph[couple1].append(couple2)
                graph[couple2].append(couple1)
        
        visited = [False] * n
        swaps = 0
        
        def dfs(node): #busca em profundidade
            visited[node] = True
            size = 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    size += dfs(neighbor)
            return size
        
        for couple in range(n):
            if not visited[couple]:
                component_size = dfs(couple)
                swaps += component_size - 1
        
        return swaps