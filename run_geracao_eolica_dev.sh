#!/bin/zsh

DIR_BASE=$HOME

echo "Esse script se chama $0"
echo "Seu PID: $$"

# Use -e no echo quando deseja utilizar n, t, r ...
# Idem printf do C
echo -e "Voce esta logado com o usuario:\t\t\t\t\t$USER"
echo -e "O diretorio home deste usuario:\t\t\t\t$HOME"
echo -e "O diretorio onde este script esta sendo executado:\t\t$PWD"

STR_CMD_01="cd $HOME/work/geracao-eolica-previsao"
STR_CMD_02="source $HOME/work/geracao-eolica-previsao/.venv/bin/activate"
STR_CMD_03="which python"
STR_CMD_04="python main.py"
echo -e "Comando: \t$STR_CMD_01\n"
eval $STR_CMD_01
echo -e "Comando: \t$STR_CMD_02\n"
eval $STR_CMD_02
echo -e "Comando: $STR_CMD_03"
eval $STR_CMD_03
echo -e "O diretorio onde este script esta sendo executado:\t\t$PWD"
echo "Disparado a execução Geracao Eólica Previsão - Diária..."
eval $STR_CMD_04
echo "Execução deste script finalizada..."
exit 0
