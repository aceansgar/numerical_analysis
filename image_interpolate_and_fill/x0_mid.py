from scipy.io import loadmat
import numpy as np

data=loadmat('boundary_intensity.mat')
vc=np.array(data['image'])
data=loadmat('gradient_map.mat')
gra_x=data['imgradient'][0]
gra_y=data['imgradient'][1]
n,m=298,298*298

def getx0_mid():
    x0 = np.zeros([m])
    for i0 in range(n):
        for j0 in range(n):
            k = i0 * n + j0
            if j0 == 0:
                x0[k] = vc[i0 + 1][0] + gra_x[i0 + 1][j0]
            elif j0 == 1:
                x0[k] = vc[i0 + 1][0] + gra_x[i0 + 1][j0] * 2
            else:
                x0[k] = x0[k - 2] + gra_x[i0 + 1][j0] * 2
    return x0.reshape((m, 1))