from __future__ import division
import numpy
import math



def sor(n,A_mat,b_vec,xo_vec,w,TOL,N):
    k=1
    
    while k<=N:
        x_vec=[]
        for i in xrange(n):
            temp_res=0
            for j in xrange(i-1):
                temp_res=temp_res-A_mat[i][j]*x_vec[j]
            for j in xrange(i+1,n):
                temp_res=temp_res-A_mat[i][j]*xo_vec[j]
            temp_res=temp_res + b_vec[i]
            temp_x=(1-w)*xo_vec[i]+(1/A_mat[i][i])*w*temp_res
            x_vec.append(temp_x)
        delta_x_vec=[]
        for i in xrange(n):
            delta_x_vec.append(abs(x_vec[i]-xo_vec[i]))
        
        norm=0
        for i in xrange(n):
            temp_x=delta_x_vec[i]
            if temp_x>norm:
                norm=temp_x
        if norm<TOL:
            print(x_vec)
            return
        k=k+1
        for i in xrange(n):
            xo_vec[i]=x_vec[i]
    print("maximun number of iterations exceeded")


A=[]
n=80

for i in xrange(80):
    a_vec=[]
    for j in xrange(80):
        a_vec.append(0)
    A.append(a_vec)

for i in xrange(80):
    A[i][i]=2*(i+1)
for i in xrange(78):
    A[i][i+2]=0.5*(i+1)
for i in xrange(2,80):
    A[i][i-2]=0.5*(i+1)
for i in xrange(76):
    A[i][i+4]=0.25*(i+1)
for i in xrange(4,80):
    A[i][i-4]=0.25*(i+1)

b=[]
for i in xrange(80):
    b.append(math.pi)
nn=100
w=1.1
TOL=pow(10,-5)
xo=[]
for i in xrange(80):
    xo.append(0)

sor(n,A,b,xo,w,TOL,nn)

        
    
