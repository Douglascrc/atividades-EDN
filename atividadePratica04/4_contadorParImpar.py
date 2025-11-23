pares = 0
impares = 0

print("Digite números inteiros. Digite 0 para encerrar.")

while True:
    try:
        numero = int(input("Digite um número: "))
        
        if numero == 0:
            break
            
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

print("--------")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")