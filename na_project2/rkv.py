from __future__ import division
import numpy
import math


def f(t,y):
    a=y/t
    return a-a*a

def calc_k1(h,temp_t,temp_w):
    return h*f(temp_t,temp_w)

def calc_k2(h,temp_t,temp_w,k1):
    param1=temp_t+h/6
    param2=temp_w+(1/6)*k1
    return h*f(param1,param2)

def calc_k3(h,temp_t,temp_w,k1,k2):
    param1=temp_t+4*h/15
    param2=temp_w+k1*4/75+k2*16/75
    return h*f(param1,param2)

def calc_k4(h,temp_t,temp_w,k1,k2,k3):
    param1=temp_t+h*2/3
    param2=temp_w+k1*5/6-k2*8/3+k3*5/2
    return h*f(param1,param2)

def calc_k5(h,temp_t,temp_w,k1,k2,k3,k4):
    param1=temp_t+h*5/6
    param2=temp_w-k1*165/64+k2*55/6-k3*425/64+k4*85/96
    return h*f(param1,param2)

def calc_k6(h,temp_t,temp_w,k1,k2,k3,k4,k5):
    param1=temp_t+h
    param2=temp_w+k1*12/5-k2*8+k3*4015/612-k4*11/36+k5*88/255
    return h*f(param1,param2)

def calc_k7(h,temp_t,temp_w,k1,k2,k3,k4,k5,k6):
    param1=temp_t+h*1/15
    param2=temp_w-k1*8263/15000+k2*124/75-k3*643/680-k4*81/250+k5*2484/10625
    return h*f(param1,param2)

def calc_k8(h,temp_t,temp_w,k1,k2,k3,k4,k5,k6,k7):
    param1=temp_t+h
    param2=temp_w+k1*3501/1720-k2*300/43+k3*297275/52632-k4*319/2322+k5*\
    24068/84065+k7*3850/26703
    return h*f(param1,param2)

def rkv(end_a,end_b,init_val,TOL,hmax,hmin):
    T=[]
    W=[]
    H=[]#step size
    t=end_a
    w=init_val
    step_size=hmax

    flag=1
    while flag==1:
        k1=calc_k1(step_size,t,w)
        k2=calc_k2(step_size,t,w,k1)
        k3=calc_k3(step_size,t,w,k1,k2)
        k4=calc_k4(step_size,t,w,k1,k2,k3)
        k5=calc_k5(step_size,t,w,k1,k2,k3,k4)
        k6=calc_k6(step_size,t,w,k1,k2,k3,k4,k5)
        k7=calc_k7(step_size,t,w,k1,k2,k3,k4,k5,k6)
        k8=calc_k8(step_size,t,w,k1,k2,k3,k4,k5,k6,k7)
        w1=w+k1*13/160+k3*2375/5984+k4*5/16+k5*12/85+k6*3/44
        w2=w+k1*3/40+k3*875/2244+k4*23/72+k5*264/1955+k7*125/11592+k8\
        *43/616
        R=abs(w1-w2)/step_size
        if R<=TOL:
            t=t+step_size
            w=w1
            T.append(t)
            W.append(w)
            H.append(step_size)
        delta=0.84*pow(TOL/R,0.25)
        if delta<=0.1:
            step_size=0.1*step_size
        elif delta>=4:
            step_size=4*step_size
        else:
            step_size=delta*step_size
        
        if step_size>hmax:
            step_size=hmax
        if t>=end_b:
            flag=0
        elif t+step_size>end_b:
            step_size=end_b-t
        elif step_size<hmin:
            flag=0
            print("minimun h exceeded")
    
    print("T:")
    print(T)
    print
    print("W:")
    print(W)
    print
    print("H:")
    print(H)


rkv(1,4,1,pow(10,-6),0.5,0.05)