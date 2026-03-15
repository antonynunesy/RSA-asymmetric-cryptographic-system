def mod_exp(base, exp, mod):
    resultado = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            resultado = (resultado * base) % mod

        base = (base * base) % mod
        exp = exp // 2

    return resultado
