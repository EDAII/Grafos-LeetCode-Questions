from couples_holding_hands import Solution

class CouplesHoldingHandsTest:
    def test_case(self, row, expected):
        sol = Solution()
        result = sol.minSwapsCouples(row)
        print(f"Row: {row}")
        print(f"Esperado: {expected}")
        print(f"Resultado: {result}")
        print(f"Status: {'PASSOU' if result == expected else 'FALHOU'}")
        print("\n")
        
def main():
    test = CouplesHoldingHandsTest()
    
    test.test_case([0, 2, 1, 3], 1)
    
    test.test_case([3, 2, 0, 1], 0)
    
    test.test_case([0, 1], 0)
    
    test.test_case([1, 0], 0)
    
    test.test_case([0, 2, 4, 6, 1, 3, 5, 7], 2)
    
    test.test_case([5, 4, 2, 6, 3, 1, 0, 7], 2)

if __name__ == "__main__":
    main()