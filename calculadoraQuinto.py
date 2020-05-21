#********* Caculadora Quinto em Python *********
print("********* Caculadora Quinto em Python *********")

print("Selecione o número  da operação desejada: ")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
strContinuar = 1
while strContinuar == 1:
	strOperacao = int(input("Digite a sua opção (1/2/3/4): "))

	if strOperacao >=1 and  strOperacao <=4:
		fltN1 = float(input("Digite o primeiro número: "))
		fltN2 = float(input("Digite o segundo número: "))

		if strOperacao ==1:
			print(str(fltN1) +" + "+ str(fltN2) + " = " + str(fltN1+fltN2))
		elif strOperacao ==2:
			print(str(fltN1) +" - "+ str(fltN2) + " = " + str(fltN1-fltN2))
		elif strOperacao ==3:
			print(str(fltN1) +" x "+ str(fltN2) + " = " + str(fltN1*fltN2))
		elif strOperacao ==4:
			print(str(fltN1) +" / "+ str(fltN2) + " = " + str(fltN1/fltN2))
	else:
		print("Você digitou uma operação errada.")
	strDesejaContinuar = input("Deseja outra conta(S/N)? ")

	if strDesejaContinuar != "S":
		if strDesejaContinuar != "s":
			strContinuar = 0
			print("Calculadora fechada !!!!!")
		else:
			strContinuar = 1
