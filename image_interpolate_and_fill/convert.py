import scipy.io as sio
import pandas as pd
import numpy as np
from PIL import Image
boundary_data=sio.loadmat('boundary_intensity.mat')
boundary_array=boundary_data['image']
np.savetxt("boundary_img.csv",boundary_array,fmt="%d",delimiter=',')

gradient_data=sio.loadmat('gradient_map.mat')
gradient_array=gradient_data['imgradient']
np.savetxt("gradient_map_x.csv",gradient_array[0],fmt="%.1f",delimiter=',')
np.savetxt("gradient_map_y.csv",gradient_array[1],fmt="%.1f",delimiter=',')