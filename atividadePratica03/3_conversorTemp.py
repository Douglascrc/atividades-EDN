valor = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

if origem == "C":
    temp_c = valor
elif origem == "F":
    temp_c = (valor - 32) * 5/9
elif origem == "K":
    temp_c = valor - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = (temp_c * 9/5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida.")
    exit()

print(f"Resultado: {resultado:.2f} {destino}")
