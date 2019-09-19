import numpy as np
from scipy.io import loadmat
from PIL import Image

im=Image.open('ground_truth.png')
im_nw=im.convert('L')
im_nw.save("truth.png")
