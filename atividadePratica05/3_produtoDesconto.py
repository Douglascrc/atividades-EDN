porcentagemDesconto = float(input("De quanto é o desconto? "))
valorOriginal = float(input("Qual o preço do produto? "))

def aplicaDesconto(preco, desconto):
    precoDesconto = preco - (preco * (desconto/100))
    return precoDesconto

precoFinal = aplicaDesconto(valorOriginal, porcentagemDesconto)

print(f"O preço com desconto aplicado é {precoFinal}")