import requests

def consulta_cep(cep):
    cep = cep.replace("-", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido")
        return
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
    except Exception:
        print("Falha na requisição")
        return
    if "erro" in dados:
        print("CEP não encontrado")
        return
    logradouro = dados.get("logradouro", "")
    bairro = dados.get("bairro", "")
    cidade = dados.get("localidade", "")
    estado = dados.get("uf", "")
    print(f"Logradouro: {logradouro}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")

if __name__ == "__main__":
    cep_digitado = input("Digite o CEP (somente números): ")
    consulta_cep(cep_digitado)
