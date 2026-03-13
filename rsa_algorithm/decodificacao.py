from .inverso_modular import *
from .exp_modular import *

def decodificacao(msg_cod, n, lambd, p, q):
    msg_decod = "" 
    i_lambd = inverso_modular(lambd, (p-1) * (q-1))
    
    for i in range(len(msg_cod)):
        msg_decod += str(mod_exp(int(msg_cod[i]), i_lambd, n))
    
    return msg_decod
