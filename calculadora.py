def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero"

print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite o número da operação: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    print(f"Resultado: {soma(num1, num2)}")
elif opcao == 2:
    print(f"Resultado: {subtracao(num1, num2)}")
elif opcao == 3:
    print(f"Resultado: {multiplicacao(num1, num2)}")
elif opcao == 4:
    print(f"Resultado: {divisao(num1, num2)}")
else:
    print("Opção inválida!")

