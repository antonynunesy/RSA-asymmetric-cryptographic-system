def receber_mensagem():
    while(True):
        msg = input("Digite sua mensagem (apenas caracteres pertencentes ao alfabeto): \n")

        if(msg.strip() != ""):
            break

        print("Digite uma mensagem válida!!")

    return msg.strip().upper()