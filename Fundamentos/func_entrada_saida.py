def operacao(operacao,num1,num2):
    if operacao == "+"or operacao == "soma":
        return num1 + num2
    if operacao == "-" or operacao == "subtração":
        if num1>num2:
            return num2-num1
    else:
       return num1-num2
    if operacao == "*" or operacao == "multiplicacao":
        return num1*num2
    if operacao == "/" or operacao == "divisao":
        if num1==0 or num2==0:
            print("Erro,não consigo dividir")
        else:
            return num1/num2

a=int(input("Digite um numero: "))
b=int(input("Digite outro numero: "))
op = input("Escolha uma opração:")
calc=operacao(op,a,b)
print(f'o resultado da operação:  {op} entre {a} e {b} é {calc}  ')