import scipy.io as sio
import pandas as pd
import numpy as np
from PIL import Image
#get boundary matrix
boundary_data=sio.loadmat('boundary_intensity.mat')
boundary_data=boundary_data['image']
#300*300 image
n=300
#point inside image: 298*298
m=298
#only consider inner point
inner_pixel_cnt=m*m

# x_0=np.zeros(inner_pixel_cnt)
x_0=sio.loadmat("x_0.mat")
x_0=x_0['image'][0]
print(x_0.shape)

def matmul_A(x):
    res_list=[]
    for point_id in range(inner_pixel_cnt):
        tmp_val=0
        point_row=point_id//m
        point_col=point_id-point_row*m
        if point_row==0:
            if point_col==0:
                tmp_val+=4*x[point_id]
                tmp_val-=x[point_id+1]
                tmp_val-=x[point_id+m]
                
                # A[point_id][point_id+1]=-1
            
                # A[point_id][point_id+m]=-1
            elif point_col==m-1:
                tmp_val+=4*x[point_id]
                tmp_val-=x[point_id-1]
                tmp_val-=x[point_id+m]
                # A[point_id][point_id]=4
                # A[point_id][point_id-1]=-1
            
                # A[point_id][point_id+m]=-1
            else:
                tmp_val+=4*x[point_id]
                tmp_val-=x[point_id-1]
                tmp_val-=x[point_id+1]
                tmp_val-=x[point_id+m]

                # A[point_id][point_id]=4
                # A[point_id][point_id-1]=-1
                # A[point_id][point_id+1]=-1
               
                # A[point_id][point_id+m]=-1
        elif point_row==m-1:
            if point_col==0:
                tmp_val+=4*x[point_id]
                tmp_val-=x[point_id+1]
                tmp_val-=x[point_id-m]

                # A[point_id][point_id]=4
               
                # A[point_id][point_id+1]=-1
                # A[point_id][point_id-m]=-1
              
            elif point_col==m-1:
                tmp_val+=4*x[point_id]
                tmp_val-=x[point_id-1]
                tmp_val-=x[point_id-m]

                # A[point_id][point_id]=4
                # A[point_id][point_id-1]=-1
               
                # A[point_id][point_id-m]=-1
               
            else:
                tmp_val+=4*x[point_id]
                tmp_val-=x[point_id-1]
                tmp_val-=x[point_id+1]
                tmp_val-=x[point_id-m]

                # A[point_id][point_id]=4
                # A[point_id][point_id-1]=-1
                # A[point_id][point_id+1]=-1
                # A[point_id][point_id-m]=-1
               
        elif point_col==0:
            tmp_val+=4*x[point_id]
            tmp_val-=x[point_id+1]
            tmp_val-=x[point_id-m]
            tmp_val-=x[point_id+m]

            # A[point_id][point_id]=4
           
            # A[point_id][point_id+1]=-1
            # A[point_id][point_id-m]=-1
            # A[point_id][point_id+m]=-1
        elif point_col==m-1:
            tmp_val+=4*x[point_id]
            tmp_val-=x[point_id-1]
            tmp_val-=x[point_id-m]
            tmp_val-=x[point_id+m]

            # A[point_id][point_id]=4
            # A[point_id][point_id-1]=-1
          
            # A[point_id][point_id-m]=-1
            # A[point_id][point_id+m]=-1
        else:
            #not on the edge
            tmp_val+=4*x[point_id]
            tmp_val-=x[point_id-1]
            tmp_val-=x[point_id+1]
            tmp_val-=x[point_id-m]
            tmp_val-=x[point_id+m]

            # A[point_id][point_id]=4
            # A[point_id][point_id-1]=-1
            # A[point_id][point_id+1]=-1
            # A[point_id][point_id-m]=-1
            # A[point_id][point_id+m]=-1

        res_list.append(tmp_val)
    res_list=np.array(res_list)
    return res_list
    #construct A,b end


