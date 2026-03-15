from rsa_algorithm import *

def main():
    n = int(input("Informe a chave pública do processo: "))
    e = int(input("Informe o expoente público do processo: "))
    msg = receber_mensagem(input("Informe a mensagem a ser encriptada: "))

    msg_ascii = ""
    for c in msg:
        msg_ascii += str(ord(c) + 100)
     
    msg_blocos = blocagem(msg_ascii, int(n))

    msg_codificada = "-".join(msg_blocos)
    
    msg_encriptada = encriptacao(msg_blocos, n, e)

    print(f"\nMensagem codificada via ASCII:\n{msg_codificada}")
 
    print(f"\nMensagem encriptada:\n{"-".join(msg_encriptada)}")

main()
