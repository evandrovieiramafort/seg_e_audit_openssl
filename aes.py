import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def derivar_chave_aes(senha: str) -> bytes:
    return hashlib.md5(senha.encode('utf-8')).digest()

def cifrar_texto_aes(texto_plano: str, senha: str) -> bytes:
    chave = derivar_chave_aes(senha)

    cifrador = AES.new(chave, AES.MODE_ECB)
    dados_preenchidos = pad(texto_plano.encode('utf-8'), AES.block_size)
    texto_cifrado = cifrador.encrypt(dados_preenchidos)
    return texto_cifrado

def decifrar_dados_aes(dados_cifrados: bytes, senha: str) -> str:
    chave = derivar_chave_aes(senha)
    cifrador = AES.new(chave, AES.MODE_ECB)
    dados_decifrados_preenchidos = cifrador.decrypt(dados_cifrados)
    texto_plano_bytes = unpad(dados_decifrados_preenchidos, AES.block_size)
    return texto_plano_bytes.decode('utf-8')

def menu_aes(limpar_tela_func):
    while True:
        limpar_tela_func()
        print("--- Criptografia AES ---")
        print("1. Cifrar texto")
        print("2. Decifrar texto")
        print("3. Voltar ao menu principal")
        
        escolha = input("\nEscolha uma opção (1, 2 ou 3): ")

        if escolha == '1':
            try:
                limpar_tela_func()
                print("--- Cifragem de Texto (AES) ---")
                texto = input("Digite o texto a ser cifrado: ")
                senha = input("Digite a senha para cifrar (16 caracteres para AES-128): ")

                if not all([texto, senha]):
                    print("\nErro: O texto e a senha são obrigatórios.")
                    input("\nPressione Enter para continuar...")
                    continue

                arquivo_saida = "cifrado_aes.txt"
                dados_cifrados = cifrar_texto_aes(texto, senha)
                with open(arquivo_saida, 'wb') as f:
                    f.write(dados_cifrados)
                
                print(f"\nSucesso! Texto salvo no arquivo '{arquivo_saida}'.")
                print(f"Conteúdo cifrado (bytes): {dados_cifrados}")

            except Exception as e:
                print(f"\nOcorreu um erro ao cifrar: {e}")
            
            input("\nPressione Enter para voltar ao menu...")

        elif escolha == '2':
            try:
                limpar_tela_func()
                print("--- Decifragem de Texto (AES) ---")
                arquivo_entrada = "cifrado_aes.txt"
                senha = input("Digite a senha para decifrar: ")

                if not senha:
                    print("\nErro: A senha é obrigatória.")
                    input("\nPressione Enter para continuar...")
                    continue
                
                with open(arquivo_entrada, 'rb') as f:
                    dados_cifrados = f.read()

                texto_decifrado = decifrar_dados_aes(dados_cifrados, senha)
                
                print("\n--- Processo de Decifragem Concluído ---")
                print(f"Conteúdo cifrado lido: {dados_cifrados}")
                print(f"Texto decifrado: {texto_decifrado}")
                print("-----------------------------------------")

            except FileNotFoundError:
                print(f"\nErro: O arquivo '{arquivo_entrada}' não foi encontrado. Cifre um texto primeiro.")
            except (ValueError, KeyError):
                print("\nErro ao decifrar. A senha pode estar incorreta ou o arquivo corrompido.")
            except Exception as e:
                print(f"\nOcorreu um erro ao decifrar: {e}")

            input("\nPressione Enter para voltar ao menu...")

        elif escolha == '3':
            break
        
        else:
            print("\nOpção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")
