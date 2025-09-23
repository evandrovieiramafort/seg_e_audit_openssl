# Sistema de Criptografia com DES em Python
Melhoria do exercício anterior. A implementação original, que utilizava cifras de Transposição e Vigenère, foi modernizada para utilizar o algoritmo DES (Data Encryption Standard).

## Dependências e Requisitos
- Python 3.6 ou superior
- As bibliotecas listadas no arquivo requirements.txt

## Como Executar
Siga os passos abaixo para configurar e rodar o projeto corretamente.

1. Clone o Repositório
Primeiro, clone este repositório para a sua máquina local:
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

Você saberá que funcionou quando vir (venv) no início do seu terminal.

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

Siga as instruções exibidas no menu para cifrar ou decifrar seu texto.

Arquivos no Projeto
main.py: Script principal que contém todo o sistema de criptografia e o menu interativo.

requirements.txt: Arquivo que lista as dependências do projeto.

cifrado.txt: (Gerado) Arquivo que armazena os dados após o processo de cifragem.
