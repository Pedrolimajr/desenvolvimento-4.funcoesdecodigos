num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número "))
operacao = input("Informe a operação desejada (+, -, * ou /): ")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)



