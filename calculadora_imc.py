print("\n***Calculadora de IMC***")
nome=input("\nDigite o seu nome: ")
peso=int(input("\nDigite o seu peso: "))
altura=float(input("\nDigite a sua altura: "))
imc=peso / (altura*altura)
print(f"{nome} seu IMC é {imc:.2f}")
if imc<18.5:
    print("Você está abaixo do peso.")
elif imc>=18.5 and imc<=24.9:
    print("Você está em seu peso normal.")
elif imc>=25.0 and imc<=29.9:
    print("Você está com sobrepeso.")
elif imc>=30.0:
    print("Você está obeso. Por favor se cuide!")