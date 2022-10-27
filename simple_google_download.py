# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:07:04 2021

@author: Nguyen Quyet
"""
from simple_image_download import simple_image_download as simp

response = simp.simple_image_download
response().download('dent car hail storm',50)

import os
import pandas as pd

images_path = [os.path.join('dent_car/', f'{x}') for x in os.listdir('simple_images/dent_car_hail_storm)')]
idx = list(range(0,50))
df = pd.DataFrame({'ID': idx,
                  'images': images_path})
df.to_csv('simple_images/samples3.csv', index=False)


