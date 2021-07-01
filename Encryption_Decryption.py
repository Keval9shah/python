# END
#+1+count % 2
#-1-count % 2
from math import sqrt
import random as rn


def caesarCipher(string, key=0):
    result = ""
    for i in string:
        if ord(i) in range(65, 91) or ord(i) in range(97, 123):
            if ord(i) < 91:
                result += chr((ord(i) + key - 65) % 26 + 65)
            else:
                result += chr((ord(i) + key - 97) % 26 + 97)
        else:
            result += i
    return result


def caesarDecipher(string, key=0):
    result = ""
    for i in string:
        if ord(i) in range(65, 91) or ord(i) in range(97, 123):
            if ord(i) < 91:
                result += chr((ord(i) - key - 65) % 26 + 65)
            else:
                result += chr((ord(i) - key - 97) % 26 + 97)
        else:
            result += i
    return result


def Enc(txt, z):
    if z != 0:
        txt = caesarCipher(txt, z)
    rn.seed(z)
    count = 0
    len1 = int(sqrt(len(txt)))
    if len1*len1 < len(txt):
        len1 += 1
    if z == 0:
        move = 0
    else:
        move = rn.randint(0, len1)
    new_st = [[a for a in range(len1)] for b in range(len1)]
    for i in range(len1):
        for j in range(move, len1):
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


def Dec(txt, z):
    rn.seed(z)
    count = 0
    len1 = int(sqrt(len(txt)))
    if len1*len1 < len(txt):
        len1 += 1
    if z == 0:
        move = 0
    else:
        move = rn.randint(0, len1)
    nonull = len1*len1-len(txt)
    new_st = [[a for a in range(len1)] for b in range(len1)]

    nplc = -1
    if nonull > 0:
        if nonull > len1:
            new_st[-1] = ['\0' for i in range(len1)]
            nonull -= len1
            nplc = -2
        for i in range(move-nonull, move):
            new_st[nplc][i] = '\0'
    for i in range(len1):
        for j in reversed(range(len1)):
            if new_st[j][i] != '\0':
                new_st[j][i] = txt[count]
                count += 1
    ans = ""
    count = 0
    for i in range(len1):
        for j in range(move, len1):
            if new_st[i][j] != '\0':
                ans += chr(ord(new_st[i][j])-1-count % 2)
            count += 1
        for j in range(move):
            if new_st[i][j] != '\0':
                ans += chr(ord(new_st[i][j])-1-count % 2)
            count += 1
    if z != 0:
        return caesarDecipher(ans, z)
    else:
        return ans


tg = input("Enter \n1 to Encrypt & \n2 to Decrypt\n")
if tg == "1":
    intxt = input("Text to encrypt  ")
    inkey = input("key  ")
    if inkey.isnumeric():
        print("◻ Encrypted text is --> " + Enc(intxt, int(inkey)))
    else:
        print("key should be numeric")
elif tg == "2":
    intxt = input("Text to encrypt  ")
    inkey = input("key  ")
    if inkey.isnumeric():
        print("◻ Decrypted text is --> " + Dec(intxt, int(inkey)))
    else:
        print("key should be numeric")
