import scipy.io as sio
import pandas as pd
import numpy as np
from PIL import Image
#calculate init vector ,1 dimension 298*298
boundary_data=sio.loadmat('boundary_intensity.mat')
boundary_data=boundary_data['image']

gradient_array=sio.loadmat("gradient_map.mat")
gradient_array=gradient_array['imgradient']
gradient_x=gradient_array[0]
gradient_y=gradient_array[1]

# def proc_pixel(tmp):
#     res=tmp
#     if res>255:
#         res=255
#     elif res<0:
#         res=0
#     return res

n=300
for i in range(n):
    for j in range(n):
        if i==0:
            continue
        if j==0:
            continue
        if i==n-1:
            continue
        if j==n-1:
            continue
        if j==1:
            tmp=boundary_data[i][j-1]+gradient_x[i][j]
        else:
            tmp=boundary_data[i][j-2]+gradient_x[i][j-1]*2
        
      
        
        boundary_data[i][j]=tmp

# for i in range(n):
#     for j in range(n//2):
#         if i==0:
#             continue
#         if j==0:
#             continue
#         if i==n-1:
#             continue
#         if j==n-1:
#             continue
#         tmp3=


x_0=[]
for i in range(1,n-1):
    for j in range(1,n-1):
        x_0.append(boundary_data[i][j])

sio.savemat("x_0.mat",{'image':x_0})