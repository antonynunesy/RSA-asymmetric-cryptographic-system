from .inverso_modular import *
from .tcr import *

def decriptacao(msg_cod, n, e, p, q):
    """
    Realiza a decriptação dos blocos utilizando o TCR.
    """

    msg_decod = ""
    
    #Calcula o expoente privado (inverso modular de e)
    d = inverso_modular(e, (p - 1) * (q - 1))
    
    for i in range(len(msg_cod)):
        #Aplica decriptação otimizada com Teorema Chinês do Resto
        msg_decod += tcrRSA(int(msg_cod[i]), d, [p, q])
    
    return msg_decod
