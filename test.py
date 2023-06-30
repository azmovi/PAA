from typing import List

def insertion(vetor):
    for i in range(len(vetor)):
        menor = i
        for j in range(i, len(vetor)):
            if vetor[j] < vetor[menor]:
                menor = j
        vetor[menor], vetor[i] = vetor[i], vetor[menor]
    return vetor

print(insertion([4, 5, 2, 1, 10, 9, 4]))
