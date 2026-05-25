import pytest
from fibonacci import fibonacci_iterativo, fibonacci_recursivo, fibonacci_memo


SEQUENCIA_CONHECIDA = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


class TestFibonacciIterativo:
    def test_zero_termos(self):
        assert fibonacci_iterativo(0) == []

    def test_um_termo(self):
        assert fibonacci_iterativo(1) == [0]

    def test_dois_termos(self):
        assert fibonacci_iterativo(2) == [0, 1]

    def test_dez_termos(self):
        assert fibonacci_iterativo(10) == SEQUENCIA_CONHECIDA[:10]

    def test_onze_termos(self):
        assert fibonacci_iterativo(11) == SEQUENCIA_CONHECIDA

    def test_negativo_retorna_vazio(self):
        assert fibonacci_iterativo(-5) == []

    @pytest.mark.parametrize("n,esperado", [
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (7, [0, 1, 1, 2, 3, 5, 8]),
    ])
    def test_primeiros_n_termos(self, n, esperado):
        assert fibonacci_iterativo(n) == esperado


class TestFibonacciRecursivo:
    def test_f0(self):
        assert fibonacci_recursivo(0) == 0

    def test_f1(self):
        assert fibonacci_recursivo(1) == 1

    def test_f2(self):
        assert fibonacci_recursivo(2) == 1

    def test_f10(self):
        assert fibonacci_recursivo(10) == 55

    @pytest.mark.parametrize("n,esperado", [
        (0, 0), (1, 1), (2, 1), (3, 2),
        (4, 3), (5, 5), (6, 8), (7, 13),
    ])
    def test_valores_conhecidos(self, n, esperado):
        assert fibonacci_recursivo(n) == esperado


class TestFibonacciMemo:
    def test_f0(self):
        assert fibonacci_memo(0) == 0

    def test_f1(self):
        assert fibonacci_memo(1) == 1

    def test_f10(self):
        assert fibonacci_memo(10) == 55

    def test_f20(self):
        assert fibonacci_memo(20) == 6765

    def test_consistente_com_iterativo(self):
        for n in range(15):
            seq = fibonacci_iterativo(n + 1)
            assert fibonacci_memo(n) == seq[n]


class TestConsistenciaEntreAbordagens:
    @pytest.mark.parametrize("n", range(1, 16))
    def test_iterativo_e_memo_concordam(self, n):
        seq = fibonacci_iterativo(n)
        assert seq[-1] == fibonacci_memo(n - 1)

    @pytest.mark.parametrize("n", range(0, 10))
    def test_recursivo_e_memo_concordam(self, n):
        assert fibonacci_recursivo(n) == fibonacci_memo(n)
