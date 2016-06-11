def largest_possible(eltos):
    ret = 0

    for elto in eltos:
        if ret == 0:
            ret = elto
        else:
            case_1 = int('%d%d' % (ret, elto))
            case_2 = int('%d%d' % (elto, ret))
            if case_1 > case_2:
                ret = case_1
            else:
                ret = case_2

    return ret


print(largest_possible([50, 2, 1, 9]))