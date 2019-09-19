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

def steepest(n,b,x_0,N,TOL):
    
    x=x_0
    r=b-matmul_A(x)
    t_denom=np.inner(matmul_A(r),r)
    t_numerat=np.inner(r,r)
    t=t_numerat/t_denom
    x=x+t*r
    step_id=0
    while step_id<N:
        print("loop "+str(step_id))
        r=b-matmul_A(x)
        r_norm=np.linalg.norm(r)
        # print(str(r_norm))
        # if r_norm<TOL:
        #     return x
        t_numerat=r_norm*r_norm
        t_denom=np.inner(matmul_A(r),r)
        t=t_numerat/t_denom
        print(t)
        if t<TOL:
            return x
        x=x+t*r
        step_id+=1
    return x


N=100
TOL=0.3
b=np.zeros(inner_pixel_cnt)

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


inner_array_steepest=steepest(inner_pixel_cnt,b,x_0,N,TOL)
inner_array_steepest=inner_array_steepest.reshape((m,m))
sio.savemat("inner_array_steepest.mat",{'image':inner_array_steepest})
print(inner_array_steepest)