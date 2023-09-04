
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


print(main())
