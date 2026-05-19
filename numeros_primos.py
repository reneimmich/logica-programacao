# Numeros Primos
# Tres abordagens: forca bruta, otimizada e Crivo de Eratostenes

import math
import time

def is_primo_forca_bruta(n):
    """Verifica se n e primo - abordagem simples O(n)."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_primo_otimizado(n):
    """Verifica se n e primo - abordagem otimizada O(sqrt(n))."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def crivo_eratostenes(limite):
    """Encontra todos os primos ate 'limite' usando o Crivo de Eratostenes."""
    if limite < 2:
        return []
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(math.sqrt(limite)) + 1):
        if primos[i]:
            for j in range(i * i, limite + 1, i):
                primos[j] = False
    return [i for i, p in enumerate(primos) if p]

def fatorar(n):
    """Retorna a fatoracao em primos de n."""
    fatores = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            fatores.append(d)
            n //= d
        d += 1
    if n > 1:
        fatores.append(n)
    return fatores

def proximo_primo(n):
    """Retorna o proximo primo apos n."""
    candidato = n + 1
    while not is_primo_otimizado(candidato):
        candidato += 1
    return candidato

def main():
    print("=== Numeros Primos ===")
    while True:
        print("\n1 - Verificar se um numero e primo")
        print("2 - Listar primos ate N (Crivo de Eratostenes)")
        print("3 - Fatorar um numero")
        print("4 - Proximo primo apos N")
        print("5 - Comparar velocidade dos algoritmos")
        print("0 - Sair")
        opcao = input("Opcao: ")

        if opcao == "0":
            break
        elif opcao == "1":
            n = int(input("Digite o numero: "))
            if is_primo_otimizado(n):
                print(f"{n} E primo!")
            else:
                print(f"{n} NAO e primo.")
        elif opcao == "2":
            lim = int(input("Ate qual numero? "))
            primos = crivo_eratostenes(lim)
            print(f"Encontrados {len(primos)} primos ate {lim}:")
            print(primos[:50], "..." if len(primos) > 50 else "")
        elif opcao == "3":
            n = int(input("Digite o numero para fatorar: "))
            fatores = fatorar(n)
            print(f"Fatores primos de {n}: {fatores}")
            print(f"Verificacao: {' x '.join(map(str, fatores))} = {eval(' * '.join(map(str, fatores)))}")
        elif opcao == "4":
            n = int(input("Apos qual numero? "))
            print(f"Proximo primo apos {n}: {proximo_primo(n)}")
        elif opcao == "5":
            n = int(input("Verificar primalidade de N (ex: 999983): "))
            t = time.time(); r1 = is_primo_forca_bruta(n); t1 = time.time() - t
            t = time.time(); r2 = is_primo_otimizado(n); t2 = time.time() - t
            print(f"Forca bruta:  {r1} em {t1:.6f}s")
            print(f"Otimizado:    {r2} em {t2:.6f}s")
            print(f"Speedup: {t1/t2:.1f}x mais rapido")

if __name__ == "__main__":
    main()
