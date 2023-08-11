def main():
    m, e, n, c = map(int, input().split())
    string =  input().split()
    mapping = [0]*e
    for i in range(0, len(string), 3):
        coord = tuple(map(float, string[i:i+3]))
        mapping[i//3] = coord

    string = input().split()
    vent = [0]*n
    for i in range(0, len(string), 2):
        par = tuple(map(int, string[i:i+2]))
        vent[i//2] = par
    consultas = int(input())
    find = int(input())

    print(mapping)
    print(vent)


main()
