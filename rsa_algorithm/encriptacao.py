from .blocagem import blocagem
from .exp_modular import mod_exp

def encriptacao(mensagem, n, e):
    """
    Realiza a encriptação dos blocos utilizando RSA.
    """

    #Divide a mensagem em blocos menores que n
    blocos = blocagem(mensagem, n)
    blocos_cod = []
    
    for i in range(len(blocos)):
        #Aplica exponenciação binária em cada bloco
        blocos_cod.append(str(mod_exp(int(blocos[i]), e, n)))
    
    return blocos_cod
