import pytest
from numeros_primos import (
    is_primo_forca_bruta,
    is_primo_otimizado,
    crivo_eratostenes,
    fatorar,
    proximo_primo,
)

PRIMOS_CONHECIDOS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
NAO_PRIMOS = [0, 1, 4, 6, 8, 9, 10, 12, 15, 20, 25, 100]


class TestIsPrimoForcaBruta:
    @pytest.mark.parametrize("n", PRIMOS_CONHECIDOS)
    def test_primos_conhecidos(self, n):
        assert is_primo_forca_bruta(n) is True

    @pytest.mark.parametrize("n", NAO_PRIMOS)
    def test_nao_primos(self, n):
        assert is_primo_forca_bruta(n) is False

    def test_numero_negativo(self):
        assert is_primo_forca_bruta(-7) is False


class TestIsPrimoOtimizado:
    @pytest.mark.parametrize("n", PRIMOS_CONHECIDOS)
    def test_primos_conhecidos(self, n):
        assert is_primo_otimizado(n) is True

    @pytest.mark.parametrize("n", NAO_PRIMOS)
    def test_nao_primos(self, n):
        assert is_primo_otimizado(n) is False

    def test_numero_grande_primo(self):
        assert is_primo_otimizado(999983) is True

    def test_numero_grande_nao_primo(self):
        assert is_primo_otimizado(999981) is False

    def test_concordancia_com_forca_bruta(self):
        for n in range(0, 100):
            assert is_primo_otimizado(n) == is_primo_forca_bruta(n), f"Divergência em n={n}"


class TestCrivoEratostenes:
    def test_limite_menor_que_dois(self):
        assert crivo_eratostenes(1) == []

    def test_limite_zero(self):
        assert crivo_eratostenes(0) == []

    def test_primos_ate_50(self):
        assert crivo_eratostenes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    def test_apenas_dois(self):
        assert crivo_eratostenes(2) == [2]

    def test_todos_sao_primos(self):
        primos = crivo_eratostenes(100)
        for p in primos:
            assert is_primo_otimizado(p), f"{p} deveria ser primo"

    def test_quantidade_primos_ate_100(self):
        assert len(crivo_eratostenes(100)) == 25


class TestFatorar:
    def test_fatorar_12(self):
        assert fatorar(12) == [2, 2, 3]

    def test_fatorar_primo(self):
        assert fatorar(13) == [13]

    def test_fatorar_potencia_de_2(self):
        assert fatorar(32) == [2, 2, 2, 2, 2]

    def test_produto_dos_fatores_e_o_original(self):
        for n in [12, 36, 100, 360, 999]:
            fatores = fatorar(n)
            produto = 1
            for f in fatores:
                produto *= f
            assert produto == n

    def test_fatores_sao_todos_primos(self):
        for n in [12, 60, 100, 210]:
            for f in fatorar(n):
                assert is_primo_otimizado(f), f"{f} nao e primo"


class TestProximoPrimo:
    def test_apos_1(self):
        assert proximo_primo(1) == 2

    def test_apos_2(self):
        assert proximo_primo(2) == 3

    def test_apos_10(self):
        assert proximo_primo(10) == 11

    def test_apos_primo_e_primo(self):
        resultado = proximo_primo(7)
        assert is_primo_otimizado(resultado)

    def test_e_maior_que_n(self):
        for n in [5, 10, 20, 50]:
            assert proximo_primo(n) > n
