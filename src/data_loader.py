'''
Name : Rupesh Garsondiya
github : @Rupeshgarsondiya
Organization : L.J University
'''

import os
import cv2
import pandas as pd

class load_data:

    def __init__(self):
        pass

    def load_data(self):
        path = 'data/raw'

        image_list = os.listdir(path)

        # image extension
        image_extensions = ('.jpg', '.jpeg', '.png', '.bmp' ,'.tiff ','.gif')

        for i in image_list:
            if i.endswith(image_extensions):
                img = cv2.imread(i)
                print(img.shape)



