from rsa_algorithm import *

def main():
    msg = receber_mensagem()

    msg_ascii = ""
    for c in msg:
        msg_ascii += str(ord(c))

    p = gerar_primo(256)
    q = gerar_primo(256)

    public_key = p * q
    public_lambd = 65537
    #public_lambd = gerar_expoente((p - 1)*(q - 1))

    msg_blocos = blocagem(msg_ascii, public_key)
    
    msg_codificada = ""
    for c in range(len(msg_blocos)):
        msg_codificada += str(msg_blocos[c])
      
    print("\nMensagem codificada via ASCII:", msg_codificada)
    msg_encriptada = encriptacao(msg_blocos, public_key, public_lambd)    
    
    str_mensagem = ""
    for b in range(len(msg_encriptada)):
        str_mensagem += msg_encriptada[b]
    
    print("\nMensagem encriptada:", str_mensagem)

    msg_decriptada = decriptacao(msg_encriptada, public_key, public_lambd, p, q)
    print("\nMensagem decriptada:", msg_decriptada)
    
    saida = ""
    for i in range(0, len(msg_decriptada), 2):
        c = chr(int(msg_decriptada[i] + msg_decriptada[i+1]))
        saida += c
    print(saida)

main()
