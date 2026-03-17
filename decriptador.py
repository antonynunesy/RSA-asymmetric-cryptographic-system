from rsa_algorithm import *

def main():
    """
    Uma das três funçẽs principais, responsável por executar o processo de decriptação
    utilizando o algoritmo RSA.

    O receptor ira fornecer os parâmetros que ele possui (p, q e e), além da
    mensagem criptografada. O programa realiza a decriptação e converte
    o resultado numérico de volta para caracteres ASCII.
    """

    #Entrada dos parâmetros para decriptação.
    p = int(input("Informe a primeira chave privada do processo: "))
    q = int(input("Informe a segunda chave privada do processo: "))
    e = int(input("Informe o expoente público do processo: "))
    msg = input("Informe a mensagem encriptada: ")
    
    #A mensagem criptografada é separada em blocos
    msg_encriptada = msg.split("-")

    #n é calculado como o produto de p e q
    msg_decriptada = decriptacao(msg_encriptada, (p * q), e, p, q)
    
    print("\nMensagem decriptada:", msg_decriptada)
    
    #Conversão da mensagem numérica para caracteres ASCII
    #Cada conjunto de 3 dígitos representam um caractere da tabela.
    saida = ""
    for i in range(0, len(msg_decriptada) - 1, 3):
        valor_ascii = int(msg_decriptada[i] + msg_decriptada[i+1] + msg_decriptada[i+2]) - 100
        c = chr(valor_ascii)
        saida += c

    print(f"\nMensagem final: {saida}")

main()
