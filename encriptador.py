from rsa_algorithm import *

def main():
    """
    Uma das três funções principais, responsável pelo processo de encriptação.

    O emissor fornece a chave pública (n) e o expoente público (e), além da mensagem
    a ser criptografada. O programa realiza a conversão da mensagem para formato numérico,
    aplica a blocagem e executa a encriptação.
    """

    n = int(input("Informe a chave pública do processo: "))
    e = int(input("Informe o expoente público do processo: "))
    
    msg = receber_mensagem(input("Informe a mensagem a ser encriptada: "))

    msg_ascii = ""
    for c in msg:
        msg_ascii += str(ord(c) + 100)
     
    msg_blocos = blocagem(msg_ascii, n)

    msg_codificada = "-".join(msg_blocos)
    
    #Processo de encriptação da mensagem
    msg_encriptada = encriptacao(msg_blocos, n, e)

    print(f"\nMensagem codificada via ASCII:\n{msg_codificada}")
 
    #Exibição da mensagem final encriptada
    print(f"\nMensagem encriptada:\n{'-'.join(msg_encriptada)}")

main()
