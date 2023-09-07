# Lista 3 - Alan Demétrius 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 

> Algoritmos Gulosos e Programação Dinâmica

### 2° - Questão
Um teste de mesa para o problema do troco com moedas de {1,5,7} centavos para 
um troco de 10 utilizando algoritmos gulosos e programação dinâmica

###### Abordagem Algoritmos Gulosos:
- Ordenamos nossas moedas em ordem decrescente ficamos com  {7, 5, 1}
- Entramos em um loop iterando as moedas
- Para cada moeda fazemos a divisão inteira e guardamos no nosso total
- O novo valor total vai ser o resto da divisão que será iterado com as outras 
moedas.

Moedas = {1:0, 5:0, 7:0}
total = 10
- Primeira iteração:
10 // 7 = 1
10 % 7 = 3
Moedas = {1:0, 5:0, 7:1}

- Segunda iteração:
3 // 5 = 0
3 % 5 = 3
Moedas = {1:0, 5:0, 7:1}

- Terceira iteração:
3 // 1 = 3
3 % 1 = 0
Moedas = {1:3, 5:0, 7:1}

- Como nosso total de moedas chegou a zero temos a nossa resposta final.

###### Abordagem Programação Dinâmica:

- Iniciamos com a primeira moeda que dos foi dada $1$
- Podemos pegar ate 10 moedas de 1 real, e devemos guardar todos esses valores
em uma hash table para auxilar na memorização

|0|1|2|3|4|5|6|7|8|9|10|
|-|-|-|-|-|-|-|-|-|-|-|
|0|1|2|3|4|5|6|7|8|9|10|

- Mesmo procedimento para a moeda de 5

|0|1|2|3|4|5|6|7|8|9|10|
|-|-|-|-|-|-|-|-|-|-|-|
|0|1|2|3|4|1|2|3|4|5|2|

- Ocorre a mudança do troco para 5, onde so a necessidade de usar 1 moeda e dai
em diante usa-se a moeda de um. Na etapa final usa-se duas moedas de 5

- Por ultimo o procedimento para o troco de 7

|0|1|2|3|4|5|6|7|8|9|10|
|-|-|-|-|-|-|-|-|-|-|-|
|0|1|2|3|4|1|2|1|2|3|2|

- Ocorre uma diminuição da quantidade de moedas para o troco de 7 para cima, com
exceção do troco para 10, que a forma mais otimizada sao apenas duas moedas de 5.

### 5° Questão
Dado um conjunto de atividades, juntamente com o tempo de início e término de 
cada atividade, encontre o número máximo de atividades realizadas por uma única 
pessoa, assumindo que uma pessoa pode trabalhar apenas em uma atividade por vez.**

- input: número de atividades, atividade, periodo dessa atividade:
- output: O numero inteiro de esportes que ele é capaz de fazer
Ex: 
    6
    15 18
    14 15
    16 17
    14 16
    18 19
    16 18
    output : 3
```py
def atv_max(atv):
    atv.sort(key=lambda x: x[1])
    finalizado = 0
    total = 0
    for i in range(len(atv)):
        ini, fim = atv[i]
        if ini >= finalizado:
            total += 1
            finalizado = fim
    return total

def main():
    total = int(input())
    atv = [0]*total
    for i in range(total):
        atv[i] = tuple(map(int, input().split()))

    return atv_max(atv)
```
### 7° Questão 
Construir uma função recursiva com programação dinâmica para resolver a sequência 
de fibonacci de um termo i, e fazer o teste de mesa dessa função para o valor i = 5.
```py
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)
```

- teste de mesa para n igual a 5

- O codigo chamara recursivamente a funçao para n = 4 e n = 3, que por sua vez
n = 2 e n = 1
- fib(2) = fib(1) + fib(0)
- fib(2) = 1 + 1
- fib(2) = 2
- Agora somos capazes de calcular o fib(3)
- fib(3) = fib(2) + fib(1)
- fib(3) = 2 + 1
- fib(3) = 3
- Por sua vez o fib(4)
- fib(4) = fib(3) + fib(2)
- fib(4) = 3 + 2
- fib(4) = 5
- E por ultimo o valor de fib(5)
- fib(5) = fib(4) + fib(3)
- fib(5) = 5 + 3
- fib(5) = 8

