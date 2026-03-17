def mod_exp(base, exp, mod):
    """
    Calcula exponenciação modular de forma eficiente.
    """

    resultado = 1
    base = base % mod

    while exp > 0:
        #Se o expoente for ímpar, multiplica ao resultado
        if exp % 2 == 1:
            resultado = (resultado * base) % mod

        #Eleva a base ao quadrado e reduz pelo modulo
        base = (base * base) % mod
        
        #Divide o expoente por 2
        exp = exp // 2

    return resultado
