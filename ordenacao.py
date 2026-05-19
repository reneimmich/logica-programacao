# Algoritmos de Ordenacao
# Bubble Sort, Selection Sort, Insertion Sort e Quick Sort

import time
import random

def bubble_sort(lista):
    """Ordenacao bolha - O(n^2) - didatico."""
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:
            break
    return arr

def selection_sort(lista):
    """Ordenacao por selecao - O(n^2)."""
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(lista):
    """Ordenacao por insercao - O(n^2), eficiente para listas quase ordenadas."""
    arr = lista.copy()
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

def quick_sort(lista):
    """Quick Sort - O(n log n) em media, muito rapido na pratica."""
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais  = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)

def comparar_algoritmos(tamanho):
    lista = [random.randint(1, 1000) for _ in range(tamanho)]
    print(f"\nComparando com lista de {tamanho} elementos:")
    print("-" * 45)

    algoritmos = [
        ("Bubble Sort",    bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Quick Sort",     quick_sort),
        ("Python sorted()",sorted),
    ]

    for nome, func in algoritmos:
        inicio = time.perf_counter()
        resultado = func(lista)
        tempo = time.perf_counter() - inicio
        print(f"  {nome:<18}: {tempo*1000:.3f} ms")

    print(f"\nLista ordenada? {resultado == sorted(lista)}")

def main():
    print("=== Algoritmos de Ordenacao ===")
    while True:
        print("\n1 - Visualizar ordenacao passo a passo")
        print("2 - Comparar velocidade dos algoritmos")
        print("0 - Sair")
        opcao = input("Opcao: ")

        if opcao == "0":
            break
        elif opcao == "1":
            entrada = input("Digite numeros separados por espaco: ")
            try:
                lista = list(map(int, entrada.split()))
                print(f"Original:       {lista}")
                print(f"Bubble Sort:    {bubble_sort(lista)}")
                print(f"Selection Sort: {selection_sort(lista)}")
                print(f"Insertion Sort: {insertion_sort(lista)}")
                print(f"Quick Sort:     {quick_sort(lista)}")
            except ValueError:
                print("Entrada invalida!")
        elif opcao == "2":
            try:
                tam = int(input("Tamanho da lista (ex: 1000): "))
                comparar_algoritmos(tam)
            except ValueError:
                print("Digite um numero valido!")

if __name__ == "__main__":
    main()
