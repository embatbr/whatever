def wesley_safadao(dia, mes, ano):
    ano = ano - 1900

    safadeza = round(mes + (ano/100)*(50 - dia), 2)
    anjo = round(100 - safadeza, 2)

    print('%% safadeza: %.2f' % safadeza)
    print('%% anjo: %.2f' % anjo)


import sys

dia = int(sys.argv[1])
mes = int(sys.argv[2])
ano = int(sys.argv[3])

wesley_safadao(dia, mes, ano)