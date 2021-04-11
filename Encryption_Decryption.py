# ENC
from math import sqrt


def Enc(txt):
    count = 0
    len1 = int(sqrt(len(txt)))
    if len1*len1 < len(txt):
        len1 += 1
    new_st = [[a for a in range(len1)] for b in range(len1)]
    for i in range(len1):
        for j in range(len1):
            if count < len(txt):
                new_st[i][j] = chr(ord(txt[count])+1+count % 2)
                count += 1
            else:
                new_st[i][j] = '\0'
    ans = ""
    for i in range(len1):
        for j in reversed(range(len1)):
            if new_st[j][i] != '\0':
                ans += new_st[j][i]
    return ans


def Dec(txt):
    count = 0
    len1 = int(sqrt(len(txt)))
    if len1*len1 < len(txt):
        len1 += 1
    new_st = [[a for a in range(len1)] for b in range(len1)]
    for i in range(len1):
        for j in reversed(range(len1)):
            if j*len1+i+1 > len(txt):
                new_st[j][i] = '\0'
            else:
                new_st[j][i] = txt[count]
                count += 1
    ans = ""
    count = 0
    for i in range(len1):
        for j in range(len1):
            if new_st[i][j] != '\0':
                ans += chr(ord(new_st[i][j])-1-count % 2)
            count += 1
    return ans


def EnD(x, y):
    if type(x) == str and type(y) == int and y in [1, 2] and len(x) > 0:
        if y == 1:
            print("Encrypted text is", Enc(x))
        elif y == 2:
            print("Decrypted text is", Dec(x))


EnD('0ltxjm', 2)
