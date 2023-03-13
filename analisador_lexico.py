# Bibliotecas para entrada e saida de arquivos
import os.path

# Bliblioteca padrao de string
import string

# Declarando Classe do analisador Lexico
class AnalisadorLexico():
  #Definindo os arquivos de entrada e saída
  def __init__(self):
    self.arquivo_e = "programa.txt"
    self.arquivo_s = "resp-lex.txt"

  # Metodo para mudar arquivo de entrada
  def mudaEntrada(self, string):
    self.arquivo_e = string

  def getEntrada(self):
    return self.arquivo_e

  def getSaida(self):
    return self.arquivo_s

  # Metodo que verifica se a entrada é um delimitador
  def ehDelimitador(self, caracter):
    # String com os delimitadores componentes da linguagem
    delimitadores = ";,(){}[]"
    if caracter in delimitadores:
      return True
    return False

  # Metodo que especifica qual dos tokens delimitadores é a entrada
  def qualTokenDelimitador(self, entrada):
    # String com os operadores componentes da linguagem
    delimitadores = ";,(){}[]"
    posicao = delimitadores.find(entrada)
    return "tok20"+str(posicao)

  # Metodo que verifica se a entrada é uma letra
  def ehLetra (self, caracter):
    # String com as letras (a..z|A..Z)
    letra = string.ascii_letters
    if caracter in letra:
      return True
    return False

  # Metodo que verifica se a entrada é um digito
  def ehDigito (self, caracter):
    # String com os digitos componentes da linguagem
    digito = '0123456789'
    if caracter in digito:
      return True
    return False

  # Metodo que verifica se a entrada é um simbolo
  def ehSimbolo(self, caracter):
    # Strings com os simbolos da tabela ASCII (32 a 126)
    simbolos = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHJKLMNOPQRSTUVXWYZ[\]^_`abcdefghijklmnopqrstuvxwyz{|}~'''
    if(caracter in simbolos):
      return True
    return False

  # Metodo que verifica se a entrada é um operador
  def ehOperador(self, entrada):
    # Listas com os operadores componentes da linguagem
    operadores = '. + - * / ++ -- == != > >= < <= && || ='.split()
    if entrada in operadores:
      return True
    return False
  
  # Metodo que especifica qual dos tokens operadores é a entrada
  def qualTokenOperador(self, entrada):
    # Listas com os operadores componentes da linguagem
    operadores = '. + - * / ++ -- == != > >= < <= && || ='.split()
    posicao = 0
    for x in operadores:
      if x == entrada:
        break
      posicao += 1
    if(posicao > 9):
      return "tok1"+str(posicao)
    else:
      return "tok10"+str(posicao)

# Metodo que verifica se a entrada é uma palavra reservada
  def ehReservada(self, entrada):
    reservadas = "continuar variaveis constantes registro funcao retorno vazio se senao enquanto quebrar leia escreva inteiro real booleano char imprimir verdadeiro falso".split()
    if entrada in reservadas:
      return True
    return False

  # Metodo que especifica qual dos tokens palavras reservadas é a entrada
  def qualTokenReservada(self, entrada):
    reservadas = '''continuar variaveis constantes registro funcao retorno vazio se senao enquanto quebrar leia escreva inteiro real booleano char imprimir verdadeiro falso'''.split()
    posicao = 0
    for x in reservadas:
      if x == entrada:
        break
      posicao += 1
    if(posicao > 9):
      return "tok6"+str(posicao)
    else:
      return "tok60"+str(posicao)

  # Metodo que executa o analsador lexico
  def analisa(self):
    # Abre o arquivo de saida do programa
    arquivo_saida = open(self.arquivo_s, 'w')
    # Verifica se o arquivo de entrada já existe
    if not os.path.exists(self.arquivo_e):
      arquivo_saida.write("Arquivo de entrada inexistente")
      return

    # Abre o arquivo de entrada do programa
    arquivo = open(self.arquivo_e, 'r')

    # Le a primeira linha
    linha_programa = arquivo.readline()

    # Variavel que indica a linha do caracter_atual
    numero_linha = 1
    
    # Percorre o programa linha por linha
    while linha_programa:
      i = 0
      tamanho_linha = len(linha_programa)
      #Percorre os caracteres da linha
      while i < tamanho_linha: 
        caracter_atual = linha_programa[i] 
        caractere_seguinte = None
        # So se pega o caractere_seguinte se ele existe na linha
        if ((i+1) < tamanho_linha):
          caractere_seguinte = linha_programa[i+1] 
        # Verifica se o caracter é um delimitador
        if (self.ehDelimitador(caracter_atual)):
          arquivo_saida.write(self.qualTokenDelimitador(caracter_atual)+'_'+caracter_atual+'->'+str(numero_linha)+'\n')
        # Verificando se o elemento é um operador
        elif caractere_seguinte != None and self.ehOperador(caracter_atual+caractere_seguinte):
          arquivo_saida.write(self.qualTokenOperador(caracter_atual+caractere_seguinte)+'_'+caracter_atual+caractere_seguinte+'->'+str(numero_linha)+'\n')
          i += 1
        elif self.ehOperador(caracter_atual):
          arquivo_saida.write(self.qualTokenOperador(caracter_atual)+'_'+caracter_atual+'->'+str(numero_linha)+'\n')
          
        # Verificando se o elemento em questao é caractere
        
        elif (caracter_atual == "'"):
          if (linha_programa[i+1] == '\n') or (not ("'" in linha_programa[i+1:])):
            arquivo_saida.write('Erro Lexico - Caractere nao fechado - Linha: %d\n' %numero_linha)
            i = tamanho_linha
          elif self.ehSimbolo(linha_programa[i+1]) and linha_programa[i+1] != string.punctuation[6] and linha_programa[i+2] == string.punctuation[6]:
            arquivo_saida.write('tok400_'+linha_programa[i+1]+'->'+str(numero_linha)+'\n')
            i+=2
          elif linha_programa[i+1] == string.punctuation[6] and linha_programa[i+2] == string.punctuation[6]:
            arquivo_saida.write('Erro Lexico - Caractere nao pode ser aspas simples - Linha: %d\n' %numero_linha)
            i+=2
          elif linha_programa[i+1] == string.punctuation[6]:
            arquivo_saida.write('Erro Lexico - Caractere nao pode ser vazio - Linha: %d\n' %numero_linha)
            i+=1
          else:
            arquivo_saida.write('Erro Lexico - Tamanho ou simbolo do Caractere invalido - Linha: %d\n' %numero_linha)
            i=linha_programa[i+1:].find(string.punctuation[6])+1 
            
        # Verificando se o elemento em questao é um numero
        elif (self.ehDigito(caracter_atual)):
          string_temp = caracter_atual
          i += 1
          j = 0
          
          caracter_atual = linha_programa[i]
          while (self.ehDigito(caracter_atual) and (i+1 < tamanho_linha)):
            string_temp += caracter_atual
            i += 1
            caracter_atual = linha_programa[i]
          # Vai contar se o numero tem pelo menos 1 digito depois do '.'
          if (caracter_atual == '.'):
            if ((i+1) < tamanho_linha):
              string_temp += caracter_atual
              i += 1
              caracter_atual = linha_programa[i]
              while self.ehDigito(caracter_atual) and i+1 < tamanho_linha:
                j += 1
                string_temp += caracter_atual
                i += 1
                caracter_atual = linha_programa[i]
                if self.ehDelimitador(caracter_atual) or caracter_atual == ' ':
                    i -= 1 
                    break
                if(caracter_atual == '.'):
                  j = 0
                  while (i+1 < tamanho_linha):
                    i += 1
                    # Preciso voltar um elemento da linha para que o delimitador seja reconhecido no momento certo
                    caracter_atual = linha_programa[i]
                    
                    
            else:
              arquivo_saida.write('Erro Lexico - Numero mal formado - Linha: %d\n' %numero_linha)

            if (j > 0):
              arquivo_saida.write('tok301_'+string_temp+'->'+str(numero_linha)+'\n')
              if(self.ehOperador(caracter_atual)):
                arquivo_saida.write(self.qualTokenOperador(caracter_atual)+'_'+caracter_atual+'->'+str(numero_linha)+'\n')
            else: 
              arquivo_saida.write('Erro Lexico - Numero mal formado - Linha: %d\n' %numero_linha)
          else:
            arquivo_saida.write('tok300_'+string_temp+'->'+str(numero_linha)+'\n')
            if(not self.ehDigito(caracter_atual)):
              i -= 1
        # Verificando identificadores ou palavras reservadas - OK
        elif (self.ehLetra(caracter_atual)):
          # Apos verificar que o primeiro caractere da palavra era uma letra, vou percorrendo o identificador
          # ateh encontrar um caractere que nao possa ser de identificadores ou ateh o final da linha
          string_temp = caracter_atual
          i += 1
          algum_erro = False
          while i < tamanho_linha:
            caractere_seguinte = None
            caracter_atual = linha_programa[i]
            if(i+1 < tamanho_linha):
              caractere_seguinte = linha_programa[i+1]
            if (self.ehLetra(caracter_atual) or self.ehDigito(caracter_atual) or caracter_atual == '_'):
              string_temp += caracter_atual
            elif (self.ehDelimitador(caracter_atual) or caracter_atual == ' ' or caracter_atual == '\t' or caracter_atual == '\r'):
              i -= 1 # Preciso voltar um elemento da linha para que o delimitador seja reconhecido no momento certo
              break
            elif(caractere_seguinte != None and self.ehOperador(caracter_atual+caractere_seguinte)) or self.ehOperador(caracter_atual):
              i-=1
              break
            elif caracter_atual != '\n':
              arquivo_saida.write("Erro Lexico - Identificador com caracter invalido: "+caracter_atual+" - linha: %d\n" %numero_linha)
              algum_erro = True
              break
            i += 1 # Passando o arquivo ate chegar ao final do identificador/palavra reservada
            

          if (algum_erro):
            while (i+1 < tamanho_linha):
              i += 1
              caracter_atual = linha_programa[i]
              if self.ehDelimitador(caracter_atual) or caracter_atual == ' ' or caracter_atual == '\t' or caracter_atual == '\r' or caracter_atual == '/':
                i -= 1 # Preciso voltar um elemento da linha para que o delimitador seja reconhecido no momento certo
                break
          else: # Se nao houver erros basta verificar se o elemento eh palavra reservada tambem
            if (self.ehReservada(string_temp)):
              arquivo_saida.write(self.qualTokenReservada(string_temp)+'_'+string_temp+'->'+str(numero_linha)+'\n')
            else:
              arquivo_saida.write('tok500_'+string_temp+'->'+str(numero_linha)+'\n')
          
        # Verificando Erros Lexicos - Caracter Invalido
        # os caracteres especiais \n, \t, \r e espaco sao desconsiderados como caracteres invalidos
        elif caracter_atual != '\n' and caracter_atual != ' ' and caracter_atual != '\t' and caracter_atual != '\r':
          arquivo_saida.write('Erro Lexico - Caracter Invalido: ' + caracter_atual + ' - linha: %d\n' %numero_linha)
        i += 1 # Incrementando a leitura dos caracteres da linha lida no momento

      linha_programa = arquivo.readline() # Le a proxima linha
      numero_linha += 1
    # Fim do programa
    arquivo_saida.write('$')
    # Fim do arquivo de entrada
    arquivo.close()
    # Fim do arquivo de entrada
    arquivo_saida.close
