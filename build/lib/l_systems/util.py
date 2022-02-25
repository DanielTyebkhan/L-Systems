from typing import Callable, Iterable, List


def flat_map(function: Callable, iterable: Iterable) -> List:
    """
    Map to iterable of iterables and return 1 level flattened
    """
    bumpy = list(map(function, iterable))
    return flatten(bumpy)

def flatten(iterable: Iterable) -> List:
    return [item for sublist in iterable for item in sublist]
