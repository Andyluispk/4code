while True:
        print("\n****Conversor de Temperatura****\n")
        print("1 - Celsius para Fahrenheit")
        print("2 - Celsius para Kelvin")
        print("3 - Fahrenheit para Celsius")
        print("4 - Fahrenheit para Kelvin")
        print("5 - Kelvin para Celsius")
        print("6 - Kelvin para Fahrenheit")
        print("7 - Finalizar o sistema")

        opcao = int(input("\nEscolha a opção de conversão que você deseja: "))

        if opcao == 7:
            break
        elif opcao < 1 or opcao > 7:
            print("\nErro: Opção inválida! Escolha um número entre 1 e 7.")
            continue

        temperatura = float(input("\nDigite a temperatura: "))

        if opcao == 1:
            resultado = (temperatura * 9/5) + 32
            print(f"A conversão é: {temperatura}°C = {resultado}°F")
        elif opcao == 2:
            resultado = temperatura + 273.15
            print(f"A conversão é: {temperatura}°C = {resultado}°K")
        elif opcao == 3:
            resultado = (temperatura - 32) * 5/9
            print(f"A conversão é: {temperatura}°F = {resultado}°C")
        elif opcao == 4:
            resultado = ((temperatura - 32) * 5/9) + 273.15
            print(f"A conversão é: {temperatura}°F = {resultado}°K")
        elif opcao == 5:
            resultado = temperatura - 273.15
            print(f"A conversão é: {temperatura}°K = {resultado}°C")
        elif opcao == 6:
            resultado = ((temperatura - 273.15) * 9/5) + 32
            print(f"A conversão é: {temperatura}°K = {resultado}°F")
