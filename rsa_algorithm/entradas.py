def receber_mensagem():
    while(True):
        msg = input("Digite sua mensagem (Compatibilidade com caracteres de dois digitos da ASCII): \n")

        if(msg.strip() != ""):
            break

        print("Digite uma mensagem válida!!")

    return msg.strip().upper()
