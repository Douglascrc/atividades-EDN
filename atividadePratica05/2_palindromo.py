texto = input("Qual a plavra ou frase? ")
texto_limpo = texto.replace(" ", "").lower()

if texto_limpo == texto_limpo[::-1]:
    print("É palindromo")
else:
    print("Não é um palindromo.")