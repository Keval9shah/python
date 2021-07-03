# chess2
# ultimate1.5
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


def chess(s, d, x=8):
    global start, end
    start = time.time()
    s -= 1
    d -= 1
    if s < 0 or d < 0:
        print("wrong parameters")
        return "error 42"
    if d > s:
        s, d = d, s
    global array, dvsbl, dst
    dvsbl = max(n(s), n(d), x)
    # 1st is | & 2nd is --
    src = [s//dvsbl, s % dvsbl]
    dst = [d//dvsbl, d % dvsbl]
    # print(src,dst)
    if src[0]-dst[0] >= 0 and src[1]-dst[1] >= 0:
        pass
    else:
        temp = src[1]
        src[1] = dst[1]
        dst[1] = temp
    if dst[0] > dst[1]:
        td = dst[0]
        dst[0] = dst[1]
        dst[1] = td
        ts = src[0]
        src[0] = src[1]
        src[1] = ts
    array = [[dvsbl for i in range(dvsbl)] for j in range(dvsbl)]
    array[src[0]][src[1]] = 0
    YXratio = abs(src[0]-dst[0])/abs(max(src[1]-dst[1], 1))
    # print(src,dst)
    # print(YXratio)
    m = 0
    while array[dst[0]][dst[1]] >= dvsbl:
        x = [min(dvsbl-1, max(max(0, dst[0]-3), src[0]-int(m *
                                                           max(1, YXratio))-2)), min(dvsbl, max(dst[0]+3, src[0]+3-m))]
        y = [min(dvsbl-1, max(max(0, dst[1]-3), src[1]-int(m *
                                                           max(1, YXratio))-2)), min(dvsbl, max(dst[1]+3, src[1]+3-m))]
        addval(src, dst, dvsbl, x, y)
        m += 1
    end = time.time() - start
    return array[dst[0]][dst[1]]


def addval(src, dst, dvsbl, x, y):
    global array
    for i in range(x[0], x[1]):
        for j in range(y[0], y[1]):
            minn = dvsbl
            if [i, j] != src:
                for k in range(8):
                    if i+psblmv[k][0] in range(dvsbl) and j+psblmv[k][1] in range(dvsbl):
                        nx = array[i+psblmv[k][0]][j+psblmv[k][1]]+1
                        if nx < minn:
                            minn = nx
                array[i][j] = minn


print("Least Knight Moves ♟")
print("Example - From: 20 To: 120")
x1 = int(input("From: "))
x2 = int(input("To: "))
print("--->", colored(chess(x1, x2), 'blue', attrs=['bold']), "steps")
print("--- ", (end), " seconds ---")

# lxmit=15
# nrr=[[0 for i in range(lxmit)] for j in range(lxmit)]
# sq=(lxmit**2)+1
# for i in range(1,sq):
#   temp=[]
#   for j in range(1,sq):
#     temp+=[chess(i,j,lxmit)]
#   nrr[(i-1)//lxmit][(i-1)%lxmit]=max(temp)

# for i in range(dvsbl):
#     for j in range(dvsbl):
#         if array[i][j] == 0:
#             print(colored(array[i][j], 'blue', attrs=['bold']), end="\t")
#         elif [i, j] == dst:
#             print(colored(array[i][j], 'blue', attrs=['bold']), end="\t")
#         else:
#             print(array[i][j], end="\t")
#     print()

# for i in nrr:
#   print(i)

# 1st is | & 2nd is --
