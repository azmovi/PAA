# Lista 1 - Alan Demétrius 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
> Recursão e Análise assintótica 
### 1 - Questão 
- Algoritmo recursivo para buscar um elemento v em um vetor A, caso exista retornar o índice
se não retornar _NULL_.

```py
def busca_sequencial_recursiva(A: List[int], v: int, indice: int = 0) -> int:
    if len(A) == 0:
        return None

    if A[0] == v:
        return indice

    else:
        return busca_sequencial_recursiva(A[1:], v, indice+1)
```
- Análise da complexidade de tempo:
$$ T(n) = 1 + 1 + 1 + T(n-1) $$
$$ T(n-1) = 1 + 1 + 1 + T(n-1-1) $$
- Generalizando:
$$ T(n) = 3 + T(n-1) $$
$$ T(n) = \sum_{i=0}^{n} (3 + T(n-1-i)) $$
$$ T(n) = \sum_{i=0}^{n} 3 + T(0) $$
$$ T(n) = 3n $$
- Dessa forma chegamos no $\text{O}(n)$

### 2 - Questão 
- Encontrar se uma palavra é um palíndromo. Escrever um algoritmo recursivo e
iterativo. (É possível escrever em uma linha de código?)
```py
def palindromo_recursivo(palavra: str) -> bool:
    print(palavra)
    if len(palavra) == 0:
        return True 
    if palavra[0] != palavra[-1]:
        return False
    else:
        return palindromo(palavra[1:-1])

def iterativo(palavra: str) -> bool:
    return all(palavra[i] == palavra[-i-1] for i in range(len(palavra)//2))

```

### 3 - Questão 
- Ordenar n elementos em um vetor A pelo método do _Insertion Sort_. E verificar
a complexidade desse algoritmo.
```py
def insertion(vetor):
    for i in range(len(vetor)):
        menor = i
        for j in range(i, len(vetor)):
            if vetor[j] < vetor[menor]:
                menor = j
        vetor[menor], vetor[i] = vetor[i], vetor[menor]
    return vetor

```
- Análise da complexidade do _Insertion Sort_
$$ T(n) = \sum_{i=0}^{n-1}(3 + \sum_{j = i}^{n-1} 1)$$
$$ T(n) = \sum_{i=0}^{n-1}3 + \sum_{i=0}^{n-1} \sum_{j = i}^{n-1} 1)$$
$$ T(n) = 3n + \sum_{i=0}^{n-1} n-i $$

- Usando soma de n termos de uma progressão aritmética:
$$ T(n) = 3n + \frac{(n + 1)n}{2}$$

- Simplificando nossa expressão e abstraindo as constantes
$$ T(n) = n + n^2 $$

- Concluímos que a complexidade desse algoritmo está na ordem de $O(n^2)$

### 4 - Questão 
- Escrever um algoritmo para determinar se existe uma letras duplicadas.
E determinar sua complexidade.

```py
def duplicada(string:str):
    letras = set()
    for letra in string:
        if letra in letras:
            return True
        letras.add(letra)
    return False

```
- Para analisarmos complexidade precisamos previamente saber como funciona o if
presente no código, ele vai executar em tempo constante logo $O(1)$, dessa forma
conseguimos perceber que o responsável pela complexidade é unicamente o tamanho da
string que for passada para função, já que o restante trabalha em tempo constante.
