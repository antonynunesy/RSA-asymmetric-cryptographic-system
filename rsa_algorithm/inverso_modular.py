def inverso_modular(a, m):
    """
    Calcula o inverso modular utilizando o algoritmo de Euclides estendido.
    """

    m0 = m#Armazena o valor original do módulo
    y = 0
    x = 1#Resultado (inverso modular)

    #Caso base.
    if m == 1:
        return 0

    while a > 1:
        #Calcula quociente da divisão
        q = a // m

        #Atualiza valores com t sendo temporaria
        t = m
        m = a % m
        a = t

        #Atualiza os coeficientes de Bézout
        t = y
        y = x - q * y
        x = t

    #Garante resultado positivo somando o modulo
    if x < 0:
        x = x + m0

    return x
