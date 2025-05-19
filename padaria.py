# Inicialização das variáveis
frances = 0
integral = 0
doce_liso = 0
doce_farofa = 0
forma = 0
valor_frances = 0.0
valor_integral = 0.0
valor_doce_liso = 0.0
valor_doce_farofa = 0.0
valor_forma = 0.0
valor_total = 0.0

while True:
    print("\nMenu de opções:📋")
    print("1 - Comprar pão francês🍞")
    print("2 - Comprar pão integral🍞")
    print("3 - Comprar pão doce liso🍞")
    print("4 - Comprar pão doce farofa🍞")
    print("5 - Comprar pão de forma🍞")
    print("6 - Finalizar compra💵")

    opcao = int(input("Escolha uma opção🏷️: "))

    if opcao == 1:
        quantidade = int(input("Digite a quantidade de pão francês que você quer⌨️: "))
        valor_do_pao = 1.50
        frances += quantidade
        valor_frances += round(quantidade * valor_do_pao, 2)
    elif opcao == 2:
        quantidade = int(input("Digite a quantidade de pão integral que você quer⌨️: "))
        valor_do_pao = 2.00
        integral += quantidade
        valor_integral += round(quantidade * valor_do_pao, 2)
    elif opcao == 3:
        quantidade = int(input("Digite a quantidade de pão doce liso que você quer⌨️: "))
        valor_do_pao = 2.50
        doce_liso += quantidade
        valor_doce_liso += round(quantidade * valor_do_pao, 2)
    elif opcao == 4:
        quantidade = int(input("Digite a quantidade de pão doce farofa que você quer⌨️: "))
        valor_do_pao = 3.00
        doce_farofa += quantidade
        valor_doce_farofa += round(quantidade * valor_do_pao, 2)
    elif opcao == 5:
        quantidade = int(input("Digite a quantidade de pão de forma que você quer⌨️: "))
        valor_do_pao = 0.95
        forma += quantidade
        valor_forma += round(quantidade * valor_do_pao, 2)
    elif opcao == 6:
        valor_total = round(valor_frances + valor_integral + valor_doce_liso + valor_doce_farofa + valor_forma, 2)
        break
    else:
        print("⛔Opção inválida. Por favor, escolha uma opção válida.")

print("\nResumo da compra🗒️:")
if frances > 0:
    print(f"Pão Francês - Quantidade: {frances} | Valor: 💸R$ {valor_frances:.2f}")
if integral > 0:
    print(f"Pão Integral - Quantidade: {integral} | Valor: 💸R$ {valor_integral:.2f}")
if doce_liso > 0:
    print(f"Pão Doce Liso - Quantidade: {doce_liso} | Valor: 💸R$ {valor_doce_liso:.2f}")
if doce_farofa > 0:
    print(f"Pão Doce Farofa - Quantidade: {doce_farofa} | Valor: 💸R$ {valor_doce_farofa:.2f}")
if forma > 0:
    print(f"Pão de Forma - Quantidade: {forma} | Valor: 💸R$ {valor_forma:.2f}")
print(f"\nValor total da compra: 💰R$ {valor_total:.2f}")