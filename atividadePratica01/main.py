# 1 - Programa de saudação
print("Olá mundo!")
print("--------")

# 2- Calculadora de Soma
numero1 = 12
numero2 = 14

def soma(a, b):
    return a + b

resultado = soma(numero1,numero2)
print(resultado)
print("--------")

# 3- Calculadora de Volume
C = 12
L = 14
A = 20

def calculaVolume(a, b,c):
    return a * b * c 

volume = calculaVolume(C,L,A)
print("O volume da caixa é:", volume, "cm³")
print("--------")

# 4- Calculadora de Preço Total
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

preco_total = preco_unitario * quantidade

print("Produto:", nome_produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total: R$", preco_total)
