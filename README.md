# Sistema de Criptografia com DES em Python
Este projeto foi desenvolvido para a disciplina de Segurança e Auditoria de Sistemas. A implementação original, que utilizava cifras de Transposição e Vigenère, foi modernizada para utilizar o algoritmo DES (Data Encryption Standard), um padrão de cifra simétrica em blocos, para fins educacionais.

## Dependências e Requisitos
Para executar o projeto, você precisará de:

- Python 3.6 ou superior
- As bibliotecas listadas no arquivo requirements.txt

Para instalar todas as dependências de uma vez, clone o repositório, navegue até a pasta do projeto pelo terminal e execute o seguinte comando:

```bash
pip install -r requirements.txt
```

## Funcionalidades
O projeto foi unificado em um único script interativo, o main.py, que faz o seguinte:

- Cifra texto: Solicita que o usuário digite um texto e uma senha. O conteúdo criptografado é salvo automaticamente no arquivo cifrado.txt.
- Decifra texto: Solicita a senha, lê automaticamente o arquivo cifrado.txt e exibe o texto original diretamente na tela do terminal.
- Sair: Encerra a execução do programa.

## Como Executar
Certifique-se de ter o Python 3 e o pip instalados.
Clone este repositório para a sua máquina.
Abra um terminal na pasta do projeto e instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o script principal no terminal:

```bash
python main.py
```

Siga as instruções exibidas no menu para cifrar ou decifrar seu texto.


Arquivos no Projeto
main.py: Script principal que contém todo o sistema de criptografia e o menu interativo.

requirements.txt: Arquivo que lista as dependências do projeto.

cifrado.txt: (Gerado) Arquivo que armazena os dados após o processo de cifragem.
