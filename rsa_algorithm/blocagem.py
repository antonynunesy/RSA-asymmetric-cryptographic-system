def blocagem(mensagem, n):
    blocos = []
    bloco = ""
    
    for i in range(len(mensagem)):
        if int(bloco + mensagem[i]) > n:
            blocos.append(bloco)
            bloco = mensagem[i]
        else:
            bloco = bloco + mensagem[i]

    blocos.append(bloco)
    return blocos
