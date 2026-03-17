def receber_mensagem(msg):
    """
    Garante que a mensagem de entrada não esteja vazia.
    """

    while True:
        #Verifica se a mensagem possui conteúdo válido
        if msg.strip() != "":
            break
        
        msg = input("Digite uma mensagem válida!! ")

    return msg.strip()
