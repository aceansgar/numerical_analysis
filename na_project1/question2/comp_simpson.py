import numpy as np
import math
import matplotlib.pyplot as plt

acc_res=-4/9

def f(x):
    return math.sqrt(x)*math.log(x)

h_list=[]
err=[]
for k in range(1,20):
    divnum=2**k
    h=1/divnum
    h_list.append(h)
    simpson_res=0
    for i in range(1,int(divnum/2)):
        tmpx=2*i/divnum
        simpson_res+=2*f(tmpx)*h/3
    for i in range(1,int(divnum/2+1)):
        tmpx=(2*i-1)/divnum
        simpson_res+=4*f(tmpx)*h/3
    
    simpson_res+=f(1)*h/3

    
    err.append(simpson_res-acc_res)

plt.plot(h_list,err,'o')
plt.xlabel('h')
plt.ylabel('error')
plt.show()
plt.savefig('comp-simpson.png')