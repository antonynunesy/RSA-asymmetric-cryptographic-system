from rsa_algorithm import *

def main():
    public_key = 391
    public_lambd = 3
    msg = "10222499249915221212"
    msg_blocos = blocagem(msg, public_key)

    msg_codificada = codificacao(msg_blocos, public_key, public_lambd)    
    print("Mensagem codificada:", msg_codificada)

    msg_decodificada = decodificacao(msg_codificada, public_key, public_lambd)
    print("Mensagem decodificada:", msg_decodificada)

main()
