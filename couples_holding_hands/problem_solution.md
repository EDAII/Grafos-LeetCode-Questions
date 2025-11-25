# Couples Holding Hands

## O problema

Temos vários casais sentados em uma fileira de cadeiras, mas estão todos misturados. Cada casal é numerado como (0,1), (2,3), (4,5) e assim por diante. O objetivo é descobrir o número mínimo de trocas necessárias para que todos os casais fiquem sentados lado a lado.

## A resolução

A solução modela o problema usando grafos. Cada **casal** é um nó no grafo, e se dois casais diferentes estão entrelaçados no mesmo sofá (uma pessoa de cada casal), criamos uma aresta entre eles. Para descobrir a qual casal cada pessoa pertence, uso divisão inteira (`person // 2`): as pessoas 0 e 1 pertencem ao casal 0, as pessoas 2 e 3 ao casal 1, e assim por diante.

Depois de construir o grafo, uso DFS (busca em profundidade) para encontrar todos os componentes conexos. A chave é que cada componente conexo de tamanho k precisa de exatamente k-1 trocas para ser resolvido. Somo todas essas quantidades e obtenho o resultado final.

## Capturas de tela
![imagem](/couples_holding_hands/image.png)

## Conclusões

Casais entrelaçados formam ciclos que precisam ser "quebrados". Cada componente conexo representa um grupo de casais que estão misturados entre si, e a fórmula k-1 vem da teoria de grafos.