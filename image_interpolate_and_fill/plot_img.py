import scipy.io as sio

from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

inner_array_file="inner_array_conjugate.mat"
res_file="res_conjugate.png"

inner_data=sio.loadmat(inner_array_file)
img_array_inner=inner_data['image']


boundary_data=sio.loadmat('boundary_intensity.mat')
img_array_edge=boundary_data['image']

n=300

img_array_res=np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if i==0:
            tmp=img_array_edge[i][j]
        elif i==n-1:
            tmp=img_array_edge[i][j]
        elif j==0:
            tmp=img_array_edge[i][j]
        elif j==n-1:
            tmp=img_array_edge[i][j]
        else:
            tmp=img_array_inner[i-1][j-1]
        img_array_res[i][j]=tmp

res_img=Image.fromarray(img_array_res)
res_img=res_img.convert('L')
res_img.save(res_file)

# fig=plt.figure()
# ax =Axes3D(fig)
# X=range(n)
# Y=range(n)
# X,Y=np.meshgrid(X,Y)
# Z=img_array_res
# ax.plot_surface(X,Y,Z)
# plt.savefig("res_img_surface.png")