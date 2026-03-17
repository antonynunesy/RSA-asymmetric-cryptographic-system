import math

from .inverso_modular import *
from .exp_modular import *

def tcrRSA(mensagem, d, modulos):
    """
    Aplica o Teorema Chinês do Resto na decriptação RSA.
    """

    resultado = 0
    
    #Produto dos módulos (n = p * q)
    razaoM = math.prod(modulos)

    for mod in modulos:
        #Calcula resto da exponenciação modular (mod p ou mod q)
        resto = mod_exp(mensagem, d, mod)
        
        #Calcula os n's
        razao = razaoM // mod
        
        #Calcula inverso modular dos n's
        inverso = inverso_modular(razao % mod, mod)
        
        #Somatório do TCR
        resultado = (resultado + inverso * resto * razao) % razaoM

    return str(resultado)
