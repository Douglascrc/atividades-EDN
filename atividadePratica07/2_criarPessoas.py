import pandas as pd

try:
    dados = {
        'nome': ['Ana', 'Carlos', 'Mariana', 'João', 'Beatriz'],
        'idade': [23, 35, 28, 41, 19],
        'cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Salvador', 'Belo Horizonte']
    }

    df = pd.DataFrame(dados)

    print("\nTabela criada:\n")
    print(df)

    caminho = input("\nDigite o caminho e o nome do arquivo: ")

    df.to_csv(caminho, index=False, encoding='utf-8')

    print(f"\n✅ Arquivo '{caminho}' salvo com sucesso!")

except FileNotFoundError:
    print("\n Erro: Caminho inválido.")
except Exception as e:
    print(f"\n Erro ao salvar o arquivo: {e}")
