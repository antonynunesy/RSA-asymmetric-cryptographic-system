from rsa_algorithm import *

def main():

    p = gerar_primo(64)
    q = gerar_primo(64)
    exp_pub = 65537
    key_pub = p * q

    print(f"As chaves privadas do processo serão:\n\np = {p}\nq = {q}")
    print("\nA chave pública do processo será:", key_pub)
    print("\nO expoente público do processo será:", exp_pub)

main()
