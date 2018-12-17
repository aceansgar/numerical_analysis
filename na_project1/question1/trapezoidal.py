import numpy as np
from scipy import linalg
from matplotlib import pyplot as plt

def g(t):
    f1=np.exp(2*t)
    f2=(np.exp(2)-1)*t/2
    f3=(np.exp(2)+1)/4
    return f1+f2-f3

for partnum in [8,16,32,64]:
    dx=1/partnum
    A=[]
    Y=[]
    for i in range(partnum+1):
        tmp_t = dx*i
        Y.append(g(tmp_t))
    for i in range(partnum+1):
        A_line=[]
        tmp_t = dx*i
        for j in range(partnum+1):
            A_line.append(0)
        A_line[i]+=1
        '''composite trapezoidal'''
        A_line[0]+=(tmp_t*dx/2)
        A_line[partnum]-=((1-tmp_t)*dx/2)
        for j in range(1,partnum):
            tmp_s=dx*j
            A_line[j]-=(tmp_s-tmp_t)*dx
        A.append(A_line)
    A=np.array(A)
    Y=np.array(Y)
   
    

    invA=np.linalg.inv(A)
    approx_res=np.dot(invA,Y)
    # print(approx_res)

    X=np.linspace(0,1,partnum+1)
    

    acc_res=np.exp(2*X)

    # print(acc_res)
    err_res=acc_res-approx_res
    test_start_id=int(0.25/dx)
    
    id0=0
    id1=test_start_id
    id2=id1*2
    id3=id1*3
    index=[id0,id1,id2,id3]
    print('error when sample nodes number is:%d'%partnum)
    for i in range(4):
        tmp_id=index[i]
        print("t="+str(0.25*i)+":",err_res[tmp_id])
    plt.plot(X,approx_res,'green',label='%d division'%partnum)
    # line,=plt.plot(X,approx_res,'green')
    # plt.legend(handles=[line],labels=['%d division'%partnum])
X=np.linspace(0,1,65)
    

acc_res=np.exp(2*X)
plt.plot(X,acc_res,'blue',label='accuracy')
# plt.legend(handles=[acc_line],labels=['accuracy'])
plt.legend()
plt.show()
plt.savefig('question1.png')
