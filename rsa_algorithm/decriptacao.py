from .inverso_modular import *
from .tcr import *

def decriptacao(msg_cod, n, lambd, p, q):
    msg_decod = "" 
    i_lambd = inverso_modular(lambd, (p-1) * (q-1))
    
    for i in range(len(msg_cod)):
        msg_decod += tcrRSA(int(msg_cod[i]), i_lambd, [p,q])
    
    return msg_decod
