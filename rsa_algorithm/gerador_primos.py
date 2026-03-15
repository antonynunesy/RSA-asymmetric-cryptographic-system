import random
from .exp_modular import *

def miller_rabin(n, k=50):

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    r = 0

    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)

        x = mod_exp(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def gerar_primo(bits):

    while True:

        n = random.getrandbits(bits)
        n |= (1 << bits - 1) | 1

        if miller_rabin(n):
            return n
