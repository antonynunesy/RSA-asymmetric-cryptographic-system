from .blocagem import blocagem

def codificacao(mensagem, n, lambd):
    blocos = blocagem(mensagem, n)
    blocos_cod = []
    
    for i in range(len(blocos)):
        blocos_cod.append(str((int(blocos[i]) ** lambd) % n))
    
    return blocos_cod
