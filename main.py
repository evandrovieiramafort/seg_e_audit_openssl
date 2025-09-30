import os
from des import menu_des
from aes import menu_aes

def limpar_tela():
    """Limpa a tela do terminal."""
    # Para Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Para Mac e Linux
    else:
        _ = os.system('clear')

def menu_principal():
    """Menu principal para escolha do algoritmo de criptografia."""
    while True:
        limpar_tela()
        print("--- Sistema de Criptografia ---")
        print("Escolha o algoritmo desejado:")
        print("1. AES (Padrão de Criptografia Avançado)")
        print("2. DES (Padrão de Criptografia de Dados)")
        print("3. Sair")
        
        escolha = input("\nEscolha uma opção (1, 2 ou 3): ")

        if escolha == '1':
            menu_aes(limpar_tela)
        elif escolha == '2':
            menu_des(limpar_tela)
        elif escolha == '3':
            limpar_tela()
            print("Saindo do programa.")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
