# Couples Holding Hands

## O problema

Temos vários casais sentados em uma fileira de cadeiras, mas estão todos misturados. Cada casal é numerado como (0,1), (2,3), (4,5) e assim por diante. O objetivo é descobrir o número mínimo de trocas necessárias para que todos os casais fiquem sentados lado a lado.

## A resolução

A solução passa pelos assentos de dois em dois. Para cada par de assentos, verifico se a primeira pessoa está sentada ao lado do seu parceiro. Se não estiver, localizo onde está o parceiro correto e faço a troca. Para encontrar o parceiro de alguém, uso a operação XOR (`person ^ 1`) que funciona bem: se o número é par vira ímpar e vice-versa. Também mantenho um dicionário com as posições de cada pessoa, facilitando a busca pelo parceiro que precisa trocar de lugar.

## Capturas de tela
exemplo

## Conclusões

Essa abordagem funciona porque cada troca sempre deixa pelo menos um casal junto, sem desfazer o que já foi arrumado. O algoritmo percorre o array uma única vez, sendo bastante eficiente. É uma solução direta que aproveita bem a propriedade matemática dos pares, e o truque do XOR simplifica bastante o código.