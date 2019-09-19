import scipy.io as sio
import pandas as pd
import numpy as np
from PIL import Image

inner_data=sio.loadmat("img_array_inner.mat")
img_array_inner=inner_data['img_array_inner']
img_array_inner=img_array_inner.reshape((298,298))
sio.savemat("img_array_inner.mat",{'img_array_inner':img_array_inner})


