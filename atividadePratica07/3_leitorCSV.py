import pandas as pd

try:
    caminho = input("Digite o caminho do arquivo CSV: ")

    df = pd.read_csv(caminho)

    print("\n✅ Arquivo carregado com sucesso!")
    print("\n📄 Conteúdo do arquivo linha por linha:\n")

    for index, linha in df.iterrows():
        print(linha.to_string())
        print("-" * 40)

except FileNotFoundError:
    print("\n Erro: Arquivo não encontrado.")
except pd.errors.EmptyDataError:
    print("\n Erro: O arquivo está vazio.")
except Exception as e:
    print(f"\n Erro inesperado: {e}")