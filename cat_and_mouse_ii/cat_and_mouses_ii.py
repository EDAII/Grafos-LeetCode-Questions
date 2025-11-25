from typing import List
from collections import deque

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        cat_pos = mouse_pos = food_pos = None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'C':
                    cat_pos = (r, c)
                elif grid[r][c] == 'M':
                    mouse_pos = (r, c)
                elif grid[r][c] == 'F':
                    food_pos = (r, c)
        
        MOUSE_TURN = 0
        CAT_TURN = 1
        MOUSE_WIN = 1
        CAT_WIN = 2
        DRAW = 0
        
        def get_neighbors(pos, max_jump, is_cat=False):
            neighbors = [pos] 
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for jump in range(1, max_jump + 1):
                    nr, nc = pos[0] + dr * jump, pos[1] + dc * jump
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        break
                    if grid[nr][nc] == '#':
                        break
                    if is_cat and (nr, nc) == food_pos:
                        break
                    neighbors.append((nr, nc))
            return neighbors
        
        result = {}
        degree = {}
        
        positions = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] != '#'] #quem é agora?
        
        for mouse in positions: #movimentos
            for cat in positions:
                for turn in [MOUSE_TURN, CAT_TURN]:
                    result[(mouse, cat, turn)] = DRAW
                    if turn == MOUSE_TURN:
                        degree[(mouse, cat, turn)] = len(get_neighbors(mouse, mouseJump))
                    else:
                        degree[(mouse, cat, turn)] = len(get_neighbors(cat, catJump, is_cat=True))
        
        queue = deque()
        
        for mouse in positions: #onde o jogo já acabou
            for cat in positions:
                for turn in [MOUSE_TURN, CAT_TURN]:
                    if mouse == food_pos:
                        result[(mouse, cat, turn)] = MOUSE_WIN
                        queue.append((mouse, cat, turn))
                    elif mouse == cat:
                        result[(mouse, cat, turn)] = CAT_WIN
                        queue.append((mouse, cat, turn))
                    elif cat == food_pos:
                        result[(mouse, cat, turn)] = CAT_WIN
                        queue.append((mouse, cat, turn))
        
        while queue:
            mouse, cat, turn = queue.popleft()
            current_result = result[(mouse, cat, turn)]
            
            if turn == MOUSE_TURN:
                prev_turn = CAT_TURN
                for prev_cat in get_neighbors(cat, catJump, is_cat=True):
                    prev_state = (mouse, prev_cat, prev_turn)
                    
                    if result[prev_state] != DRAW:
                        continue
                    
                    if current_result == CAT_WIN:
                        result[prev_state] = CAT_WIN
                        queue.append(prev_state)
                    else:
                        degree[prev_state] -= 1
                        if degree[prev_state] == 0:
                            result[prev_state] = MOUSE_WIN
                            queue.append(prev_state)
            
            else:  
                prev_turn = MOUSE_TURN
                for prev_mouse in get_neighbors(mouse, mouseJump):
                    prev_state = (prev_mouse, cat, prev_turn)
                    
                    if result[prev_state] != DRAW:
                        continue
                    
                    if current_result == MOUSE_WIN:
                        result[prev_state] = MOUSE_WIN
                        queue.append(prev_state)
                    else:
                        degree[prev_state] -= 1
                        if degree[prev_state] == 0:
                            result[prev_state] = CAT_WIN
                            queue.append(prev_state)
        
        return result[(mouse_pos, cat_pos, MOUSE_TURN)] == MOUSE_WIN