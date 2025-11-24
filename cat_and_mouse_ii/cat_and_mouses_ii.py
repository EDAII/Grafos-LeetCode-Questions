from typing import List

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
        
        MOUSE_WIN = 1
        CAT_WIN = 2
        DRAW = 0
        MAX_MOVES = 1000
        
        memo = {}
        
        def get_moves(pos, max_jump):
            moves = [pos]
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for jump in range(1, max_jump + 1):
                    nr, nc = pos[0] + dr * jump, pos[1] + dc * jump
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                        moves.append((nr, nc))
                    else:
                        break
            return moves
        
        def minimax(mouse, cat, turn, moves):
            if moves > MAX_MOVES:
                return CAT_WIN
            
            if mouse == food_pos:
                return MOUSE_WIN
            
            if cat == food_pos or mouse == cat:
                return CAT_WIN
            
            if (mouse, cat, turn, moves) in memo:
                return memo[(mouse, cat, turn, moves)]
            
            if turn == 0:
                mouse_wins = False
                for next_mouse in get_moves(mouse, mouseJump):
                    result = minimax(next_mouse, cat, 1, moves + 1)
                    if result == MOUSE_WIN:
                        mouse_wins = True
                        break
                memo[(mouse, cat, turn, moves)] = MOUSE_WIN if mouse_wins else CAT_WIN
            else:
                cat_wins = False
                for next_cat in get_moves(cat, catJump):
                    if next_cat == food_pos:
                        cat_wins = True
                        break
                    result = minimax(mouse, next_cat, 0, moves + 1)
                    if result == CAT_WIN:
                        cat_wins = True
                        break
                memo[(mouse, cat, turn, moves)] = CAT_WIN if cat_wins else MOUSE_WIN
            
            return memo[(mouse, cat, turn, moves)]
        
        result = minimax(mouse_pos, cat_pos, 0, 0)
        return result == MOUSE_WIN