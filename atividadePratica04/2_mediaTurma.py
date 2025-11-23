notas = []

while True:
    entrada = input("Digite a nota do aluno (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        break
    
    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print("Por favor, digite um número válido.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")