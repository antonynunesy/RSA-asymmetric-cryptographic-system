def blocagem(mensagem, n):
    blocos = []
    bloco = ""
    
    for i in range(len(mensagem)):
        valor  = int(bloco + mensagem[i])
        if valor >= n:
            blocos.append(bloco)
            bloco = mensagem[i]
        else:
            bloco = bloco + mensagem[i]

    blocos.append(bloco)
    return blocos
