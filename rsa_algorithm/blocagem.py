def blocagem(mensagem, n):
    """
    Divide a mensagem numérica em blocos menores que n.
    """

    blocos = []
    bloco = ""
    
    for i in range(len(mensagem)):
        valor = int(bloco + mensagem[i])
        
        #Verifica se o bloco ultrapassa o valor de n
        if valor >= n:
            blocos.append(bloco)
            bloco = mensagem[i]
        else:
            bloco = bloco + mensagem[i]

    #Adiciona o último bloco
    blocos.append(bloco)
    
    return blocos
