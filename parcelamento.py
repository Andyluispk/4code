print("\n****Programa de parcelamento de compras****")
print("\nObs.: Acima de 6 parcelas é cobrado um juros de 5% por mês")

valor_compra = float(input("\nDigite o valor da sua compra: "))
numero_parcelas = int(input("Agora digite a quantidade de parcelas que você deseja: "))

if numero_parcelas > 6:
    print("\nCom essa quantidade de parcelas você vai pagar juros de 5% por mês, ok?")
    valor_parcelas_sem_juros = valor_compra / numero_parcelas
    valor_juros = valor_compra * 0.05
    valor_parcelas_com_juros = valor_parcelas_sem_juros + (valor_juros / numero_parcelas)
    print(f"Você pagará {numero_parcelas} parcelas de R$ {valor_parcelas_com_juros:.2f}")
    print(f"\n**Obs.:Você está pagando R$ {valor_juros:.2f} de juros no total.**")
else:
    valor_parcelas = valor_compra / numero_parcelas
    print(f"Você pagará {numero_parcelas} parcelas de R$ {valor_parcelas:.2f}")