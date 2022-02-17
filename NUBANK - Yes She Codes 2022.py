#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'acharMinimoDeDias' function below.
#
# The function is expected to return an INTEGER.
# The function accepts FLOAT_ARRAY duracoes as parameter.
#

def acharMinimoDeDias(duracoes):
    lenDuracoes = len(duracoes)
    if lenDuracoes >= 1 and lenDuracoes <= 1000:
        dias = 0
        assistidos = []
        melhorCombinacao = {'soma': 0, 'pos1': None, 'pos2': None}
        while len(assistidos) < lenDuracoes:
            cont = 0
            while cont < lenDuracoes:
                cont2 = cont + 1
                while cont2 < lenDuracoes:
                    soma = duracoes[cont] + duracoes[cont2]
                    if soma > melhorCombinacao['soma'] \
                            and soma <= 3.00 \
                            and cont not in assistidos \
                            and cont2 not in assistidos:
                        melhorCombinacao['soma'] = soma
                        melhorCombinacao['pos1'] = cont
                        melhorCombinacao['pos2'] = cont2
                    cont2 += 1
                cont += 1
            if melhorCombinacao['soma'] > 0:
                assistidos.append(melhorCombinacao['pos1'])
                assistidos.append(melhorCombinacao['pos2'])
                melhorCombinacao = {'soma': 0, 'pos1': None, 'pos2': None}
            else:
                break
            dias += 1
        return dias + (lenDuracoes - len(assistidos))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    duracoes_count = int(input().strip())

    duracoes = []

    for _ in range(duracoes_count):
        duracoes_item = float(input().strip())
        duracoes.append(duracoes_item)

    result = acharMinimoDeDias(duracoes)

    fptr.write(str(result) + '\n')

    fptr.close()
