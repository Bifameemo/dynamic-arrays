from typing import Any

type DynamicArray = tuple[list[Any], int, int]
# items, count, capacity


def da_create(xs: list[Any]) -> DynamicArray:
    da_xs = ([None], 0, 1)
    for i in range(len(xs)):
        da_xs = da_append(da_xs, xs[i])
    return da_xs


def da_to_arr(da_xs: DynamicArray) -> list[Any]:
    xs = [None] * _da_count(da_xs)
    for i in range(_da_count(da_xs)):
        xs[i] = _da_items(da_xs)[i]
    return xs


def _da_items(xs: DynamicArray) -> Any:
    return xs[0]


def _da_count(xs: DynamicArray) -> int:
    return xs[1]


def _da_capacity(xs: DynamicArray) -> int:
    return xs[2]


def da_append(xs: DynamicArray, x: Any) -> DynamicArray:
    items = _da_items(xs)
    count = _da_count(xs)
    capacity = _da_capacity(xs)
    if count == capacity:
        # reallocate 2 times the memory
        new_items = [None] * capacity * 2
        for i in range(capacity):
            new_items[i] = items[i]
        new_items[capacity] = x
        return (new_items, count + 1, capacity * 2)
    items[count] = x
    return (items, count + 1, capacity)


def da_extend(xs: DynamicArray, ys: DynamicArray) -> DynamicArray:
    for i in range(_da_count(ys)):
        xs = da_append(xs, _da_items(ys)[i])
    return xs
