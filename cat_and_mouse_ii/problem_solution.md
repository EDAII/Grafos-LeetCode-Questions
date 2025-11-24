# Cat and Mouse II

## O problema

Um gato e um rato jogam em um tabuleiro que contém paredes, espaços vazios e comida. O rato move primeiro e eles alternam turnos. Cada um pode pular até uma distância máxima nas quatro direções. O rato vence se alcançar a comida primeiro, enquanto o gato vence se capturar o rato, chegar na comida antes, ou se o jogo ultrapassar 1000 movimentos. A questão é determinar se o rato consegue vencer quando ambos jogam de forma ótima.

Exemplo 1:
![Exemplo 1](/cat_and_mouse_ii/exemplo_1.png)

Exemplo: 2:
![Exemplo 2](/cat_and_mouse_ii/exemplo_2.png)


## A resolução

Usei minimax para simular todas as possibilidades do jogo. O rato tenta maximizar suas chances de vitória enquanto o gato tenta minimizá-las. Cada estado do jogo armazena a posição do rato, posição do gato, de quem é o turno e quantos movimentos já ocorreram. Para evitar recalcular os mesmos estados, implementei memorização com um dicionário. As condições de término incluem: rato alcança comida, gato alcança comida, gato captura rato, ou limite de 1000 movimentos excedido.

## Capturas de tela
colocar

## Conclusões

O minimax com memorização é adequado para este problema de teoria dos jogos. A complexidade pode ser alta, mas a memorização reduz significativamente os cálculos repetidos. O limite de 1000 movimentos previne loops infinitos. A solução funciona bem para grades pequenas como especificado nas restrições, embora possa ser lenta em casos mais complexos. É uma técnica aplicável a outros problemas de jogos adversariais.