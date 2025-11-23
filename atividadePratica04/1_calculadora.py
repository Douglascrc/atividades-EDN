def calculadora(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

resultado = calculadora(num1, num2, operacao)
print(f"Resultado: {resultado}")