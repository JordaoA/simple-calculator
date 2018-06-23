#coding: utf-8
#Calculadora simples.
#Com uso de conhecimentos de Python, apenas com condicionais. 

#Entrada
tipo_de_operacao = raw_input("Qual o tipo de operção você deseja fazer?\n*apenas operações simples*\n")

#possiveis resultados tipos de operações
#possiveis entradas para multiplicação
mult = ["multiplicação", "Multiplicação", "vezes", "Vezes"]

#possiveis entradas para divisão
div = ["divisão", "Divisão", "dividir", "Dividir"]

#possiveis entradas para soma
soma = ["Soma", "soma", "Mais", "mais"]

#possiveis entradas para subtração
sub = ["Subtração", "subtração", "Menos", "menos"]

#Condições, caso o tipo da operação informado seja igual das operações basicas.
#Condições para multiplicação.
if tipo_de_operacao in mult:
    primeiro_numero = float(raw_input("Informe o primeiro numero: "))
    segundo_numero = float(raw_input("Informe o segundo numero: "))
    multplicacao = primeiro_numero * segundo_numero 
    print "O resultado da sua multiplicação é igual a : %f" %multplicacao
    
#Condições para divisão.
elif tipo_de_operacao in div:
    primeiro_numero = float(raw_input("Informe o primeiro numero: "))
    segundo_numero = float(raw_input("Informe o segundo numero: "))
    divisao = primeiro_numero / segundo_numero
    print "O resultado da sua divisão é igual a : %f" %divisao
	
#Condições para soma.
elif tipo_de_operacao == soma or tipo_de_operacao == soma2 or tipo_de_operacao == soma3 or tipo_de_operacao == soma4:
    primeiro_numero = float(raw_input("Informe o primeiro numero: "))
    segundo_numero = float(raw_input("Informe o segundo numero: "))
    soma = primeiro_numero + segundo_numero
    print "O resultado da sua soma é igual a : %f" %soma

#Condições para subtração.
elif tipo_de_operacao == sub or tipo_de_operacao == sub2 or tipo_de_operacao == sub3 or tipo_de_operacao == sub4 :
    primeiro_numero = float(raw_input("Informe o primeiro numero: "))
    segundo_numero = float(raw_input("Informe o segundo numero: "))
    subtracao = primeiro_numero - segundo_numero
    print "O resultado da sua subtração é igual a : %f" %subtracao
else:
    print "\nOperação indisponível."

print "\n=======### V-1.1.0 ###======="
