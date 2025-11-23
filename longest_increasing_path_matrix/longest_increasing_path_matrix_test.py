from longest_increasing_path_matrix import Solution

class LongestIncreasingPathMatrixTest:
    def test_case(self, matrix, expected):
        sol = Solution()
        result = sol.longestIncreasingPath(matrix)
        print(f"Matrix: {matrix}")
        print(f"Experado: {expected}")
        print(f"Resultado: {result}")
        print("\n")
        
def main():
    test = LongestIncreasingPathMatrixTest()
    
    # Teste 1
    matrix1 = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    expected1 = 4
    test.test_case(matrix1, expected1)
    
    # Teste 2
    matrix2 = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    expected2 = 4
    test.test_case(matrix2, expected2)
    
    # Teste 3
    matrix3 = [
        [1]
    ]
    expected3 = 1
    test.test_case(matrix3, expected3)
    
    # Teste 4: Matriz vazia
    matrix4 = []
    expected4 = 0
    test.test_case(matrix4, expected4)
    
    # Teste 5: Matriz com todos os mesmos valores
    matrix5 = [
        [7, 7, 7],
        [7, 7, 7],
        [7, 7, 7]
    ]
    expected5 = 1
    test.test_case(matrix5, expected5)
    
if __name__ == "__main__":
    main()