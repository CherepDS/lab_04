import pytest
import random

from algorithms.sorting import insertion_sort, quick_sort
from algorithms.binary_exponentiation import binary_exp_iterative, binary_exp_recursive
from algorithms.data_generators import generate_random, generate_sorted, generate_reverse, generate_nearly_sorted, generate_duplicates
from algorithms.priority_queue import PriorityQueue


# ---------- Sorting ----------

def test_insertion_sort():
    assert insertion_sort([]) == []
    assert insertion_sort([5]) == [5]
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]
    assert insertion_sort([3, 1, 3, 2]) == [1, 2, 3, 3]
    assert insertion_sort([-5, 2, -1, 0]) == [-5, -1, 0, 2]


def test_quick_sort():
    assert quick_sort([]) == []
    assert quick_sort([5]) == [5]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([1, 2, 3]) == [1, 2, 3]
    assert quick_sort([3, 1, 3, 2]) == [1, 2, 3, 3]
    assert quick_sort([-5, 2, -1, 0]) == [-5, -1, 0, 2]


def test_insertion_sort_does_not_change_original_list():
    arr = [5, 2, 8, 1]
    original = arr.copy()

    result = insertion_sort(arr)

    assert arr == original
    assert result == [1, 2, 5, 8]


def test_quick_sort_does_not_change_original_list():
    arr = [5, 2, 8, 1]
    original = arr.copy()

    result = quick_sort(arr)

    assert arr == original
    assert result == [1, 2, 5, 8]


def test_sort_wrong_input():
    with pytest.raises(TypeError):
        insertion_sort(None)

    with pytest.raises(TypeError):
        quick_sort(None)

# ---------- Binary exponentiation ----------

def test_fast_power_iterative():
    assert binary_exp_iterative(2, 10) == 1024
    assert binary_exp_iterative(3, 4) == 81
    assert binary_exp_iterative(5, 0) == 1
    assert binary_exp_iterative(2, -3) == 0.125
    assert binary_exp_iterative(0, 3) == 0


def test_fast_power_recursive():
    assert binary_exp_recursive(2, 10) == 1024
    assert binary_exp_recursive(3, 4) == 81
    assert binary_exp_recursive(5, 0) == 1
    assert binary_exp_recursive(2, -3) == 0.125
    assert binary_exp_recursive(0, 3) == 0


def test_power_zero_with_negative_exponent():
    with pytest.raises(ZeroDivisionError):
        binary_exp_iterative(0, -1)

    with pytest.raises(ZeroDivisionError):
        binary_exp_recursive(0, -1)


# ---------- Generators ----------

def test_generate_random():
    arr = generate_random(100, -100, 100, seed=42)

    assert len(arr) == 100
    assert all(-100 <= x <= 100 for x in arr)


def test_generate_sorted():
    arr = generate_sorted(100, -100, 100, seed=42)

    assert arr == sorted(arr)


def test_generate_reverse():
    arr = generate_reverse(100, -100, 100, seed=42)

    assert arr == sorted(arr, reverse=True)


def test_generate_nearly_sorted():
    arr = generate_nearly_sorted(100, -100, 100, seed=42)

    assert len(arr) == 100


def test_generate_duplicates():
    arr = generate_duplicates(100, 0, 5, seed=42)

    assert len(arr) == 100
    assert len(set(arr)) <= 6


def test_generators_same_seed():
    assert generate_random(50, 0, 100, seed=42) == generate_random(50, 0, 100, seed=42)
    assert generate_sorted(50, 0, 100, seed=42) == generate_sorted(50, 0, 100, seed=42)
    assert generate_reverse(50, 0, 100, seed=42) == generate_reverse(50, 0, 100, seed=42)
    assert generate_nearly_sorted(50, 0, 100, seed=42) == generate_nearly_sorted(50, 0, 100, seed=42)
    assert generate_duplicates(50, 0, 5, seed=42) == generate_duplicates(50, 0, 5, seed=42)


# ---------- Priority Queue ----------

def test_priority_queue():
    queue = PriorityQueue()

    assert len(queue) == 0
    assert not queue

    queue.put(10)
    queue.put(30)
    queue.put(30)
    queue.put(20)

    assert len(queue) == 4
    assert bool(queue)

    assert queue.get() == 10
    assert queue.get() == 20
    assert queue.get() == 30
    assert queue.get() == 30

    assert len(queue) == 0
    assert not queue


def test_priority_queue_empty():
    queue = PriorityQueue()

    with pytest.raises(IndexError):
        queue.get()

    with pytest.raises(IndexError):
        queue.next()


# ---------- Benchmark ----------

def test_benchmark_settings():
    from algorithms import benchmark

    assert benchmark.REPEATS >= 5
    assert 100 in benchmark.SIZES
    assert 1000 in benchmark.SIZES
    assert 10000 in benchmark.SIZES