# Análise Experimental de Algoritmos de Ordenação

**Disciplina:** Fundamentos da Teoria da Computação e Análise de Algoritmos  
**Professor:** José Guilherme Picolo   
---

## Algoritmos implementados

| Algoritmo | Melhor caso | Caso médio | Pior caso |
|---|---|---|---|
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

---

## Estrutura do repositório

```
📁 repositorio/
├── sorting_algorithms.py   
├── benchmark.py            
└── README.md               
```

---

## Como executar

### Pré-requisito
- Python 3.8 ou superior instalado

### Rodando os testes
```bash
python benchmark.py
```

O script irá:
1. Gerar vetores aleatórios com semente fixa (seed=42) para n = 1.000, 10.000 e 100.000
2. Executar cada algoritmo 3 vezes usando o mesmo vetor base por tamanho
3. Exibir os tempos individuais, tempo médio, desvio padrão e quantidade de trocas/movimentações
4. Registrar N/C para execuções que ultrapassem 5 minutos

### Exemplo de saída esperada
```
===============================================================================
  ANÁLISE EXPERIMENTAL DOS ALGORITMOS DE ORDENAÇÃO
===============================================================================
  Semente aleatória : 42
  Execuções por caso: 3
  Timeout           : 300s (5 min) — registrado como N/C
===============================================================================
  Algoritmo    : Insertion Sort
  Complexidade : O(n²)
-------------------------------------------------------------------------------
  n=  1.000 | Execução 1: 0.014000s
  n=  1.000 | Execução 2: 0.013950s
  n=  1.000 | Execução 3: 0.014430s
  n=  1.000 | Média: 0.014127s | Desvio: 0.00002s | Movimentações: 238.485
  ...
```

---

## Metodologia

- **Vetor compartilhado:** para cada tamanho de vetor, um único vetor base é gerado com random.seed(42). O mesmo vetor é fornecido como entrada para os três algoritmos, garantindo comparação justa.
- **Contagem de operações:**
  - *Insertion Sort:* conta deslocamentos de elementos e inserções da chave
  - *Merge Sort:* conta escritas de elementos durante a intercalação (merge)
  - *Quick Sort:* conta trocas de posição durante o particionamento
- **Timeout:** qualquer execução que ultrapasse 300 segundos é interrompida e registrada como N/C (Não Concluído)
- **Quick Sort iterativo:** implementado com pilha explícita para evitar erros de limite de recursão do Python em vetores grandes

---

## Resultados obtidos

| Algoritmo | n = 1.000 | n = 10.000 | n = 100.000 |
|---|---|---|---|
| Insertion Sort | ~0,014s | ~1,586s | N/C (>5 min) |
| Merge Sort | ~0,001s | ~0,017s | ~0,225s |
| Quick Sort | ~0,001s | ~0,012s | ~0,152s |

> Ambiente de execução: Windows 11 · Intel Core i7-13620H · 16 GB RAM · Python 3

Os resultados confirmam a teoria: o Insertion Sort cresce de forma quadrática e se torna inviável para entradas grandes, enquanto Merge Sort e Quick Sort mantêm crescimento logarítmico e finalizam todos os testes em frações de segundo.
