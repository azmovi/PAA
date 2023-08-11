
def main():
    loop = int(input())
    resposta = [0]*loop
    for i in range(loop):
        string = input().split()
        choice = int(string[0])
        total = int(string[1])
        notas = list(map(float, string[2:]))
        heap_sort(choice, notas)
        resposta[i] = notas[0]
    for resp in resposta:
        print("{:.2f}".format(resp))
    return

def heap_sort(choice:int, notas:list[float]):

    build_heap(notas)
    n = len(notas)
    for i in range(n-1, n-choice, -1):
        notas[i], notas[0] = notas[0], notas[i]
        heapfy(notas, i)
    return 

def heapfy(vector, n, indice = 0):
    maior = indice
    left = 2*indice + 1
    right = 2*indice + 2

    if left < n and vector[left] > vector[maior]:
        maior = left 
    if right < n and vector[right] > vector[maior]:
        maior = right

    if maior != indice:
        vector[indice], vector[maior] = vector[maior], vector[indice]
        heapfy(vector, n,  maior)

def build_heap(vector):
    for i in range(len(vector)//2 - 1, -1, -1):
        heapfy(vector, len(vector), i)
    return

main()
