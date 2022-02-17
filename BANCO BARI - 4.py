'''3) Faça um algoritmo para ler quatro números e mostre a sua média ponderada
(as notas têm pesos respectivos de 1, 1, 2 e 3).'''

a = float(input('Insira o primeiro número: '))
b = float(input('Insira o primeiro número: '))
c = float(input('Insira o primeiro número: '))
d = float(input('Insira o primeiro número: '))
p = (a*1 + b*1 + c*2 + d*3)

#abaixo se o código for permitir entrada de números negativos, pare verificar basta descomentar
'''if p > 0:
    ponderada = p / 7
    print(f'A média ponderada é de: {ponderada:.2f}')
else:
    print('Um ou mais números digitados é/são inválido(s)!') #mensagem de erro se o usuário digitar numero zero
'''
#aqui está a forma mais completa, onde excluo dos resultados caso o usuário digite um número negativo
# ou o resultado da média ponderada for menor que zero. Caso queira testar a opção mais abrangente,
# basta comentar essa parte abaixo e descomentar a opção acima desse comentário
if p > 0:
    ponderada = p / 7
    if a >= 0 and b >= 0 and c >= 0 and d >= 0:
        ponderada = (a*1 + b*1 + c*2 + d*3) / 7
        print(f'A média ponderada é de: {ponderada:.2f}')
    else:
        print('Um ou mais números digitados é/são inválido(s)!') #mensagem de erro se o usuário digitar numero negativo
else:
    print('Digite um número diferente de zero!')  # mensagem de erro se o usuário digitar o numero zero