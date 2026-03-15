import math

from .inverso_modular import *
from .exp_modular import *

def tcrRSA(mensagem, lambd ,modulos):

    resultado = 0
    razaoM = math.prod(modulos)

    for mod in modulos:
        resto = mod_exp(mensagem, lambd, mod)
        razao = razaoM // mod
        inverso = inverso_modular(razao  % mod, mod)
        resultado = (resultado + inverso * resto * razao) % razaoM

    return str(resultado)
