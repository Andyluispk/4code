import random
numero_secreto = random.randint(1,10)
tentativas = 0
contagem_tentativas = 0
print ("Bem-vindo ao jogo do Número Secreto!!")
print ("Tente adivinhar o número secreto: ")
while tentativas != numero_secreto:
    numero = int(input("Digite um numero: "))
    contagem_tentativas = contagem_tentativas+1
    if numero == numero_secreto:
        print("Parabéns! Você adivinhou o número secreto!")
        print (f"Você precisou de {contagem_tentativas} tentativas para acertar.")
        break
    elif numero < numero_secreto:
        print (f"O número secreto é maior que {numero}")
    else:
        print (f"O número secreto é menor que {numero}")
    