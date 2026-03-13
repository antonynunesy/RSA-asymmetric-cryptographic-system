def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gerar_expoente(euler):
    e = 3

    while e < euler:
        if gcd(e, euler) == 1:
            return e
        e += 2
