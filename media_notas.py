nome = input("Digite o nome do aluno ")
nota_prova = float(input("Digite a nota da prova do aluno "))
nota_trabalho = float(input("Digite a nota do trabalho do aluno "))
media = (nota_prova + nota_trabalho)/2
print (f"A nota do aluno é {media}")
if media >= 7:
    print(f"A média do {nome} é {media}, ele está Aprovado!!")
else:
    print(f"A média do {nome} é {media}, ele está Reprovado!!")

