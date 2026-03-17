from rsa_algorithm import *

def main():
    """
    Uma das três funções principais, responsável pela geração das chaves do algoritmo RSA.

    Neste processo, são gerados dois números primos grandes (p e q),
    que compõem a base da chave privada. A partir deles, calcula-se
    a chave pública n = p * q, além da definição do expoente público.
    """ 

    #Geração de dois números primos com número de bits arbitrário(chaves privadas)
    p = gerar_primo(64)
    q = gerar_primo(64)
    
    #Definição do expoente público padrão
    exp_pub = 65537
    
    #Cálculo da chave pública (n = p * q)
    key_pub = p * q

    #Dilvulgação das chaves para o receptor.
    print(f"As chaves privadas do processo serão:\n\np = {p}\nq = {q}")
    print("\nA chave pública do processo será:", key_pub)
    print("\nO expoente público do processo será:", exp_pub)

main()
