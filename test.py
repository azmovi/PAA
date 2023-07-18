from typing import List, Tuple
def soma(A:List[int], B:List[int], target:int) -> Tuple[int, int]:
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

print(soma([5, 13, 20], [0, 15, 8], 13))
