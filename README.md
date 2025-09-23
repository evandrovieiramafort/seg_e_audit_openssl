# Sistema de Criptografia com DES em Python
Melhoria do exercício anterior. A implementação original, que utilizava cifras de Transposição e Vigenère, foi modernizada para utilizar o algoritmo DES (Data Encryption Standard). **Obviamente** a implementação não foi na mão, sendo utilizada ao invés disso a biblioteca ```pycryptodome```.

## Dependências e Requisitos
- Python 3.6 ou superior
- As bibliotecas listadas no arquivo requirements.txt

## Como Executar

1. Clone o Repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DA_PASTA_DO_PROJETO>
```

2. Crie e Ative um Ambiente Virtual
```bash
python3 -m venv venv
```
3. Ative o ambiente. 

```bash
source venv/bin/activate
```

Você saberá que funcionou quando vir (venv) no início do terminal.

3. Instale as Dependências

Com o ambiente virtual ativo, faça
```bash
pip install -r requirements.txt
```
4. Execute o Programa

Finalmente, execute o script principal:
```bash
python main.py
```

## Arquivos no Projeto
- main.py: Script principal que contém todo o sistema de criptografia e o menu interativo.
- requirements.txt: Arquivo que lista as dependências do projeto.
- cifrado.txt: (Gerado) Arquivo que armazena os dados após o processo de cifragem.
