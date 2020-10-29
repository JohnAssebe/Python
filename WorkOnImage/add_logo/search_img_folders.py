'''
@Author:Yohannes Assebe
Check it out
'''
from PIL import Image
import os
for folders,subfolders,filenames in os.walk('C:\\'):
    no_of_photos=0
    no_of_nonphotos=0
    for file in filenames:
        try:
            if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg') or file.lower().endswith('.png') or file.lower().endswith('.gif') or file.lower().endswith('.bmp'):
                   img=Image.open(file)
                   width,height=img.size
                   if width>300 and height>300:
                       no_of_photos+=1
                   else:
                       no_of_nonphotos+=1
            else:
                no_of_nonphotos+=1
        except FileNotFoundError:
            pass
    if no_of_photos>no_of_nonphotos:
                print(folders)
            

