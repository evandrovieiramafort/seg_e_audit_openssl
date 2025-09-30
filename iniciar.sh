#!/bin/bash

echo "--- Configurando o Ambiente ---"

echo "1. Criando ambiente virtual 'venv'..."
python3 -m venv venv

echo "2. Ativando o ambiente virtual..."
source venv/bin/activate

echo "Você saberá que funcionou quando vir (venv) no início do terminal."
echo ""

echo "3. Instalando dependências do requirements.txt..."
pip install -r requirements.txt
echo ""

echo "4. Executando o programa principal (main.py)..."
python main.py

echo "--- Programa finalizado. Desativando ambiente virtual. ---"
deactivate
