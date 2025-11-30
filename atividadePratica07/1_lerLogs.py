import pandas as pd

try: 
    df = pd.read_csv('atividadePratica07/logs_treinamento.csv')
    
    if 'tempo_execucao' not in df.columns:
        raise KeyError("Coluna 'tempo_execucao' não encontrada no arquivo.")
    
    media = df['tempo_execucao'].mean()
    desvio_padrao = df['tempo_execucao'].std()
    
    print(f"Média do tempo de execução: {media:.2f} segundos")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")

except FileNotFoundError:
    print("Erro: Arquivo de logs não encontrado.")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo está vazio.")
except Exception as e:
    print(f"Erro inesperado: {e}")