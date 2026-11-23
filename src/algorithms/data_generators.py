import random


DEFAULT_MIN = -10_000
DEFAULT_MAX = 10_000


def _validate_size(size):
    if not isinstance(size, int) or isinstance(size, bool) or size < 0:
        raise ValueError("Размер должен быть целым положительным числом!")


def _validate_bounds(min_value, max_value):
    if not isinstance(min_value, int) or isinstance(min_value, bool):
        raise TypeError("Нижняя граница должна быть целым положительным числом!")

    if not isinstance(max_value, int) or isinstance(max_value, bool):
        raise TypeError("Верхняя граница должна быть целым положительным числом!")

    if min_value > max_value:
        raise ValueError("Нижняя граница должна быть не бльше верхней границы!")


def _create_random_array(size, min_value, max_value, rng):
    return [rng.randint(min_value, max_value) for _ in range(size)]


def generate_random(
    size,
    min_value=DEFAULT_MIN,
    max_value=DEFAULT_MAX,
    seed=None
):
    _validate_size(size)
    _validate_bounds(min_value, max_value)

    rng = random.Random(seed)

    return _create_random_array(size, min_value, max_value, rng)


def generate_sorted(
    size,
    min_value=DEFAULT_MIN,
    max_value=DEFAULT_MAX,
    seed=None
):
    arr = generate_random(size, min_value, max_value, seed)
    return sorted(arr)


def generate_reverse(
    size,
    min_value=DEFAULT_MIN,
    max_value=DEFAULT_MAX,
    seed=None
):
    arr = generate_random(size, min_value, max_value, seed)
    return sorted(arr, reverse=True)


def generate_nearly_sorted(
    size,
    min_value=DEFAULT_MIN,
    max_value=DEFAULT_MAX,
    seed=None,
    swaps=None
):
    _validate_size(size)
    _validate_bounds(min_value, max_value)

    if swaps is None:
        swaps = size // 100

    if not isinstance(swaps, int) or isinstance(swaps, bool) or swaps < 0:
        raise ValueError("Количество повторов должно быть целым положительным числом!")

    rng = random.Random(seed)

    arr = _create_random_array(size, min_value, max_value, rng)

    arr.sort()

    for _ in range(swaps):
        if size < 2:
            break

        i, j = rng.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def generate_duplicates(
    size,
    min_value=0,
    max_value=5,
    seed=None
):
    return generate_random(size, min_value, max_value, seed)