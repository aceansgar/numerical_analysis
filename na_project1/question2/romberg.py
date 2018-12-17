import numpy as np
import math
import matplotlib.pyplot as plt


def f(t):
    if t==0:
        return 0
    f1=math.sqrt(t)
    f2=math.log(t)
    return f1*f2
def h(k):
    return 1/(2**(k-1))


acc_res=-4/9


r_list=[]
r_list.append([-1])

def romberg(k,t):
    
    try :
        return r_list[k][t]
    except:
        if k==1 and t==1:
            tmp_r=(f(0)+f(1))/2
            r_list.append([-1,tmp_r])
            return tmp_r
        if t==1:
            tmp_r=0
            i_last=2**(k-2)
            for i in range(1,i_last+1):
                tmp_id=2*i-1
                tmp_f=f(tmp_id*h(k))    
                tmp_r+=tmp_f
            tmp_r=tmp_r*h(k-1)
            tmp_r=tmp_r+romberg(k-1,1)
            tmp_r=tmp_r/2
            r_list.append([-1,tmp_r])
            return tmp_r
        tmp_r=romberg(k,t-1)+(romberg(k,t-1)-romberg(k-1,t-1))/(4**(t-1)-1)
        r_list[k].append(tmp_r)
        return tmp_r

max_k=10
romberg(max_k,max_k)
for i in range(1,max_k+1):
    for j in range(1,i+1):
        print("R(%d,%d)="%(i,j)+str(r_list[i][j]),"error is "+str(r_list[i][j]-acc_res))
