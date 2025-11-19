valor = float(input("Qual o valor da conta? "))
porcentagemGorjeta = float(input("Qual porcentagem da gorjeta? "))

def calcula(valorConta, porcentagem):
    gorjeta = (porcentagem/100) * valorConta
    return gorjeta

gorjeta = calcula(valor, porcentagemGorjeta)

print(gorjeta)