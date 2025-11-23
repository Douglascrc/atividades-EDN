import requests

try:
    response = requests.get("https://randomuser.me/api/")

    if response.status_code == 200:
        dados = response.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print("Erro na conexão.")

except:
    print("Falha na conexão.")