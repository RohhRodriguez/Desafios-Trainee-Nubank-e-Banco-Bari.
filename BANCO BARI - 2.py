'''2) O preço final de um produto é calculado pela soma do preço bruto com o preço dos impostos
(30% do preço bruto) e a percentagem do revendedor (28% do preço bruto). Faça um algoritmo que
leia o nome do produto e o preço bruto e escreva o nome do produto e o preço final.'''

class Produtos:
    def __init__(self, nome, precoI):
        self.nome = nome
        self.precoI = precoI

#Dados = Produtos('Leite',1000) #teste1
Dados = Produtos('Macarrão',370) #teste2
#Dados = Produtos('Manteiga',-100) #teste3
#Dados = Produtos('Vinagre',1.69) #teste4
#Dados = Produtos('Café',1000000000) #teste5
'''Para testar diferentes cenários, basta descomentar acima a linha desejada'''

if Dados.precoI >= 0:
    impostos = Dados.precoI*0.30
    revendedores = Dados.precoI * 0.28
    precoF = Dados.precoI + impostos + revendedores
    print(f'{Dados.nome} R$ {precoF:,.2f}')
else:
    print('Preco informado é inválido, pois é menor ou igual a zero.')
