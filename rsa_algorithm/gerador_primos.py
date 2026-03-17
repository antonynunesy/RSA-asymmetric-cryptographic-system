import random
from .exp_modular import *

def miller_rabin(n, k=50):
    """
    Teste probabilístico de primalidade de Miller Rabin.
    """
    
    #Casos base
    if n <= 1 or n % 2 == 0:
        return False
    if n <= 3:
        return True

    #Escreve n-1 como 2^r * d
    d = n - 1
    r = 0

    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        #Gera bases aleatorias para teste.
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

        #Gera um número aleatório com tamanho fixo e ímpar
        n = random.getrandbits(bits)
        n |= (1 << (bits - 1)) | 1
        
        #Testa se esse número é primo.
        if miller_rabin(n):
            return n
