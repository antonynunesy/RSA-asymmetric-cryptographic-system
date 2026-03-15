from .blocagem import blocagem
from .exp_modular import mod_exp

def encriptacao(mensagem, n, lambd):
    blocos = blocagem(mensagem, n)
    blocos_cod = []
    
    for i in range(len(blocos)):
        blocos_cod.append(str(mod_exp(int(blocos[i]), lambd, n)))
    
    return blocos_cod
