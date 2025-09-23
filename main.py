import hashlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def derivar_chave(senha: str) -> bytes:
    """Deriva uma chave de 8 bytes a partir da senha usando MD5."""
    return hashlib.md5(senha.encode('utf-8')).digest()[:8]

def cifrar_texto(texto_plano: str, senha: str) -> bytes:
    """Criptografa um texto usando a senha e retorna os bytes cifrados."""
    chave = derivar_chave(senha)
    cifrador = DES.new(chave, DES.MODE_ECB)
    dados_preenchidos = pad(texto_plano.encode('utf-8'), DES.block_size)
    texto_cifrado = cifrador.encrypt(dados_preenchidos)
    return texto_cifrado

def decifrar_dados(dados_cifrados: bytes, senha: str) -> str:
    """Decifra os bytes usando a senha e retorna o texto original."""
    chave = derivar_chave(senha)
    cifrador = DES.new(chave, DES.MODE_ECB)
    dados_decifrados_preenchidos = cifrador.decrypt(dados_cifrados)
    texto_plano_bytes = unpad(dados_decifrados_preenchidos, DES.block_size)
    return texto_plano_bytes.decode('utf-8')

def menu_principal():
    """Exibe o menu principal e gerencia as ações do usuário."""
    while True:
        print("\n--- Sistema de Criptografia DES ---")
        print("1. Cifrar texto")
        print("2. Decifrar texto")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1, 2 ou 3): ")

        if escolha == '1':
            try:
                texto = input("Digite o texto a ser cifrado: ")
                senha = input("Digite a senha para cifrar: ")

                if not all([texto, senha]):
                    print("\nErro: O texto e a senha são obrigatórios.")
                    continue

                arquivo_saida = "cifrado.txt"
                dados_cifrados = cifrar_texto(texto, senha)
                with open(arquivo_saida, 'wb') as f:
                    f.write(dados_cifrados)
                
                print(f"\nSucesso! Texto salvo no arquivo '{arquivo_saida}'.")
                # Exibe o texto cifrado em tela
                print(f"Conteúdo cifrado (bytes): {dados_cifrados}")

            except Exception as e:
                print(f"Ocorreu um erro ao cifrar: {e}")

        elif escolha == '2':
            try:
                arquivo_entrada = "cifrado.txt"
                senha = input("Digite a senha para decifrar: ")

                if not senha:
                    print("\nErro: A senha é obrigatória.")
                    continue
                
                with open(arquivo_entrada, 'rb') as f:
                    dados_cifrados = f.read()

                texto_decifrado = decifrar_dados(dados_cifrados, senha)
                
                # Exibe o conteúdo cifrado e o decifrado
                print("\n--- Processo de Decifragem Concluído ---")
                print(f"Conteúdo cifrado lido do arquivo: {dados_cifrados}")
                print(f"Texto decifrado: {texto_decifrado}")
                print("-----------------------------------------")

            except FileNotFoundError:
                print(f"\nErro: O arquivo '{arquivo_entrada}' não foi encontrado. Cifre um texto primeiro.")
            except (ValueError, KeyError):
                print("\nErro ao decifrar. A senha pode estar incorreta ou o arquivo corrompido.")
            except Exception as e:
                print(f"Ocorreu um erro ao decifrar: {e}")

        elif escolha == '3':
            print("Saindo do programa.")
            break
        
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    menu_principal()