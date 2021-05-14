from math import sqrt
import random as rn
import time

def Enc(txt,z):
    rn.seed(z)
    count = 0
    len1 = int(sqrt(len(txt)))
    if len1*len1 < len(txt):
        len1 += 1
    if z==0:
        move=0
    else:
        move=rn.randint(0,len1)
    new_st = [[a for a in range(len1)] for b in range(len1)]
    for i in range(len1):
        for j in range(move,len1):
            if count < len(txt):
                new_st[i][j] = chr(ord(txt[count])+1+count % 2)
                count += 1
            else:
                new_st[i][j] = '\0'
        for j in range(move):
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


def Dec(txt,z):
    rn.seed(z)
    count = 0
    len1 = int(sqrt(len(txt)))
    if len1*len1 < len(txt):
        len1 += 1
    if z==0:
        move=0
    else:
        move=rn.randint(0,len1)
    nonull=len1*len1-len(txt)
    new_st = [[a for a in range(len1)] for b in range(len1)]

    nplc=-1
    if nonull>0:
        if nonull>len1:
            new_st[-1]=['\0' for i in range(len1)]
            nonull-=len1
            nplc=-2
        for i in range(move-nonull,move):
            new_st[nplc][i]='\0'
    for i in range(len1):
        for j in reversed(range(len1)):
            if new_st[j][i]!='\0':
                new_st[j][i] = txt[count]
                count += 1
    ans = ""
    count = 0
    for i in range(len1):
        for j in range(move,len1):
            if new_st[i][j] != '\0':
                ans += chr(ord(new_st[i][j])-1-count % 2)
            count += 1
        for j in range(move):
            if new_st[i][j] != '\0':
                ans += chr(ord(new_st[i][j])-1-count % 2)
            count += 1
    return ans


def EnD(y,z=0):
    x=input("Enter the string  ")
    start = time.time()
    if type(x) == str and type(y) == int and y in [1, 2] and len(x) > 0:
        print("Copy text between 2 _")
        if y == 1:
            print("Encrypted text is _", Enc(x,z),"_  Key=",z,sep="")
        elif y == 2:
            print("Decrypted text is _", Dec(x,z),"_",sep="")
    print("--- ",(time.time() - start)," seconds ---")


EnD(1,904)
