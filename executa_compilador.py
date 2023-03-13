# Importando arquivos contendo analisadores
from analisador_lexico import AnalisadorLexico
from analisador_sintatico import AnalisadorSintatico

# Realizando etapa de analise lexica
lexico = AnalisadorLexico()
lexico.analisa()
# Realizando etapa de analise sintatica
AnalisadorSintatico.start()

