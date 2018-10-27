#coding: utf -8
#Calculadora simples.
#Com uso de conhecimentos de Python, apenas com condicionais. 
while True:
  #Possiveis entradas para encerrar o laço
  finais = ["Fim", "fim", "acabar", "Acabar", "parar", "Parar", "Encerrar", "encerrar"]
  #Possiveis entradas para operações
  #possiveis entradas para multiplicação
  mult = ["multiplicação", "Multiplicação", "vezes", "Vezes","X","x"]
  #possiveis entradas para divisão
  div = ["divisão", "Divisão", "dividir", "Dividir",":","/"]
  #possiveis entradas para soma
  soma = ["Soma", "soma", "Mais", "mais","+"]
  #possiveis entradas para subtração
  sub = ["Subtração", "subtração", "Menos", "menos","-"]
  #possiveis entradas para potenciação
  pot = ["Potenciação", "potenciação", "Elevar", "elevar", "**", "^"]
  
  #Entrada
  tipo_de_operacao = raw_input("Qual o tipo de operção você deseja fazer?\n*apenas operações simples*\n")
  #condição para encerrar o laço
  if tipo_de_operacao in finais: break
  
  #Condições, caso o tipo da operação informado seja igual das operações basicas.
  #Condições para multiplicação.
  if tipo_de_operacao in mult:
      primeiro_numero = float(raw_input("Informe o primeiro numero: "))
      segundo_numero = float(raw_input("Informe o segundo numero: "))
      multplicacao = primeiro_numero * segundo_numero 
      print "O resultado da sua multiplicação é igual a : %.2f" %multplicacao
    
  #Condições para divisão.
  elif tipo_de_operacao in div:
      primeiro_numero = float(raw_input("Informe o primeiro numero: "))
      segundo_numero = float(raw_input("Informe o segundo numero: "))
      divisao = primeiro_numero / segundo_numero
      print "O resultado da sua divisão é igual a : %.2f" %divisao
	
  #Condições para soma.
  elif tipo_de_operacao in soma:
      primeiro_numero = float(raw_input("Informe o primeiro numero: "))
      segundo_numero = float(raw_input("Informe o segundo numero: "))
      soma = primeiro_numero + segundo_numero
      print "O resultado da sua soma é igual a : %.2f" %soma

  #Condições para subtração.
  elif tipo_de_operacao in sub :
      primeiro_numero = float(raw_input("Informe o primeiro numero: "))
      segundo_numero = float(raw_input("Informe o segundo numero: "))
      subtracao = primeiro_numero - segundo_numero
      print "O resultado da sua subtração é igual a : %f.2" %subtracao
  #Condições para potenciação
  elif tipo_de_operacao in pot :
      primeiro_numero = float(raw_input("Informe o primeiro numero: "))
      segundo_numero = float(raw_input("Informe o segundo numero: "))
      subtracao = primeiro_numero ** segundo_numero
      print "O resultado da sua potenciação de %s à %s é igual a : %.2f" %(primeiro_numero, segundo_numero, subtracao)

  else:
      print "\nOperação indisponível."

  print "\n=======### V-1.1.1 ###=======\n"
