import itertools as it
import time
from termcolor import colored


def n(l):
    l += 1
    i = 0
    while(l > i**2):
        i += 1
    return i


def chess(s, d):
    start = time.time()
    dvsbl = max(n(s), n(d), 8)
    src = [s//dvsbl, s % dvsbl]
    ns = src.copy()
    dst = [d//dvsbl, d % dvsbl]
    qaz = 0
    psblmv = list(it.product([-2, 2], [-1, 1])) + \
        list(it.product([-1, 1], [-2, 2]))
    for x in range(1, 11):
        for i in it.product(psblmv, repeat=x):
            for j in range(len(i)):
                if ns[0]+i[j][0] > -1 and ns[1]+i[j][1] > -1 and ns[0]+i[j][0] < dvsbl and ns[1]+i[j][1] < dvsbl:
                    ns[0] += i[j][0]
                    ns[1] += i[j][1]
                    if ns == dst:
                        mids = []
                        tem = src.copy()
                        mids.append((src[0]*dvsbl+src[1]))
                        for c in i:
                            tem[0] += c[0]
                            tem[1] += c[1]
                            mids.append((tem[0]*dvsbl+tem[1]))
                        print("steps --> ", mids)
                        for k in range(dvsbl):
                            for j in range(dvsbl):
                                qaz = k*dvsbl+j
                                if qaz in mids:
                                    print(colored(qaz, 'green',
                                                  attrs=['bold']), end="\t")
                                else:
                                    print(qaz, end="\t")
                            print()
                        print("--- ", (time.time() - start), " seconds ---")
                        print(x, "moves")
                        return
            ns = src.copy()


chess(61, 10)
