import json

try:
    
    pessoa = {
        "nome": "Douglas Campos",
        "idade": 25,
        "cidade": "Rio de Janeiro",
    }

    
    caminho = input("Digite o caminho e o nome do arquivo: ")

    
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

    print(f"\n✅ Arquivo '{caminho}' salvo com sucesso!")

   
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)

    print("\n📄 Dados lidos do arquivo JSON:")
    for chave, valor in dados_lidos.items():
        print(f"{chave}: {valor}")

except FileNotFoundError:
    print("\n Erro: Arquivo não encontrado.")
except PermissionError:
    print("\n Erro: Permissão negada para acessar ou salvar o arquivo.")
except json.JSONDecodeError:
    print("\n Erro: O arquivo não está em um formato JSON válido.")
except Exception as e:
    print(f"\n Erro ao salvar ou ler o arquivo: {e}")
