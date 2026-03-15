from rsa_algorithm import *

def main():
    p = int(input("Informe a primeira chave privada do processo: "))
    q = int(input("Informe a segunda chave privada do processo: "))
    e = int(input("Informe o expoente público do processo: "))
    msg = input("Informe a mensagem encriptada: ")
    
    msg_encriptada = msg.split("-")

    msg_decriptada = decriptacao(msg_encriptada, (p*q), e, p, q)
    print("\nMensagem decriptada:", msg_decriptada)
    
    saida = ""
    for i in range(0, len(msg_decriptada) - 1, 3):
        c = chr(int(msg_decriptada[i] + msg_decriptada[i+1] + msg_decriptada[i+2]) - 100)
        saida += c
    print(f"\n{saida}")

main()
