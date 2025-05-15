print("***Calculadora de Bonus de Salário***")
nome=(input("\nDigite o nome do vendedor: "))
salario_fixo=float(input(f"Agora digite o salário do {nome}: R$ "))
vendas=int(input(f"E por fim digite a quantidade de vendas que o {nome} realizou: "))
bonus=0.15*salario_fixo
salario_recebido=salario_fixo+bonus
if vendas>=20:
    print(f"\nO funcionário {nome} realizou {vendas} vendas, e com isso atingiu a meta.")
    print(f"\nO salário de {nome} ficou em R$ {salario_recebido:.2f}")
else:
    print(f"\nO funcionário {nome} realizou {vendas} vendas, e infelizmente não atingiu a meta.")
    print(f"\nO salário de {nome} será de R$ {salario_fixo:.2f}")