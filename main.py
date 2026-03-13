from rsa_algorithm import *

def main():
   
    tabela = {
        10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',
        17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',
        23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',
        30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z', 99:" "}

    msg = "10222499249915221212"

    p = gerar_primo(256)
    q = gerar_primo(256)

    public_key = p * q
    public_lambd = gerar_expoente((p - 1)*(q - 1))

    msg_blocos = blocagem(msg, public_key)

    msg_codificada = codificacao(msg_blocos, public_key, public_lambd)    
    print("Mensagem codificada:", msg_codificada)

    msg_decodificada = decodificacao(msg_codificada, public_key, public_lambd, p, q)
    print("Mensagem decodificada:", msg_decodificada)
    
    saida = ""
    for i in range(0, len(msg_decodificada), 2):
        num = int(msg_decodificada[i] + msg_decodificada[i+1])
        saida += tabela[num]
    print(saida)

main()
