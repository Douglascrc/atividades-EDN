nome_produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$ {:.2f}".format(preco_original))
print("Desconto: {}%".format(desconto_percentual))
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Preço final: R$ {:.2f}".format(preco_final))