from rsa_algorithm import *

def main():
    msg = receber_mensagem()

    msg_ascii = ""
    for c in msg:
        msg_ascii += str(ord(c))

    p = gerar_primo(256)
    q = gerar_primo(256)

    public_key = p * q
    public_lambd = gerar_expoente((p - 1)*(q - 1))

    msg_blocos = blocagem(msg_ascii, public_key)

    msg_codificada = codificacao(msg_blocos, public_key, public_lambd)    
    print("Mensagem codificada:", msg_codificada)

    msg_decodificada = decodificacao(msg_codificada, public_key, public_lambd, p, q)
    print("Mensagem decodificada:", msg_decodificada)
    
    saida = ""
    for i in range(0, len(msg_decodificada), 2):
        c = chr(int(msg_decodificada[i] + msg_decodificada[i+1]))
        saida += c
    print(saida)

main()
