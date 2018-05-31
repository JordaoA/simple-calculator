#coding: utf-8
#Calculadora simples.
#Com uso de conhecimentos de Python até "If, Elif & Else". 

#Entrada
tipo_de_operacao = raw_input("Qual o tipo de operção você deseja fazer?\n*apenas operações simples*\n")

#possiveis resultados tipos de operações
mult = "multiplicação"
mult2 = "Multiplicação"
mult3 = "vezes"
mult4 = "Vezes"

div = "divisão"
div2= "Divisão"
div3 = "dividir"
div4 = "Dividir"

soma = "Soma"
soma2 = "soma"
soma3 = "Mais"
soma4 = "mais"

sub = "Subtração"
sub2 = "subtração"
sub3 = "Menos"
sub4 = "menos"

#Condições, caso o tipo da operação informado seja igual das operações basicas.
#Condições para multiplicação.
if tipo_de_operacao == mult or tipo_de_operacao == mult2 or tipo_de_operacao == mult3 or tipo_de_operacao == mult4:
	primeiro_numero = float(raw_input("Informe o primeiro numero: "))
	segundo_numero = float(raw_input("Informe o segundo numero: "))
	multplicacao = primeiro_numero * segundo_numero 
	print "O resultado da sua multiplicação é igual a : %f" %multplicacao
elif tipo_de_operacao != mult or tipo_de_operacao != mult2 or tipo_de_operacao != mult3 or tipo_de_operacao != mult4:
	print "\nOperação indisponível."

#Condições para divisão.
elif tipo_de_operacao == div or tipo_de_operacao == div2 or tipo_de_operacao == div3 or tipo_de_operacao == div4:
	primeiro_numero = float(raw_input("Informe o primeiro numero: "))
	segundo_numero = float(raw_input("Informe o segundo numero: "))
	divisao = primeiro_numero / segundo_numero
	print "O resultado da sua divisão é igual a : %f" %divisao
elif tipo_de_operacao != div or tipo_de_operacao != div2 or tipo_de_operacao != div3 or tipo_de_operacao != div4:
	print "\nOperação indisponível."
	
#Condições para soma.
elif tipo_de_operacao == soma or tipo_de_operacao == soma2 or tipo_de_operacao == soma3 or tipo_de_operacao == soma4:
	primeiro_numero = float(raw_input("Informe o primeiro numero: "))
	segundo_numero = float(raw_input("Informe o segundo numero: "))
	soma = primeiro_numero + segundo_numero
	print "O resultado da sua soma é igual a : %f" %soma
elif tipo_de_operacao != soma or tipo_de_operacao != soma2 or tipo_de_operacao != soma3 or tipo_de_operacao != soma4:
	print "\nOperação indisponível."

#Condições para subtração.
elif tipo_de_operacao == sub or tipo_de_operacao == sub2 or tipo_de_operacao == sub3 or tipo_de_operacao == sub4 :
	primeiro_numero = float(raw_input("Informe o primeiro numero: "))
	segundo_numero = float(raw_input("Informe o segundo numero: "))
	subtracao = primeiro_numero - segundo_numero
	print "O resultado da sua subtração é igual a : %f" %subtracao
elif tipo_de_operacao != sub or tipo_de_operacao != sub2 or tipo_de_operacao != sub3 or tipo_de_operacao != sub4 :
	print "\nOperação indisponível."

print "\n=======### V-1.0.0 ###======="
