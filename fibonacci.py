# Sequencia de Fibonacci
# Tres abordagens: iterativa, recursiva e com memoizacao

import time

# Abordagem 1: Iterativa (mais eficiente)
def fibonacci_iterativo(n):
    if n <= 0: return []
    if n == 1: return [0]
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

# Abordagem 2: Recursiva simples (educativa, porem lenta)
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Abordagem 3: Recursiva com memoizacao (rapida)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def comparar_desempenho(n):
    print(f"\n=== Comparando desempenho para fib({n}) ===")

    inicio = time.time()
    resultado = fibonacci_iterativo(n)[-1] if n > 0 else 0
    tempo_iter = time.time() - inicio
    print(f"Iterativo:    {resultado} em {tempo_iter:.6f}s")

    inicio = time.time()
    resultado = fibonacci_memo(n)
    tempo_memo = time.time() - inicio
    print(f"Memoizacao:   {resultado} em {tempo_memo:.6f}s")

    if n <= 30:
        inicio = time.time()
        resultado = fibonacci_recursivo(n)
        tempo_rec = time.time() - inicio
        print(f"Recursivo:    {resultado} em {tempo_rec:.6f}s")
    else:
        print(f"Recursivo:    (pulado, muito lento para n={n})")

def main():
    print("=== Sequencia de Fibonacci ===")
    while True:
        print("\n1 - Ver sequencia")
        print("2 - Calcular F(n)")
        print("3 - Comparar desempenho")
        print("0 - Sair")
        opcao = input("Opcao: ")

        if opcao == "0":
            break
        elif opcao == "1":
            try:
                n = int(input("Quantos termos? "))
                seq = fibonacci_iterativo(n)
                print(f"Sequencia: {seq}")
            except ValueError:
                print("Digite um numero inteiro!")
        elif opcao == "2":
            try:
                n = int(input("Qual F(n)? "))
                print(f"F({n}) = {fibonacci_memo(n)}")
            except ValueError:
                print("Digite um numero inteiro!")
        elif opcao == "3":
            try:
                n = int(input("Valor de n para comparar (recomendado ate 35): "))
                comparar_desempenho(n)
            except ValueError:
                print("Digite um numero inteiro!")

if __name__ == "__main__":
    main()
