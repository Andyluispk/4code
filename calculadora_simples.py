while True:
    print("🧮Calculadora🧮")
    print("1 - Somar ➕")
    print("2 - Subtrair➖")
    print("3 - Multiplicar✖️")
    print("4 - Dividir ➗")
    print("0 - Sair🏃‍➡️")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 0:
        break
    elif opcao in[1, 2, 3, 4]:
        resultado=None 
        while True:
            if resultado is None:
                num1=float(input("Digite o primeiro número: "))
                num2=float(input("Digite o segundo número: "))
                if opcao == 1:
                    resultado = num1+num2
                elif opcao == 2:
                    resultado = num1-num2
                elif opcao == 3:
                    resultado = num1*num2
                elif opcao == 4:
                    if num2 != 0:
                        resultado = num1/num2
                    else:
                        print("Erro! Não pode dividir por zero")
                        resultado = None
                        continue
                print(f"O resultado é {resultado}📟")
            
                
                print("\nDeseja: (1) continuar operando, (2) Fazer uma nova operação ou (0) Voltar ao menu principal📲")
                opcao_operacao=int(input("Escolha a sua opçao: "))
                
            if opcao_operacao==0:
                    break
            elif opcao_operacao==2:
                resultado=None
                num1=float(input("Digite o primeiro número: "))
                num2=float(input("Digite o segundo número: "))
                if opcao == 1:
                    resultado = num1+num2
                elif opcao == 2:
                    resultado = num1-num2
                elif opcao == 3:
                    resultado = num1*num2
                elif opcao == 4:
                    if num2 != 0:
                        resultado = num1/num2
                    else:
                        print("⛔Erro! Não pode dividir por zero")
                        resultado = None
                        continue
                print(f"O resultado é {resultado}")
                print("\nDeseja: (1) continuar operando, (2) Fazer uma nova operação ou (0) Voltar ao menu principal📲")
                opcao_operacao=int(input("Escolha a sua opçao: "))
                
            elif opcao_operacao==1:
                print(f"O resultado anterior é: {resultado}")
                num1=float(input("Digite o numero para operar: "))
                if opcao == 1:
                    resultado += num1
                elif opcao == 2:
                    resultado -=num1
                elif opcao == 3:
                    resultado *=num1
                elif opcao == 4:
                    if num1 != 0:
                        resultado /=num1
                    else:
                        print("⛔Erro! Não pode dividir por zero")
                        continue
                print(f"O resultado é {resultado}")
                print("\nDeseja: (1) continuar operando, (2) Fazer uma nova operação ou (0) Voltar ao menu principal📲")
                opcao_operacao=int(input("Escolha a sua opçao: "))

    else:
        print("🚫Opção inválida.")