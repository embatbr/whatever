def fib_100():
    ret = [0, 1]
    next_ix = 2

    while next_ix < 100:
        next_num = ret[next_ix - 1] + ret[next_ix - 2]
        ret.append(next_num)
        next_ix = next_ix + 1

    return ret


ret = fib_100()
print('length: %d' % len(ret))
print(ret)