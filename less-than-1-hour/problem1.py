# not using iteration in this problem

def sum_for_loop(eltos):
    ret = 0

    for i in range(len(eltos)):
        elto = eltos[i]
        ret = ret + elto

    return ret


def sum_while_loop(eltos):
    ret = 0

    i = 0
    while i < len(eltos):
        elto = eltos[i]
        ret = ret + elto
        i = i + 1

    return ret


def sum_recursion(eltos, ret=0):
    if len(eltos) > 0:
        elto = eltos[0]
        ret = sum_recursion(eltos[1 : ], ret + elto)

    return ret


eltos = list(range(1, 11))
print('eltos: %s' % eltos)

print('sum_for_loop: %d' % sum_for_loop(eltos))
print('sum_while_loop: %d' % sum_while_loop(eltos))
print('sum_recursion: %d' % sum_recursion(eltos))