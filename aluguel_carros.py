custo_dia = 90.0
custo_km = 0.20

print("💲Tabela de Preços💲\n")
print(f"\n📆Custo por dia: R$ {custo_dia:.2f}")
print(f"🛣️Custo por km rodado: R$ {custo_km:.2f}")

km_percorridos = float(input("\nDigite a quantidade de km percorridos🛣️: "))
dias_alugados = int(input("Digite a quantidade de dias alugados📆: "))

preco_dias = (dias_alugados * custo_dia)
preco_km = (km_percorridos * custo_km)
preco_total = (preco_dias + preco_km)

print("\n🗒️RECIBO DE ALUGUEL🗒️\n")
print(f"Dias alugados📆: {dias_alugados} dias")
print(f"Custo dos dias💲: R$ {preco_dias:.2f}")
print(f"Km percorridos🛣️: {km_percorridos} km")
print(f"Custo por km💸: R$ {preco_km:.2f}")
print(f"\nPreço total a pagar📋: R$ {preco_total:.2f}")