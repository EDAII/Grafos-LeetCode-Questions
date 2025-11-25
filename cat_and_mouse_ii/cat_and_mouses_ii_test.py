from cat_and_mouses_ii import Solution

class CatAndMouseIITest:
    def test_case(self, grid, cat_jump, mouse_jump, expected):
        sol = Solution()
        result = sol.canMouseWin(grid, cat_jump, mouse_jump)
        print(f"Grid:")
        for row in grid:
            print(f"  {row}")
        print(f"Cat Jump: {cat_jump}, Mouse Jump: {mouse_jump}")
        print(f"Esperado: {expected}")
        print(f"Resultado: {result}")
        print(f"Status: {'PASSOU' if result == expected else 'FALHOU'}")
        print("\n")
        
def main():
    test = CatAndMouseIITest()
    
    test.test_case(["####F", "#C...", "M...."], 1, 2, True)
    
    test.test_case(["M.C...F"], 1, 4, True)
    
    test.test_case(["M.C...F"], 1, 3, False)
    
    test.test_case(["C...#", "...#F", "....#", "M...."], 2, 5, False)
    
    test.test_case([".M...", "..#..", "#..#.", "C#.#.", "...#F"], 1, 2, True)

if __name__ == "__main__":
    main()