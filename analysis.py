import random
import time

def quicksort(arr, pivot_strategy):
    if len(arr) <= 1:
        return arr

    pivot = (
        arr[0] if pivot_strategy == "first" else
        arr[len(arr) // 2] if pivot_strategy == "middle" else
        arr[random.randint(0, len(arr) - 1)] if pivot_strategy == "random" else
        None
    )

    if pivot is None:
        raise ValueError("Invalid pivot strategy")

    less, equal, greater = [], [], []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return quicksort(less, pivot_strategy) + equal + quicksort(greater, pivot_strategy)

def generate_data(size, data_type):
    match data_type:
        case "random":
            return [random.randint(0, size) for _ in range(size)]
        case "sorted":
            return list(range(size))
        case "reverse_sorted":
            return list(range(size, 0, -1))
        case _:
            raise ValueError("Invalid data type")

def measure_sort_time(size, data_type, pivot_strategy):
    data = generate_data(size, data_type)
    start_time = time.time()
    quicksort(data, pivot_strategy)
    return time.time() - start_time

sizes = [10_000, 20_000, 30_000, 40_000, 50_000]
data_types = ["random", "sorted", "reverse_sorted"]
pivot_strategies = ["first", "middle", "random"]

results = {
    strategy: {data_type: [] for data_type in data_types}
    for strategy in pivot_strategies
}

for size in sizes:
    for data_type in data_types:
        for strategy in pivot_strategies:
            results[strategy][data_type].append(measure_sort_time(size, data_type, strategy))

print("\nResults:")
for strategy, data_results in results.items():
    print(f"\nPivot strategy: {strategy}")
    print("Vector Size | Random Numbers | Sorted Numbers | Reverse Sorted")
    print("---------------------------------------------------------")
    for i, size in enumerate(sizes):
        print(
            f"{size:<11} | "
            f"{data_results['random'][i]:<14.6f} | "
            f"{data_results['sorted'][i]:<13.6f} | "
            f"{data_results['reverse_sorted'][i]:<15.6f}"
        )
