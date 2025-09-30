# Sistema de Criptografia com DES em Python
Melhoria do exercício anterior. Além do uso do algoritmo DES (Data Encryption Standard), agora há o uso do algoritmo AES (Advanced Encryption Standard). **Obviamente** a implementação não foi na mão, sendo utilizada ao invés disso a biblioteca ```pycryptodome``` para ambas as funcionalidades.


## Como Executar


Execute os 
```bash
git clone <repositorio>
cd <repositorio>
mkdir <repositorio>
./iniciar.sh
```

**Atenção**: Se o comando ```./iniciar.sh``` resultar em um "permission denied", use ```chmod +x iniciar.sh``` pra garantir permissão de execução do arquivo.


## Arquivos no Projeto
- main.py: Script principal que contém todo o sistema de criptografia e o menu interativo.
- requirements.txt: Arquivo que lista as dependências do projeto.
- cifrado.txt: (Gerado) Arquivo que armazena os dados após o processo de cifragem.
- aes.py: arquivo contendo o sistema de criptografia e descriptografia AES.
- des.py: arquivo contendo o sistema de criptografia e descriptografia DES.
