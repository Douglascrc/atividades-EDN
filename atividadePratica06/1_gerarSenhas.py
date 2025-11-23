import random
import string

def gerar_senha(tamanho):
    if tamanho < 4:
        print("A senha deve ter pelo menos 4 caracteres para ser segura.")
        return None

    
    letras = string.ascii_letters  
    numeros = string.digits        
    simbolos = string.punctuation  


    senha = [
        random.choice(letras),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    todos_caracteres = letras + numeros + simbolos
    senha += [random.choice(todos_caracteres) for _ in range(tamanho - 3)]
    random.shuffle(senha)

    return "".join(senha)

try:
    tamanho_usuario = int(input("Digite o tamanho da senha desejada: "))
    nova_senha = gerar_senha(tamanho_usuario)

    if nova_senha:
        print("-" * 30)
        print(f"Sua senha gerada é: {nova_senha}")
        print("-" * 30)
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")