def inverso_modular(a, m):
    m0 = m #guarda o valor original do modulo
    y = 0 #segundo coeficiente de bezout
    x = 1 #inverso modular que procuramos

    #objetivo: a*x + m*y = 1
    if m == 1:
        return 0
    while a > 1:
        #q e quociente
        q = a // m
        t = m
        #m e resto
        m = a % m
        a = t
        t = y
        #t variavel temp
        #atualiza x e y
        y = x - q * y
        x = t
    #torna x em positivo
    if x < 0:
        x = x + m0
    return x
