import pytest
import random
from ordenacao import bubble_sort, selection_sort, insertion_sort, quick_sort


ALGORITMOS = [bubble_sort, selection_sort, insertion_sort, quick_sort]
NOMES = ["bubble_sort", "selection_sort", "insertion_sort", "quick_sort"]


@pytest.fixture
def lista_aleatoria():
    random.seed(42)
    return [random.randint(-100, 100) for _ in range(50)]


@pytest.fixture
def lista_ordenada():
    return list(range(1, 11))


class TestBubbleSort:
    def test_lista_basica(self):
        assert bubble_sort([3, 1, 2]) == [1, 2, 3]

    def test_lista_vazia(self):
        assert bubble_sort([]) == []

    def test_um_elemento(self):
        assert bubble_sort([42]) == [42]

    def test_negativos(self):
        assert bubble_sort([-3, -1, -2]) == [-3, -2, -1]

    def test_ja_ordenada(self):
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_ordem_inversa(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_nao_modifica_original(self):
        original = [3, 1, 2]
        bubble_sort(original)
        assert original == [3, 1, 2]


class TestSelectionSort:
    def test_lista_basica(self):
        assert selection_sort([3, 1, 2]) == [1, 2, 3]

    def test_lista_vazia(self):
        assert selection_sort([]) == []

    def test_duplicatas(self):
        assert selection_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

    def test_nao_modifica_original(self):
        original = [3, 1, 2]
        selection_sort(original)
        assert original == [3, 1, 2]


class TestInsertionSort:
    def test_lista_basica(self):
        assert insertion_sort([3, 1, 2]) == [1, 2, 3]

    def test_lista_vazia(self):
        assert insertion_sort([]) == []

    def test_negativos_e_positivos(self):
        assert insertion_sort([-2, 5, -1, 3]) == [-2, -1, 3, 5]

    def test_nao_modifica_original(self):
        original = [3, 1, 2]
        insertion_sort(original)
        assert original == [3, 1, 2]


class TestQuickSort:
    def test_lista_basica(self):
        assert quick_sort([3, 1, 2]) == [1, 2, 3]

    def test_lista_vazia(self):
        assert quick_sort([]) == []

    def test_um_elemento(self):
        assert quick_sort([7]) == [7]

    def test_duplicatas(self):
        assert quick_sort([4, 2, 4, 1]) == [1, 2, 4, 4]


@pytest.mark.parametrize("algoritmo", ALGORITMOS, ids=NOMES)
class TestTodosAlgoritmos:
    def test_resultado_igual_ao_sorted(self, algoritmo, lista_aleatoria):
        assert algoritmo(lista_aleatoria) == sorted(lista_aleatoria)

    def test_lista_vazia(self, algoritmo, lista_aleatoria):
        assert algoritmo([]) == []

    def test_tamanho_preservado(self, algoritmo, lista_aleatoria):
        resultado = algoritmo(lista_aleatoria)
        assert len(resultado) == len(lista_aleatoria)

    def test_mesmos_elementos(self, algoritmo, lista_aleatoria):
        resultado = algoritmo(lista_aleatoria)
        assert sorted(resultado) == sorted(lista_aleatoria)

    def test_lista_com_duplicatas(self, algoritmo, lista_aleatoria):
        lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        assert algoritmo(lista) == sorted(lista)
