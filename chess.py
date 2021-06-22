import time
from termcolor import colored


def n(l):
    l += 1
    i = 0
    while(l > i**2):
        i += 1
    return i


psblmv = [(-2, -1), (-2, 1), (2, -1), (2, 1),
          (-1, -2), (-1, 2), (1, -2), (1, 2)]

array = []


def chess(s, d):
    global start
    global xx, yy
    start = time.time()
    if d > s:
        s, d = d, s
    global array
    global dvsbl
    global dst
    dvsbl = max(n(s), n(d), 8)
    # 1st is | & 2nd is --
    src = [s//dvsbl, s % dvsbl]
    dst = [d//dvsbl, d % dvsbl]
    if src[0]-dst[0] >= 0 and src[1]-dst[1] >= 0:
        pass
    else:
        temp = src[1]
        src[1] = dst[1]
        dst[1] = temp
    array = [[100 for i in range(dvsbl)] for j in range(dvsbl)]
    array[src[0]][src[1]] = 0
    while array[dst[0]][dst[1]] >= 100:
        addval(src, dst, dvsbl)
    return array[dst[0]][dst[1]]


def addval(src, dst, dvsbl):
    global array
    for i in range(min(dst[0]-1, src[0]+2), max(dst[0]-1, src[0]+2)):
        for j in range(min(dst[1]-1, src[1]+2), max(dst[1]-1, src[1]+2)):
            minn = 200
            if i in range(dvsbl) and j in range(dvsbl) and [i, j] != src:
                for k in range(8):
                    if i+psblmv[k][0] in range(dvsbl) and j+psblmv[k][1] in range(dvsbl):
                        nx = array[i+psblmv[k][0]][j+psblmv[k][1]]+1
                        if nx < minn:
                            minn = nx
                array[i][j] = minn


print("--->", colored(chess(156, 11), 'blue', attrs=['bold']), "steps")

# for i in range(dvsbl):
#   for j in range(dvsbl):
#     if array[i][j]==0:
#       print(colored(array[i][j], 'blue',attrs=['bold']), end="\t")
#     elif [i,j]==dst:
#       print(colored(array[i][j], 'blue',attrs=['bold']), end="\t")
#     else:
#       print(array[i][j],end="\t")
#   print()

# 1st is | & 2nd is --

print("--- ", (time.time() - start), " seconds ---")
