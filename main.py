#Crie um programa que receba uma notas de avaliações em uma quantidade definida pelo usuário, calcula a média e exibe o resultado. Ao terminar envie para o repositório do GitHub e poste o link.

notas = []

num_notas = int(input('Informe quantas notas vc vai digitar: '))

while num_notas >= 1:
    nova_nota = int(input('Informe a nota: '))
    notas.append(nova_nota)
    num_notas -= 1


media = sum(notas)/len(notas)
print(f'A média das notas é: {media:,.2f}')