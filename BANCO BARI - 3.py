'''1) Faça um algoritmo para ler um valor e some 15%. Após diminua 8%.
Imprima o valor inicial e valor final. Calcule e mostre a divisão do valor
inicial pelo valor final. Trate possíveis validações de erro de divisão.'''

'''Fiz a resolução de duas formas, a primeira passado um parâmetro e a segunda recebendo um input:
=======>>>>>>>>'''

#PRIMEIRA OPÇÃO:
#linguagem utilizada: Python
#IDE: Pycharm
class Numero:
    def __init__(self, n):
        self.n = n
#Dados = Produtos('Leite',1000) #teste1
#Dados = Numero(370) #teste2
#Dados = Numero(-100) #teste3
Dados = Numero(1.69) #teste4
#Dados = Numero(1000000000) #teste5
'''Para testar diferentes cenários, basta descomentar acima a linha desejada'''

if Dados.n != 0:
        a = Dados.n + Dados.n * 0.15  # primeira operação
        valorFinal = a - a * 0.08  # segunda operação
        resultado = Dados.n / valorFinal
        print(f'O valor atualizado é de: {valorFinal}') #imprime o valor inicial e o atualizado
        print(f'O resultado da divisão de {Dados.n} por {valorFinal} é: {resultado}')
        print(f'OBS.: Resultado arredondado: {resultado:.2f}')  # mostra resultado mais limpo
else:
    print('Preco informado é inválido, pois é menor ou igual a zero.')

'''SEGUNDA OPÇÃO:
x = float(input('Insira o valor inicial: ')) #valor inicial
a = x + x*0.15 #primeira operação
valorFinal = a - a*0.08 #segunda operação
if x != 0: #valida se o número digitado é diferente de zero
        print(f'O valor inicial é de: {x} e o valor atualizado é de: {valorFinal}') #imprime o valor inicial e o atualizado
        resultado = x / valorFinal #terceira operação
        print(f'O resultado da divisão de {x} por {valorFinal} é: {resultado}') #imprime o resultado da divisão
        print(f'Resultado arredondado: {resultado:.2f}') #mostra resultado mais limpo
        break
else:
        print('O número digitado é inválido!') #mensagem de erro se o usuário digitar zero
'''


