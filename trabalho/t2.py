import heapq
class Grafo():
    def __init__(self, vertices:int):
        self.vertices = vertices
        self.matrix = [[[0, 0] for coluna in range(vertices)]for linha in range(vertices)]


    def add_arestas(self, l, c, size, tipo):
        if l == c:
            print("Não existe arestas no mesmo vertice")
        if tipo:
            self.matrix[l][c][1] = size 
            self.matrix[c][l][1] = size
        else:
            self.matrix[l][c][0] = size
            self.matrix[c][l][0] = size


        return 

    def show(self):
        for linha in range(self.vertices):
            print(self.matrix[linha])
        return

def dijkstra(grafo: Grafo, inicio:int, tipo:int):
    distancias = {}
    predecessor = {}
    visitados = set()
    for vertice in range(grafo.vertices):
        distancias[vertice] = float("inf")
    distancias[inicio] = 0
    pqueue = []
    heapq.heappush(pqueue, (0, inicio))

    while len(pqueue) != 0:
        d_atual, v_atual = heapq.heappop(pqueue)
        visitados.add(v_atual)

        for vizinho in range(grafo.vertices):
            if tipo == 0: #normal
                if grafo.matrix[v_atual][vizinho][0] != 0 and vizinho not in visitados:
                    distancia = grafo.matrix[v_atual][vizinho][0]

                    if d_atual + distancia < distancias[vizinho]:
                        distancias[vizinho] = d_atual + distancia
                        heapq.heappush(pqueue, (distancias[vizinho], vizinho))
            else:
                if grafo.matrix[v_atual][vizinho][0] != 0 or grafo.matrix[v_atual][vizinho][1] != 0:
                    if grafo.matrix[v_atual][vizinho][0] != 0 and grafo.matrix[v_atual][vizinho][1] != 0:
                        if grafo.matrix[v_atual][vizinho][0] < grafo.matrix[v_atual][vizinho][1]:
                            distancia = grafo.matrix[v_atual][vizinho][0]
                        else:
                            distancia = grafo.matrix[v_atual][vizinho][1]

                    elif grafo.matrix[v_atual][vizinho][0] != 0:
                        distancia = grafo.matrix[v_atual][vizinho][0]

                    else:
                        distancia = grafo.matrix[v_atual][vizinho][1]


                    if d_atual + distancia < distancias[vizinho]:
                        distancias[vizinho] = d_atual + distancia
                        heapq.heappush(pqueue, (distancias[vizinho], vizinho))
            #print(distancias[0])

    return distancias



def main():
    n_salas, n_corredor, n_tubos, loop= map(int, input().split())
    resposta = [0]*loop
    grafo = Grafo(n_salas)
    corredores = input().split()
    for i in range(0, len(corredores), 3):
        inicio, fim= int(corredores[i]), int(corredores[i+1])
        tamanho = float(corredores[i+2])
        grafo.add_arestas(inicio, fim, tamanho, 0)

    tubos = input().split()
    for i in range(0, len(tubos), 2):
        inicio, fim = int(tubos[i]), int(tubos[i+1])
        grafo.add_arestas(inicio, fim, 1, 1)
    for i in range(loop):
        inicio = int(input())
        normal = 0
        estranho = 1
        distancias = dijkstra(grafo, inicio, normal)
        distancia_normal = distancias[0]
        distancias = dijkstra(grafo, inicio, estranho)
        distancia_estranho = distancias[0]
        if (distancia_normal) <= distancia_estranho + 0.000000000000001:
            resposta[i] = 'victory'
        else:
            resposta[i] = 'defeat'

    for resp in resposta:
        print(resp)

    return 

main()
