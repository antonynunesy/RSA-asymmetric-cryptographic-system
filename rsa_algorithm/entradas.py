def receber_mensagem(msg):
    
    while(True):
        if(msg.strip() != ""):
            break
        msg = input("Digite uma mensagem válida!! ")

    return msg.strip()
