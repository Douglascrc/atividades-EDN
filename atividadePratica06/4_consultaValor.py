import requests

moeda = input("Digite o código da moeda (ex: USD, EUR): ").upper().strip()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()
except Exception:
    print("Erro na requisição")
    exit()

chave = moeda + "BRL"
if chave not in dados:
    print("Moeda não existente ou não suportada")
    exit()

info = dados[chave]
valor_atual = info.get("bid")
maxima = info.get("high")
minima = info.get("low")
datahora = info.get("create_date")

print(f"Valor atual: {valor_atual}")
print(f"Máxima: {maxima}")
print(f"Mínima: {minima}")
print(f"Data/hora da última atualização: {datahora}")
