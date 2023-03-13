# Biblioteca para entrada e saida de arquivos
import os.path


class AnalisadorSintatico():
    tokens = ""
    i = 0
   
    def start():
        arquivo_entrada = "resp-lex.txt"
        arquivo_saida = "resp-sint.txt"

        arquivo_saida = open(arquivo_saida, 'w')
        # Verifica se o arquivo de entrada existe no diretorio em questao
        if not os.path.exists(arquivo_entrada):
            print("Arquivo de entrada inexistente")
            arquivo_saida.write("Arquivo de entrada inexistente")
        
        # Abre o arquivo de entrada do programa
        arquivo = open(arquivo_entrada, 'r')
        tokens = arquivo.readlines()
        arquivo.close()
        i = 0
        vetor_erro=[]
        linha_atual = ""
        vetor_params=[]
        vetor_se=[]
        vetor_func=[]
        vetor_verif_se=[]
        vetor_enquanto=[]
        vetor_chamada=[]
        
        
        while (tokens[i] != "$"):
            
        
            if ("Erro Lexico" in tokens[i]):
                i += 1
                
            
            # verifica as atribuições dos tipos primitivos
            def verifica_atribuicao(i, tokens, tipo):
                # verifica o tipo inteiro
                if ("inteiro" in tipo[1]):
                    #verifica se realmente é um numero inteiro
                    i+=1
                    if (("tok300" in tokens[i]) == False):
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print(
                            "Erro sintatico - Esperado um número inteiro - linha: "+str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                            "Erro sintatico - Esperado um numero inteiro - linha: "+str(linha_atual[1])+"\n")
                        return i
                    
                    #verifica a existencia de um operador
                    elif("tok101" in tokens[i+1] or 
                         "tok102" in tokens[i+1] or 
                         "tok103" in tokens[i+1] or 
                         "tok104" in tokens[i+1]):

                        i+=1
                        #verifica atribuição  compostas
                        if("tok300" in tokens[i+1] or
                           "tok500" in tokens[i+1]):
                            i+=2
                        
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print(
                            "Erro sintatico - Esperado um número inteiro ou identificador depois do operador - linha: "+str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                            "Erro sintatico - Esperado um numero inteiro ou identificador depois do operador - linha: "+str(linha_atual[1])+"\n")
                        return i
                # verifica o tipo real
                elif ("real" in tipo[1]):
                    i+=1
                    if (("tok301" in tokens[i]) == False):
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print(
                            "Erro sintatico - Esperado um numero real - linha: "+str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                            "Erro sintatico - Esperado um número real - linha: "+str(linha_atual[1])+"\n")
                        return i
                    
                    #verifica a existencia de um operador
                    elif("tok101" in tokens[i+1] or 
                         "tok102" in tokens[i+1] or 
                         "tok103" in tokens[i+1] or 
                         "tok104" in tokens[i+1]):
                        i+=1
                        #verifica atribuição  compostas
                        if("tok301" in tokens[i+1] or
                           "tok500" in tokens[i+1]):
                            i+=2
                            
                        
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print(
                            "Erro sintatico - Esperado um número real ou identificador depois do operador - linha: "+str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                            "Erro sintatico - Esperado um numero real ou identificador depois do operador - linha: "+str(linha_atual[1])+"\n")
                        return i
                # verifica o tipo char
                elif ("char" in tipo[1]):
                    i+=1
                    if (("tok400" in tokens[i]) == False):
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print(
                            "Erro sintatico - Esperado um caractere - linha: "+str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                            "Erro sintatico - Esperado um caractere - linha: "+str(linha_atual[1])+"\n")
                        return i
                # verifica o tipo booleano
                elif ("booleano" in tipo[1]):
                    i+=1
                    if (("tok618" in tokens[i] or "tok619" in tokens[i]) == False):
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print(
                            "Erro sintatico - Esperado verdadeiro ou falso - linha: "+str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                            "Erro sintatico - Esperado verdaeiro ou falso - linha: "+str(linha_atual[1])+"\n")
                        return i
                return i
                
            
            def verifica_expressao_bool(i,tokens):
                #verifica se existe um indentificador dentro do se
                if("tok500" in tokens[i]):
                    i+=1
                    #verifica se existe um operador lógico
                    if("tok107" in tokens[i] or
                        "tok108" in tokens[i] or
                        "tok109" in tokens[i] or
                        "tok110" in tokens[i] or
                        "tok111" in tokens[i] or
                        "tok112" in tokens[i]):
                                      
                        i+=1
                        #verifica se existe alguma atribuicao logica válida
                        if("tok500" in tokens[i] or 
                            "tok300" in tokens[i] or
                            "tok301" in tokens[i] or
                            "tok400" in tokens[i] or
                            "tok618" in tokens[i] or
                            "tok619" in tokens[i]):
                            i+=1
                                                                                            
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print(
                            "Erro sintatico - Comparação logica invalida - linha: "+str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                                "Erro sintatico - Comparação logica invalida - linha: "+str(linha_atual[1])+"\n")
                                    
                #verifica se existe um numero    
                elif("tok3" in tokens[i]):
                    i+=1
                                        
                    #verifica se existe um operador lógico
                    if("tok107" in tokens[i] or
                    "tok108" in tokens[i] or
                    "tok109" in tokens[i] or
                    "tok110" in tokens[i] or
                    "tok111" in tokens[i] or
                    "tok112" in tokens[i]):
                                            
                        i+=1
                        #verifica se existe alguma atribuicao logica válida
                        if("tok500" in tokens[i] or 
                        "tok300" in tokens[i] or
                        "tok301" in tokens[i]):
                            i+=1
                                                
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print(
                            "Erro sintatico - Comparação logica invalida - linha: "+str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                            "Erro sintatico - Comparação logica invalida - linha: "+str(linha_atual[1])+"\n")
                                    
                #verifica se existe verdadeiro ou falso na comparação do se
                elif("tok619" in tokens[i] or "tok618" in tokens[i]):
                    i+=1
                                        
                    #verifica se existe um operador lógico
                    if("tok107" in tokens[i] or
                    "tok108" in tokens[i]):
                        i+=1
                                            
                        #verifica se existe alguma atribuicao logica válida
                        if("tok500" in tokens[i] or 
                        "tok619" in tokens[i] or
                        "tok618" in tokens[i]):
                            i+=1
                                            
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print(
                            "Erro sintatico - Comparação logica invalida - linha: "+str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                            "Erro sintatico - Comparação logica invalida - linha: "+str(linha_atual[1])+"\n")
                
                vetor_se.append(i)     
                                                   
            def tipo_primitivo(i,tokens):
              
              # verificando se existe tipo primitivo
                if ('tok614_real' in tokens[i] or
                'tok613_inteiro' in tokens[i] or
                'tok616_char' in tokens[i] or
                'tok615_booleano' in tokens[i]):
                    tipo = tokens[i].split("_")
                    # verificando se existe um indentificador
                    if ("tok500_" in tokens[i+1]):
                        i += 1
                        # verificando se existe sinal de =
                        if ("tok115" in tokens[i+1]):

                            i += 1
                            i = verifica_atribuicao(i, tokens, tipo)
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print(
                                "Erro sintatico - Esperado um sinal de = - linha: "+str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                                "Erro sintatico - Esperado um sinal de = - linha: "+str(linha_atual[1])+"\n")
                    else:
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print(
                            "Erro sintatico - Esperado um indentificador - linha: "+str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                            "Erro sintatico - Esperado um indentificador - linha: "+str(linha_atual[1])+"\n")
            
            def  verifica_params(i,tokens):
                #verifica se existe um tipo adequado como parametro
                if("tok500" in tokens[i] or
                   "tok613" in tokens[i] or
                   "tok614" in tokens[i] or
                   "tok615" in tokens[i]):
                    i+=1
                    #verifica se existe indentificador
                    if("tok500" in tokens[i]):
                        i+=1
                        
                        #verifica se existe ,
                        if("tok201" in tokens[i]):
                            i+1
                            #verifica se existe )
                            if("tok203" in tokens[i]):
                                vetor_erro.append(False)
                                linha_atual = tokens[i].split("->")
                                print("Erro sintatico - Esperado um parametros apos a , - linha: " +str(linha_atual[1])+"\n")
                                arquivo_saida.write(
                                "Erro sintatico - Esperado um parametros apos a , - linha: "+str(linha_atual[1])+"\n")
                            else:
                                #se existir executa a função dnv
                                vetor_params.clear
                                verifica_params(i,tokens)
                                i=vetor_params[len(vetor_params)-1]
                    vetor_params.append(i)
                              
                
                vetor_params.append(i)
                
            def verifica_se(i,tokens,func):
                #verifica se tem if(no caso se)
                            novamente=func
                            if("tok607" in tokens[i]):
                                
                                i+=1
                                #verifica se existe um (
                                if("tok202" in tokens[i]):
                                    i+=1
                                    vetor_se.clear
                                    verifica_expressao_bool(i,tokens)
                                    
                                    i=vetor_se[len(vetor_se)-1]
                                     #verifica a existencia do )
                                    if ("tok203" in tokens[i]):
                                        i+=1
                                        #verifica a existencia do {
                                        if ("tok204" in tokens[i]):
                                            i += 1
                                            #executa por enquando que não encontrar }
                                            while (("tok205" in tokens[i]) != True):
                                                if(func):
                                                    verifica_retorno(i,tokens)
                                                tipo_primitivo(i,tokens)
                                                if("tok607" in tokens[i]):
                                                    vetor_verif_se.clear
                                                    verifica_se(i,tokens,novamente)
                                                    i=vetor_verif_se[len(vetor_verif_se)-1]
                                                i+=1
                                            i+=1
                                            vetor_verif_se.append(i)
                                            
                                            
                                            #verifica a existencia do senao
                                            if("tok608" in tokens[i]):
                                                i+=1
                                                #verifica a existencia do {
                                                if("tok204" in tokens[i]):
                                                    i+=1
                                                    #executa por enquando que não encontrar }
                                                    while (("tok205" in tokens[i]) != True):
                                                        
                                                        tipo_primitivo(i,tokens)
                                                        if("tok607" in tokens[i]):
                                                            vetor_verif_se.clear
                                                            verifica_se(i,tokens,novamente)
                                                            i=vetor_verif_se[len(vetor_verif_se)-1]
                                                        i+=1
                                                    i+=1
                                                    vetor_verif_se.append(i)
                                                    return i
                                    
                                              
                        
                                    else:
                                        vetor_erro.append(False)
                                        linha_atual = tokens[i].split("->")
                                        print("Erro sintatico - Esperado um ) - linha: " +str(linha_atual[1])+"\n")
                                        arquivo_saida.write(
                                        "Erro sintatico - Esperado um ) - linha: "+str(linha_atual[1])+"\n")       
                                                            
                                else:
                                    vetor_erro.append(False)
                                    linha_atual = tokens[i].split("->")
                                    print(
                                        "Erro sintatico - Esperado um ( depois do se- linha: "+str(linha_atual[1])+"\n")
                                    arquivo_saida.write(
                                        "Erro sintatico - Esperado um ( depois do se- linha: "+str(linha_atual[1])+"\n")
                                                          
                            i+=1
            #verifica o corpo da funcao
            def verifica_func(i, tokens):
                vetor_params.clear
                verifica_params(i,tokens)
                i=vetor_params[len(vetor_params)-1]
                
                #verifica a existencia do )
                if ("tok203" in tokens[i]):
                    i += 1
                    #verifica a existencia do {
                    if ("tok204" in tokens[i]):
                        i += 1
                        #executa por enquando que não encontrar }
                        while (("tok205" in tokens[i]) != True):
                            tipo_primitivo(i,tokens)
                            verifica_senao(i,tokens)
                            verifica_retorno(i,tokens)
                            vetor_func.append(i)      
                            #verifica se tem if(no caso se)
                            if("tok607" in tokens[i]):
                                
                                i+=1
                                #verifica se existe um (
                                if("tok202" in tokens[i]):
                                    i+=1
                                    vetor_se.clear
                                    verifica_expressao_bool(i,tokens)
                                    
                                    i=vetor_se[len(vetor_se)-1]
                                     #verifica a existencia do )
                                    if ("tok203" in tokens[i]):
                                        i+=1
                                        #verifica a existencia do {
                                        if ("tok204" in tokens[i]):
                                            i += 1
                                            #executa por enquando que não encontrar }
                                            while (("tok205" in tokens[i]) != True):
                                                vetor_verif_se.clear
                                                #verifica se dentro de se
                                                if("tok607" in tokens[i]):
                                                    vetor_verif_se.clear
                                                    verifica_se(i,tokens,True)
                                                    i=vetor_verif_se[len(vetor_verif_se)-1]
                                                
                                                if("tok609" in tokens[i]):
                                                    vetor_enquanto.clear
                                                    verifica_enquanto(i,tokens,True)
                                                    i=vetor_enquanto[len(vetor_enquanto)-1]
                                                
                                                tipo_primitivo(i,tokens)
                                                verifica_retorno(i,tokens)
                                                i+=1
                                            i+=1
                                            
                                            #verifica a existencia do senao
                                            if("tok608" in tokens[i]):
                                                i+=1
                                                #verifica a existencia do {
                                                if("tok204" in tokens[i]):
                                                    i+=1
                                                    #executa por enquando que não encontrar }
                                                    while (("tok205" in tokens[i]) != True):
                                                        tipo_primitivo(i,tokens)
                                                        verifica_retorno(i,tokens)
                                                        if("tok607" in tokens[i]):
                                                            vetor_verif_se.clear
                                                            verifica_se(i,tokens,True)
                                                            i=vetor_verif_se[len(vetor_verif_se)-1]
                                                        i+=1
                                                    i+=1
                                              
                        
                                    else:
                                        vetor_erro.append(False)
                                        linha_atual = tokens[i].split("->")
                                        print("Erro sintatico - Esperado um ) - linha: " +str(linha_atual[1])+"\n")
                                        arquivo_saida.write(
                                        "Erro sintatico - Esperado um ) - linha: "+str(linha_atual[1])+"\n")       
                                                            
                                else:
                                    vetor_erro.append(False)
                                    linha_atual = tokens[i].split("->")
                                    print(
                                        "Erro sintatico - Esperado um ( depois do se- linha: "+str(linha_atual[1])+"\n")
                                    arquivo_saida.write(
                                        "Erro sintatico - Esperado um ( depois do se- linha: "+str(linha_atual[1])+"\n")
                                                          
                            i+=1
                    else:
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print(
                            "Erro sintatico - Esperado um { - linha: "+str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                            "Erro sintatico - Esperado um { - linha: "+str(linha_atual[1])+"\n")
                else:
                    vetor_erro.append(False)
                    linha_atual = tokens[i].split("->")
                    print("Erro sintatico - Esperado um ) - linha: " +str(linha_atual[1])+"\n")
                    arquivo_saida.write(
                        "Erro sintatico - Esperado um ) - linha: "+str(linha_atual[1])+"\n")

            def verifica_retorno(i,tokens):
                #verifica se existe retorno
                if("tok605" in tokens[i]):
                    i+=1
                    #verifica o tipo de retorno 
                    if("tok500" in tokens[i] or
                       "tok618" in tokens[i] or
                       "tok619" in tokens[i] or
                       "tok606" in tokens[i]):
                        
                        i+=1
                        #verifica se existe ;
                        if("tok200" in tokens[i]):
                            i+=1
                        
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print("Erro sintatico - Esperado um ) - linha: " +str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                            "Erro sintatico - Esperado um ) - linha: "+str(linha_atual[1])+"\n")

                    else:
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print("Erro sintatico - Retorno invalido, Esperado um indentificador ou um booleano, ou vazio - linha: " +str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                                    "Erro sintatico - Retorno invalido, Esperado um indentificador ou um booleano, ou vazio - linha: "+str(linha_atual[1])+"\n")
            
            def verifica_imprimir(i,tokens):
                #verifica se existe o token imprimir
                if("tok617" in tokens[i]):
                    i=i+1
                    #verifica se existe (
                    if("tok202" in tokens[i]):
                        i+=1
                        #verifica se o conteudo do imprimir é válido
                        if("tok500" in tokens[i] or
                           "tok3" in tokens[i] or
                           "tok618" in tokens[i] or
                           "tok619" in tokens[i]):
                            i+=1
                            
                            #verifica se existe )
                            if("tok203" in tokens[i]):
                                i+=1
                            
                            else:
                                vetor_erro.append(False)
                                linha_atual = tokens[i-1].split("->")
                                print("Erro sintatico - Esperado um ) - linha: " +str(linha_atual[1])+"\n")
                                arquivo_saida.write(
                                    "Erro sintatico - Esperado um ) - linha: "+str(linha_atual[1])+"\n")
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print("Erro sintatico - Conteudo do imprimir invalido - linha: " +str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                                    "Erro sintatico - Conteudo do imprimir invalido- linha: "+str(linha_atual[1])+"\n")
 
                    else:
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print("Erro sintatico - Esperado um ( - linha: " +str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                        "Erro sintatico - Esperado um ( - linha: "+str(linha_atual[1])+"\n")
                        
             
                            
            
            def verifica_chamada(i,tokens):
                #verifica se existe um indentificador
                if("tok500" in tokens[i]):
                    i+=1
                    #verifica se existe (
                    if("tok202" in tokens[i]):
                        i+=1
                        #verifica se existe parametros
                        vetor_params.clear
                        verifica_params(i,tokens)
                        i=vetor_params[len(vetor_params)-1]
                        
                        
                        #verifica a existencia do )
                        if ("tok203" in tokens[i]):
                            i += 1
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print("Erro sintatico - Esperado um ( - linha: " +str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                            "Erro sintatico - Esperado um ( - linha: "+str(linha_atual[1])+"\n")
                            
                    vetor_chamada.append(i)
                        
            
            def verifica_enquanto(i,tokens,func):
                novamente=func
                #verifica se existe um enquanto
                if("tok609" in tokens[i]):
                    i+=1
                    #verifica se existe (
                    if("tok202" in tokens[i]):
                        i+=1
                        vetor_se.clear()
                        verifica_expressao_bool(i,tokens)
                        i=vetor_se[len(vetor_se)-1]
                        
                        #verifica a existencia do )
                        if ("tok203" in tokens[i]):
                            i+=1
                            
                            #verifica a existencia do {
                            if("tok204" in tokens[i]):
                                i+=1
                                #executa por enquando que não encontrar }
                                while (("tok205" in tokens[i]) != True):
                                    if(func):
                                        verifica_retorno(i,tokens)
                                    tipo_primitivo(i,tokens)
                                    verifica_senao(i,tokens)
                                    
                                    #verifica se existe outro enquanto
                                    if("tok609" in tokens[i]):
                                        vetor_enquanto.clear
                                        verifica_enquanto(i,tokens,novamente)
                                        i=vetor_enquanto[len(vetor_enquanto)-1]
                                                
                                    #verifica se existe se
                                    if("tok607" in tokens[i]):
                                        vetor_verif_se.clear
                                        verifica_se(i,tokens)
                                        i=vetor_verif_se[len(vetor_verif_se)-1]
                                        
                                        i+=1
                                    i+=1
                                vetor_enquanto.append(i)  
                            else:
                                vetor_erro.append(False)
                                linha_atual = tokens[i].split("->")
                                print("Erro sintatico - Esperado um { - linha: " +str(linha_atual[1])+"\n")
                                arquivo_saida.write(
                                "Erro sintatico - Esperado um { - linha: "+str(linha_atual[1])+"\n")  
             
                        
                        else:
                            vetor_erro.append(False)
                            linha_atual = tokens[i].split("->")
                            print("Erro sintatico - Esperado um ) - linha: " +str(linha_atual[1])+"\n")
                            arquivo_saida.write(
                            "Erro sintatico - Esperado um ) - linha: "+str(linha_atual[1])+"\n")  
                vetor_enquanto.append(i)
            def verifica_quebrar(i,tokens):
                #verifica se existe e quebrar fora de um laço
                if("tok610" in tokens[i] ):
                    vetor_erro.append(False)
                    linha_atual = tokens[i].split("->")
                    print("Erro sintatico - Esperado quebrar dentro de um laco - linha: " +str(linha_atual[1])+"\n")
                    arquivo_saida.write(
                            "Erro sintatico - Esperado quebrar dentro de um laco - linha: "+str(linha_atual[1])+"\n")
            
            def verifica_continuar(i,tokens,loop):
                if(loop != True):
                
                    #verifica se existe continuar fora de um laço
                    if("tok600" in tokens[i]):
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print("Erro sintatico - Esperado continuar dentro de um laco - linha: " +str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                                "Erro sintatico -Esperado continuar dentro de um laco - linha: "+str(linha_atual[1])+"\n") 
                
            def verifica_senao(i,tokens):
                #verifica se existe um senao
                if("tok608" in tokens[i]):
                    vetor_erro.append(False)
                    linha_atual = tokens[i].split("->")
                    print("Erro sintatico - Esperado senao apos um se - linha: " +str(linha_atual[1])+"\n")
                    arquivo_saida.write(
                            "Erro sintatico -Esperado senao apos um se - linha: "+str(linha_atual[1])+"\n") 
            
            verifica_continuar(i,tokens,False)
            verifica_quebrar(i,tokens)
            if("tok500" in tokens[i]):
                vetor_chamada.clear()
                verifica_chamada(i,tokens)
                i=vetor_chamada[len(vetor_chamada)-1]
                       
            tipo_primitivo(i,tokens)
            verifica_imprimir(i,tokens)
            
            if("tok607" in tokens[i]):
                vetor_verif_se.clear()
                verifica_se(i,tokens,False)
                i=vetor_verif_se[len(vetor_verif_se)-1]
            
            verifica_senao(i,tokens)
            
            if("tok609" in tokens[i]):
                vetor_enquanto.clear()
                verifica_enquanto(i,tokens,False)
                i=vetor_enquanto[len(vetor_enquanto)-1]
            
            
                 
            # verifica a funcao
            if ("tok604_funcao" in tokens[i]):
                i += 1
                # verifica se tem espaço entre a declaracao e o indentificador da funcao
                if ("tok606_vazio" in tokens[i]):
                    i += 1
                    # verifica sem tem indentificador apos o espaco
                    if ("tok500_" in tokens[i]):
                        i += 1
                        # verifica se existe parenteses apos o indentificador
                        if ("tok202_" in tokens[i]):
                            i += 1
                            vetor_func.clear
                            verifica_func(i, tokens)
                            i=vetor_func[len(vetor_func)-1]
                        else:
                            
                          vetor_erro.append(False)
                          linha_atual = tokens[i].split("->")
                          print(
                            "Erro sintatico - Esperado um ( - linha: "+str(linha_atual[1])+"\n")
                          arquivo_saida.write(
                            "Erro sintatico - Esperado um ( - linha: "+str(linha_atual[1])+"\n")
                    else:
                        vetor_erro.append(False)
                        linha_atual = tokens[i].split("->")
                        print(
                            "Erro sintatico - Esperado um indentificador - linha: "+str(linha_atual[1])+"\n")
                        arquivo_saida.write(
                            "Erro sintatico - Esperado um indentificador - linha: "+str(linha_atual[1])+"\n")
                else:
                    vetor_erro.append(False)
                    linha_atual = tokens[i].split("->")
                    print("Erro sintatico - Esperado um espaco - linha: " +str(linha_atual[1])+"\n")
                    arquivo_saida.write(
                        "Erro sintatico - Esperado um espaco - linha: "+str(linha_atual[1])+"\n")
                    
                    
            #verifica se existe retorno fora de uma funçao
            if("tok605" in tokens[i]):
                vetor_erro.append(False)
                linha_atual = tokens[i].split("->")
                print("Erro sintatico - Esperado retorno dentro de uma funcao - linha: " +str(linha_atual[1])+"\n")
                arquivo_saida.write(
                        "Erro sintatico - Esperado retorno dentro de uma funcao - linha: "+str(linha_atual[1])+"\n") 
            
            i += 1
        
        if((False in vetor_erro)==False):
            arquivo_saida.write(
                        "Cadeia de tokens reconhecida com sucesso")
        arquivo_saida.close()
            
