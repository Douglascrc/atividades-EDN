from datetime import datetime

dataNascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

nascimento = datetime.strptime(dataNascimento, "%d/%m/%Y")

hoje = datetime.today()

diasVividos = (hoje - nascimento).days

print(f"Você está vivo há {diasVividos} dias.")
