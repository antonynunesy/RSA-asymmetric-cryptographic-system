from .inverso_modular import *

def decodificacao(msg_cod, n, lambd):
    p = 17
    q = 23

    msg_decod = "" 
    i_lambd = inverso_modular(lambd, (p-1) * (q-1))
    
    for i in range(len(msg_cod)):
        msg_decod += str(int(msg_cod[i])**i_lambd % (p*q))
    
    return msg_decod
