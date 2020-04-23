import matplotlib.pyplot as plt
import os, sys
import numpy as np
from PIL import Image # ca c'est pour manipuler des images 
# here you have to put the  Directory_of_binary_files
entries = os.listdir('Directory_of_binary_files')


for  i in entries :
   # print (i)
    directoy=  'Directory_of_binary_files' + i # change Directory_of_binary_files by y the current Directory_of_binary_files
    jpeg =  'Directory_where_to_save_jpeg_files' + i + '.jpeg'  # change the Directory_where_to_save_jpeg_files by the current Directory_where_to_save_jpeg_files
    fichier = np.fromfile(directoy, dtype=np.int32)

    f = np.reshape(fichier, (160,120,3))  # there is 160 ,120 ,3 because its the size of my image 
    im = Image.fromarray(f.astype('uint8'))
    im.save(jpeg)
