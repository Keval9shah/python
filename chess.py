#chess2
# ultimate
import time
from termcolor import colored

def n(l):
  l += 1
  i = 0
  while(l > i**2):
      i += 1
  return i


psblmv = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

array=[]
def chess(s, d,x=8):
  global start
  start = time.time()
  if d>s:
    s,d=d,s
  global array
  global dvsbl
  global dst
  dvsbl = max(n(s), n(d), 50)
  # 1st is | & 2nd is --
  src = [s//dvsbl, s % dvsbl]
  dst = [d//dvsbl, d % dvsbl]
  if src[0]-dst[0]>=0 and src[1]-dst[1]>=0:
    pass
  else:
    temp=src[1]
    src[1]=dst[1]
    dst[1]=temp
  array=[[1000 for i in range(dvsbl)] for j in range(dvsbl)]
  array[src[0]][src[1]]=0
  YXratio=abs(src[0]-dst[0])/abs(max(src[1]-dst[1],1))
  # print(YXratio)
  m=0
  while array[dst[0]][dst[1]]>=1000:
    addval(src,dst,dvsbl,m,YXratio)
    m+=1
  return array[dst[0]][dst[1]]



def addval(src,dst,dvsbl,m,YXratio):
  global array
  for i in range(min(dst[0]-1,src[0]+3)+src[0]-int(m*YXratio)-2,max(dst[0]+1,src[0]+3-int(m*(1/YXratio)))):
    for j in range(min(dst[1]-1,src[1]+3)+src[1]-int(m*YXratio)-2,max(dst[1]+1,src[1]+3-int(m*(1/YXratio)))):
      minn=1000
      if i in range(dvsbl) and j in range(dvsbl) and [i,j]!=src:
        for k in range(8):
          if i+psblmv[k][0] in range(dvsbl) and j+psblmv[k][1] in range(dvsbl):
            nx=array[i+psblmv[k][0]][j+psblmv[k][1]]+1
            if nx<minn:
              minn=nx
        array[i][j]=minn


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

print("--->",colored(chess(0,9929), 'blue',attrs=['bold']),"steps")

print("--- ",(time.time() - start)," seconds ---")