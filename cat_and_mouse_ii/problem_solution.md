# Cat and Mouse II

## O problema

Um gato e um rato jogam em um tabuleiro que contém paredes, espaços vazios e comida. O rato move primeiro e eles alternam turnos. Cada um pode pular até uma distância máxima nas quatro direções. O rato vence se alcançar a comida primeiro, enquanto o gato vence se capturar o rato ou chegar na comida antes. O gato também vence se o jogo resultar em empate (ciclos infinitos). A questão é determinar se o rato consegue vencer quando ambos jogam de forma ótima.

Exemplo 1:
![Exemplo 1](/cat_and_mouse_ii/exemplo_1.png)

Exemplo 2:
![Exemplo 2](/cat_and_mouse_ii/exemplo_2.png)

## A resolução

Implementei uma solução usando **programação dinâmica com BFS (Breadth-First Search) bottom-up**, baseada em teoria dos jogos em grafos. A abordagem trata o problema como um grafo de estados onde cada nó representa uma configuração `(posição_rato, posição_gato, turno)`.

### Estratégia

1. **Estados terminais**: Identifico primeiro todos os casos base onde o resultado é óbvio (rato alcança comida = vitória do rato; gato captura rato ou alcança comida = vitória do gato)

2. **Grau de entrada**: Para cada estado, calculo quantos movimentos possíveis cada jogador tem. Isso permite determinar quando todas as opções de um jogador levam à derrota

3. **BFS reverso**: Começo dos estados terminais e propago os resultados para trás. Se um jogador encontra um movimento que leva à sua vitória, ele escolhe esse movimento. Se todos os movimentos levam à derrota (grau de entrada chega a zero), o estado atual também resulta em derrota

4. **Regra especial**: O gato não pode pisar na posição da comida (apenas capturar o rato antes que ele chegue lá)

Esta abordagem detecta empates matematicamente através do grau de entrada: estados que permanecem indeterminados após o BFS são empates reais. Cada estado é processado exatamente uma vez, garantindo eficiência.

## Capturas de tela
![imagem](/cat_and_mouse_ii/image.png)

## Conclusões

A solução com BFS bottom-up é boa para problemas de teoria dos jogos em grafos. A complexidade é O(rows² × cols² × max_jump), mas cada estado é processado apenas uma vez, sem recursão ou limites artificiais. O algoritmo detecta empates corretamente através do grau de entrada, eliminando a necessidade de contadores arbitrários de movimento. Esta técnica é aplicável a qualquer jogo adversarial com informação perfeita em grafos finitos, sendo especialmente eficiente quando o espaço de estados é limitado, como nas restrições do problema (grid até 8×8).

## Referências

> LeetCode. Cat and Mouse II - Solution. LeetCode Discuss. Disponível em: https://leetcode.com/problems/cat-and-mouse-ii/solutions/
> GeeksforGeeks. Game Theory in Competitive Programming. GeeksforGeeks. Disponível em: https://www.geeksforgeeks.org/game-theory-competitive-programming/