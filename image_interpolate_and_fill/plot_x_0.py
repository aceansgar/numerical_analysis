import scipy.io as sio
import pandas as pd
import numpy as np
from PIL import Image

x_0=sio.loadmat("x_0.mat")
x_0=x_0['image'][0]
x_0=x_0.reshape((298,298))
x_0_img=Image.fromarray(x_0)
x_0_img=x_0_img.convert('L')
x_0_img.save("x_0.png")
