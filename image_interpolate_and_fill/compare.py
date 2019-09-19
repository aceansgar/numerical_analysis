import scipy.io as sio
import pandas as pd
import numpy as np
from PIL import Image
res_img_file="res_steepest.png"

ground_truth_img=Image.open("truth.png")
gr_array=np.asarray(ground_truth_img)
res_img=Image.open(res_img_file)
res_array=np.asarray(res_img)
n=300

diff=0
for i in range(n):
    for j in range(n):
        diff+=abs(res_array[i][j]-gr_array[i][j])

print("difference is: "+str(diff))