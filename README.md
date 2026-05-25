# Lógica de Programação — Algoritmos e Testes Automatizados

Algoritmos clássicos implementados em Python com **3 abordagens por problema** e cobertura completa de testes via **pytest**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-165%20testes-green?style=flat-square&logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/testes-passando-brightgreen?style=flat-square)

---

## Algoritmos

| Arquivo | Abordagens | Testes |
|---------|-----------|--------|
| `fibonacci.py` | Iterativa, Recursiva, Memoização | `tests/test_fibonacci.py` |
| `numeros_primos.py` | Força bruta, Otimizada O(√n), Crivo de Eratóstenes | `tests/test_numeros_primos.py` |
| `ordenacao.py` | Bubble Sort, Selection Sort, Insertion Sort, Quick Sort | `tests/test_ordenacao.py` |

---

## Como executar

```bash
# Clonar o repositório
git clone https://github.com/reneimmich/logica-programacao.git
cd logica-programacao

# Instalar dependências
pip install -r requirements.txt

# Rodar um algoritmo
python fibonacci.py

# Rodar os testes
pytest

# Rodar testes com detalhes
pytest -v

# Rodar com cobertura
pytest --cov=. --cov-report=term-missing
```

---

## Estrutura de Testes (QA)

```
tests/
├── conftest.py               # Configuração e fixtures globais
├── test_fibonacci.py         # 36 testes — 3 implementações + consistência entre elas
├── test_numeros_primos.py    # 63 testes — primos, crivo, fatoração, próximo primo
└── test_ordenacao.py         # 66 testes — 4 algoritmos com @parametrize cross-test
```

**Técnicas aplicadas:**
- `@pytest.fixture` para dados reutilizáveis entre testes
- `@pytest.mark.parametrize` para testar múltiplos valores e cenários
- Classes parametrizadas (`TestTodosAlgoritmos`) para aplicar os mesmos testes em 4 algoritmos
- Testes de consistência cruzada entre implementações diferentes
- Casos de borda: lista vazia, um elemento, negativos, duplicatas, números grandes

---

## Algoritmos — Complexidade

| Algoritmo | Melhor | Médio | Pior |
|-----------|--------|-------|------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Fibonacci iterativo | O(n) | O(n) | O(n) |
| Fibonacci memoizado | O(n) | O(n) | O(n) |
| Crivo de Eratóstenes | — | O(n log log n) | — |

---

## Tecnologias

- Python 3.x
- pytest / pytest-cov

---

## Autor

**Renê Immich** — [LinkedIn](https://linkedin.com/in/reneimmich) | [GitHub](https://github.com/reneimmich)
