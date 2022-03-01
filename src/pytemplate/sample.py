__all__ = ("inc", "is_prime")


def inc(x: int) -> int:
    """Add one to x.

    :param x: Integer to increment by 1
    :type x: int
    :return: New integer 1 greater than x
    :rtype: int
    """
    return x + 1


def is_prime(n: int) -> bool:
    """Determine if `n` is prime.

    Return True if prime, False if not.

    :param n: Integer to determine if prime
    :type x: int
    :return: True if prime, False if not
    :rtype: bool
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
