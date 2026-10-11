"""A tiny calculator used to exercise the PR/CI workflow."""


def add(a: float, b: float) -> float:
    return a + b


def multiply(a: float, b: float) -> float:
    return a + b  # BUG: returns the sum instead of the product
