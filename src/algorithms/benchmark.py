import csv
import statistics
from time import perf_counter

from algorithms.sorting import insertion_sort, quick_sort

from algorithms.data_generators import (
    generate_random,
    generate_sorted,
    generate_reverse,
    generate_nearly_sorted,
    generate_duplicates,
)


# Параметры 
SIZES = [100, 1000, 10000]
REPEATS = 10
SEED = 42


# Алгоритмы для сравнения
SORTS = {
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
}


# Генераторы входных данных
GENERATORS = {
    "Random": lambda size: generate_random(
        size, min_value=-1000, max_value=1000, seed=SEED
    ),

    "Sorted": lambda size: generate_sorted(
        size, min_value=-1000, max_value=1000, seed=SEED
    ),

    "Reverse": lambda size: generate_reverse(
        size, min_value=-1000, max_value=1000, seed=SEED
    ),

    "Nearly sorted": lambda size: generate_nearly_sorted(
        size, min_value=-1000, max_value=1000, seed=SEED
    ),

    "Duplicates": lambda size: generate_duplicates(
        size, min_value=0, max_value=5, seed=SEED
    ),
}


def measure_sort(sort_function, data):
    """Измеряет время выполнения одной сортировки."""

    # Запуск БЕЗ учета результатов
    sort_function(data.copy())

    times = []

    for _ in range(REPEATS):
        # Независимая копия для каждого измерения
        arr = data.copy()

        start = perf_counter()
        result = sort_function(arr)
        elapsed = perf_counter() - start

        times.append(elapsed)

        # Освобождаем возвращённый результат после измерения
        del result

    average = statistics.mean(times)
    median = statistics.median(times)

    return average, median


def run_benchmark():
    results = []

    for input_type, generator in GENERATORS.items():
        for size in SIZES:

            # Генерация данных вне измерения
            data = generator(size)

            for algorithm_name, sort_function in SORTS.items():

                average, median = measure_sort(sort_function, data)

                results.append({
                    "algorithm": algorithm_name,
                    "input_type": input_type,
                    "size": size,
                    "repeats": REPEATS,
                    "average_time_seconds": f"{average:.8f}",
                    "median_time_seconds": f"{median:.8f}",
                })

                print(
                    f"{algorithm_name}: "
                    f"{input_type}, size={size} — "
                    f"median={median:.8f} sec"
                )

    return results


def save_results(results):
    with open(
        "benchmark_results.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        fieldnames = [
            "algorithm",
            "input_type",
            "size",
            "repeats",
            "average_time_seconds",
            "median_time_seconds",
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    results = run_benchmark()
    save_results(results)

    print("\nBenchmark completed!")
    print("Results saved to benchmark_results.csv")
