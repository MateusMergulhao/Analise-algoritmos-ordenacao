"""
Script de benchmark para análise experimental dos algoritmos de ordenação.
Disciplina: Fundamentos da Teoria da Computação e Análise de Algoritmos
Professor: José Guilherme Picolo — PUC-Campinas

Executa cada algoritmo 3 vezes para cada tamanho de vetor (1.000, 10.000, 100.000),
usando o mesmo vetor base para garantir comparação justa.
Exibe tempo de execução (segundos), tempo médio, desvio padrão e trocas/movimentações.
"""

import random
import time
import math
import sys

from sorting_algorithms import insertion_sort, merge_sort, quick_sort

SEED = 42
SIZES = [1000, 10000, 100000]
RUNS = 3
TIMEOUT = 300 

ALGORITHMS = [
    ("Insertion Sort", "O(n²)",                              insertion_sort),
    ("Merge Sort",     "O(n log n)",                         merge_sort),
    ("Quick Sort",     "O(n log n) médio / O(n²) pior caso", quick_sort),
]

#vetores 

random.seed(SEED)
base_vectors = {n: [random.randint(1, 10 * n) for _ in range(n)] for n in SIZES}

#funções

def mean(values):
    return sum(values) / len(values)

def std_dev(values):
    m = mean(values)
    return math.sqrt(sum((v - m) ** 2 for v in values) / len(values))

def separator(char="-", width=95):
    print(char * width)

#execução dos testes

def run_benchmarks():
    print()
    separator("=")
    print("  ANÁLISE EXPERIMENTAL DOS ALGORITMOS DE ORDENAÇÃO")
    separator("=")
    print(f"  Semente aleatória : {SEED}")
    print(f"  Execuções por caso: {RUNS}")
    print(f"  Timeout           : {TIMEOUT}s (5 min) — registrado como N/C")
    separator("=")

    all_results = []

    for algo_name, complexity, fn in ALGORITHMS:
        separator()
        print(f"  Algoritmo    : {algo_name}")
        print(f"  Complexidade : {complexity}")
        separator()

        for n in SIZES:
            base = base_vectors[n]
            times = []
            moves_val = "N/C"
            timed_out = False

            for run in range(1, RUNS + 1):
                start = time.perf_counter()
                try:
                    _, moves = fn(base)
                    elapsed = time.perf_counter() - start

                    if elapsed > TIMEOUT:
                        print(f"  n={n:>7,} | Execução {run}: N/C (timeout >{TIMEOUT}s)")
                        timed_out = True
                        break

                    times.append(elapsed)
                    moves_val = moves
                    print(f"  n={n:>7,} | Execução {run}: {elapsed:.6f}s")

                except Exception as e:
                    print(f"  n={n:>7,} | Execução {run}: ERRO — {e}")
                    timed_out = True
                    break

            if timed_out or len(times) == 0:
                print(f"  n={n:>7,} | Média: N/C | Desvio: N/C | Movimentações: N/C")
                all_results.append({
                    "algo": algo_name, "complexity": complexity, "n": n,
                    "times": ["N/C"] * RUNS, "avg": "N/C", "std": "N/C", "moves": "N/C"
                })
            else:
                avg = mean(times)
                std = std_dev(times)
                print(f"  n={n:>7,} | Média: {avg:.6f}s | Desvio: {std:.8f}s | Movimentações: {moves_val:,}")
                all_results.append({
                    "algo": algo_name, "complexity": complexity, "n": n,
                    "times": times, "avg": avg, "std": std, "moves": moves_val
                })

        print()

    #resumo 
    separator("=")
    print("  RESUMO FINAL")
    separator("=")
    print(f"  {'Algoritmo':<18} {'Complexidade':<40} {'n':>8} {'Média (s)':>12} {'Desvio (s)':>14} {'Moviment.':>14}")
    separator()
    for r in all_results:
        avg = f"{r['avg']:.6f}" if isinstance(r['avg'], float) else r['avg']
        std = f"{r['std']:.8f}" if isinstance(r['std'], float) else r['std']
        mov = f"{r['moves']:,}" if isinstance(r['moves'], int) else r['moves']
        print(f"  {r['algo']:<18} {r['complexity']:<40} {r['n']:>8,} {avg:>12} {std:>14} {mov:>14}")
    separator("=")
    print()


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    run_benchmarks()