# Lista 2 - Alan Demétrius 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
> Divisão e Conquista e Análise Assintótica 

### 1 - Questão:
```py
def lives(nasce:List[int], mortos:List[int]):
    hash_mortos = {}
    for ano in mortos:
        if ano in hash_mortos:
            hash_mortos[ano] += 1
        else:
            hash_mortos[ano] = 1

    maior = 0
    maior_ano = 0
    total = 0
    for ano in nasce:
        if ano in hash_mortos:
            total -= hash_mortos[ano]
        total += 1
        if total > maior:
            maior = total
            maior_ano = ano
    return maior_ano, maior
```
Dado que o código está performando de forma correta e que a entrada duas listas
são ordenadas, temos que a complexidade desse algoritmo é:

- Primeira etapa: criação de uma hash table com o ano dos falecimentos agrupados
ela é feita em $O(n)$
- Segunda etapa: um for onde o número de iterações será o tamanho da lista de 
nascimentos
- Terceira etapa: Verificação se naquele determinado ano houve mortes com complexidade 
igual a $O(1)$ devido a estrutura de dados ser uma hash table
- Quarta etapa: Verificar se a quantidade populacional atual é a maior presente
e com isso guardar o seu ano.

Dessa forma percebemos que esse algoritmo tem complexidade igual a $O(n)$ sendo
$n$ o tamanho tamanho dos vetores de entrada.

### 5 - Questão:
```py
def soma(A:List[int], B:List[int], target:int) -> List[Tuple[int, int]]:
    resultado = []
    for numero in B:
        find = target - numero
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (r + l) // 2

            if A[mid] < find:
                l = mid + 1

            elif A[mid] > find:
                r = mid - 1

            else:
                resultado.append((A[mid], numero))
                l = r + 1

    return resultado
```

### 6 - Questão:
$$ T(n) = a * T(\frac{n}{b}) + c * n^d $$
$$ T(n) = 729 * T(\frac{n}{9}) + 15 * n^3 $$
$$ a = 729 \space | \space b = 9 \space | \space c = 15 \space | \space d = 3 $$
- Temos que:
$$ 729 =  9^3 $$
- Logo concluímos que a complexidade desse algoritmo é $O(n^3 * \log{n})$

### 7 - Questão:
###### a) Quantos subproblemas são gerados no algoritmo?
- Dividimos o problema em $n$ subproblemas.
###### b) Qual o tamanho dos vetores desses subproblemas?
- Cada subproblema vai ter tamanho 1 no ultima divisão.
###### c) Quantas operações são feitas na ordenação?
- No processo de ordenação são feitas $n$ comparações sendo $n$ o tamanho do sub vetor
até $n$ ter o tamanho do vetor original e isso vai ocorrer $k$ vezes, sendo $k$ igual
a $\log{n}$ que é a quantidade de recursões. 
###### d) Qual a recorrência do _merge sort_?
$$ T(n) = 2T(\frac{n}{2}) + n $$
- Sendo duas chamadas recursivas com o vetor divido na metade, parte esquerda e 
parte direita, e n sendo as operações de comparação para ordenar.
###### e) Qual é o último nível do _merge sort_?
$$ T(\frac{n}{2^k}) = ? $$
$$ \frac{n}{2^k} = 1 $$
$$ n = 2^k $$
$$ \log_{2}n = \log_{2}2^k $$
$$ \log_{2}n = k * \log_{2}2 $$
$$ \log_{2}n = k $$

### 8 - Questão:
- Encontrar o Big-O do _merg sort_ pelo método da recorrência.

$$ T(n) = 2T(\frac{n}{2}) + n $$
$$ T(n) = 2(2T(\frac{n}{4}) + \frac{n}{2}) + n $$
$$ T(n) = 4T(\frac{n}{4}) + n + n $$
$$ T(n) = 4(2T(\frac{n}{8}) + \frac{n}{4}) + n + n $$
$$ T(n) = 8T(\frac{n}{8}) n + n + n $$
$$ T(n) = 2^3T(\frac{n}{2^3}) + 3n $$

- Dessa forma conseguimos generalizar para:
$$ T(n) =  2^h + h*n$$

- Sendo $h$ a altura da árvore temos:
$$\frac{n}{2^h} = 1 $$
$$n = 2^h $$
$$ \log_{2}{n} = h * \log_{2} 2$$
$$ \log_{2}{n} = h $$

- Substituindo na equação principal:
$$ T(n) =  2^{\log_{2}n} + \log_{2}{n}*n$$

- Simplificando e removendo constantes
$$ T(n) = n + \log_{2}{n}*n$$

- Com isso percebemos que a complexidade do _merge sort_ é:

$$ O(n*\log_{2}n)$$


