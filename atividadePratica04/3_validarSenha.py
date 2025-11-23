senha = input("Crie sua senha: ")

tem_tamanho = len(senha) >= 8
tem_numero = any(char.isdigit() for char in senha)

if tem_tamanho and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida. Critérios:")
    if not tem_tamanho:
        print("- Deve ter pelo menos 8 caracteres.")
    if not tem_numero:
        print("- Deve conter pelo menos um número.")