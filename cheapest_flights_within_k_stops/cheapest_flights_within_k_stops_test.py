from cheapest_flights_within_k_stops import Solution

class CheapestFlightsWithinKStopsTest:
    def test_case(self, n, flights, src, dst, k, expected):
        sol = Solution()
        result = sol.findCheapestPrice(n, flights, src, dst, k)
        print(f"Numero de cidades: {n}, voos: {flights}, de: {src}, para: {dst}, numero de paradas máximas: {k}")
        print(f"Esperado: {expected}")
        print(f"Resultado: {result}")
        print("\n")
        
def main():
    test = CheapestFlightsWithinKStopsTest()
    
    # Teste 1
    n1 = 3
    flights1 = [[0,1,100],[1,2,100],[0,2,500]]
    src1 = 0
    dst1 = 2
    k1 = 1
    expected1 = 200
    test.test_case(n1, flights1, src1, dst1, k1, expected1)
    
    # Teste 2
    n2 = 4
    flights2 = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src2 = 0
    dst2 = 3
    k2 = 1
    expected2 = 700
    test.test_case(n2, flights2, src2, dst2, k2, expected2)
    
    # Teste 3
    n3 = 3
    flights3 = [[0,1,100],[1,2,100],[0,2,500]]
    src3 = 0
    dst3 = 2
    k3 = 0
    expected3 = 500
    test.test_case(n3, flights3, src3, dst3, k3, expected3)
    
    # Teste 4
    n4 = 3
    flights4 = [[0,1,100],[1,2,100],[0,2,500]]
    src4 = 0
    dst4 = 2
    k4 = 1
    expected4 = 200
    test.test_case(n4, flights4, src4, dst4, k4, expected4)
    
if __name__ == "__main__":
    main()