def conjug(n,b,x_0,N,TOL):
    x=x_0
    #step 1
    r=b-matmul_A(x)
    w=r
    v=w
    alpha=np.linalg.norm(w)
    alpha=alpha*alpha
    #step 2
    k=1
    #step 3
    while k<=N:
        print("loop "+str(k))
        #step 4
        norm_v=np.linalg.norm(v)
        # print("norm_v:"+str(norm_v))
        # if norm_v<TOL:
        #     return x
        #step 5
        u=matmul_A(v)
        t=alpha/np.inner(v,u)
        print(t)
        print
        if t<TOL:
            return x
        x=x+t*v
        r=r-t*u
        w=r
        beta=np.linalg.norm(w)
        beta=beta*beta
        #step 6
        if beta<TOL:
            if np.linalg.norm(r)<TOL:
                return x
        #step 7
        s=beta/alpha
        v=w+s*v
        alpha=beta
        k=k+1
    #step 8
    if k>n:
        print("the maximum number of iteration was exceeded")




#construct A,b, b is vector


# for i in range(inner_pixel_cnt):
#     tmp_row=[]
#     for j in range(inner_pixel_cnt):
#         tmp_row.append(0)
#     A.append(tmp_row)
# A=np.zeros((inner_pixel_cnt,inner_pixel_cnt))
b=np.zeros(inner_pixel_cnt)
# for i in range(inner_pixel_cnt):
#     b.append(0)


#construct b
for point_id in range(inner_pixel_cnt):
    point_row=point_id//m
    point_col=point_id-point_row*m
    if point_row==0:
        if point_col==0:
            # A[point_id][point_id]=4
            b[point_id]+=boundary_data[1][0]
            # A[point_id][point_id+1]=-1
            b[point_id]+=boundary_data[0][1]
            # A[point_id][point_id+m]=-1
        elif point_col==m-1:
            # A[point_id][point_id]=4
            # A[point_id][point_id-1]=-1
            b[point_id]+=boundary_data[1][299]
            b[point_id]+=boundary_data[0][298]
            # A[point_id][point_id+m]=-1
        else:
            # A[point_id][point_id]=4
            # A[point_id][point_id-1]=-1
            # A[point_id][point_id+1]=-1
            b[point_id]+=boundary_data[0][point_col+1]
            # A[point_id][point_id+m]=-1
    elif point_row==m-1:
        if point_col==0:
            # A[point_id][point_id]=4
            b[point_id]+=boundary_data[n-2][0]
            # A[point_id][point_id+1]=-1
            # A[point_id][point_id-m]=-1
            b[point_id]+=boundary_data[n-1][1]
        elif point_col==m-1:
            # A[point_id][point_id]=4
            # A[point_id][point_id-1]=-1
            b[point_id]+=boundary_data[n-2][n-1]
            # A[point_id][point_id-m]=-1
            b[point_id]+=boundary_data[n-1][n-2]
        else:
            # A[point_id][point_id]=4
            # A[point_id][point_id-1]=-1
            # A[point_id][point_id+1]=-1
            # A[point_id][point_id-m]=-1
            b[point_id]+=boundary_data[n-1][point_col+1]
    elif point_col==0:
        # A[point_id][point_id]=4
        b[point_id]+=boundary_data[point_row+1][0]
        # A[point_id][point_id+1]=-1
        # A[point_id][point_id-m]=-1
        # A[point_id][point_id+m]=-1
    elif point_col==m-1:
        # A[point_id][point_id]=4
        # A[point_id][point_id-1]=-1
        b[point_id]+=boundary_data[point_row+1][n-1]
        # A[point_id][point_id-m]=-1
        # A[point_id][point_id+m]=-1
    else:
        pass
        #not on the edge
        # A[point_id][point_id]=4
        # A[point_id][point_id-1]=-1
        # A[point_id][point_id+1]=-1
        # A[point_id][point_id-m]=-1
        # A[point_id][point_id+m]=-1
#construct A,b end



N=1000000
TOL=0.5
res_mat="inner_array_conjugate.mat"

img_array_inner=conjug(inner_pixel_cnt,b,x_0,N,TOL)
img_array_inner=img_array_inner.reshape((m,m))
sio.savemat(res_mat,{'image':img_array_inner})

print(img_array_inner)