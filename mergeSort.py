import numpy as np


def mergeSort(arr, p, r):
    if p < r:
        q = (p+r) // 2
        if pintamos in ['s', 'S']:
            paint(arr, p, q, r)
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
        merge(arr, p, q, r)
        if pintamos in ['s', 'S']:
            paint(arr, p, q, r)
    return arr


def merge(arr, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = np.empty(n1+1)
    R = np.empty(n2+1)
    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[q + 1 + j]
    L[n1] = np.inf
    R[n2] = np.inf
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
    return arr


def paint(A, p, q, r):
    for i in range(len(A)):
        if i == p:
            print(' [ ', end='')
        print(A[i], ' ', end='')
        if i == q:
            print('] [ ', end='')
        if i == r:
            print(']', end='')
    print()


ra = int(input('Introduce el rango de valores (1 - valor): '))
si = int(input('Introduce el tamaño del array a ordenar: '))
pintamos = input('¿Quiéres pintar los pasos intermedios? (s/n): ')
if si <= 0:
    si = 2
if ra < 1:
    ra = 1
arr = np.random.randint(ra, size=si)
arr = mergeSort(arr, 0, len(arr)-1)
paint(arr, 0, len(arr)-1 // 2, len(arr)-1)
