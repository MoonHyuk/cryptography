from typing import Optional


def extended_euclidean(numbers: tuple[int, int], s=(1, 0), t=(0, 1)) -> tuple[int, int, int]:
    if numbers[0] < numbers[1]:
        return extended_euclidean(numbers[::-1], t, s)

    if numbers[1] == 0:
        return numbers[0], s[0], t[0]

    q = numbers[0] // numbers[1]

    def __next(inp):
        return inp[1], inp[0] - inp[1] * q

    return extended_euclidean(__next(numbers), __next(s), __next(t))


def mod_add_inverse(a: int, n: int) -> int:
    return -a % n


def mod_multi_inverse(a: int, n: int) -> Optional[int]:
    gcd, s, t = extended_euclidean((a, n))
    if gcd == 1:
        return s % n
    return None
