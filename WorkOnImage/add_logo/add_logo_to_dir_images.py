'''
@Author:Yohannes Assebe
add logo to all image format in the folder
'''
from PIL import Image
import os
catlogo=Image.open(r'cat_logo\catlogo.png')
size_limit=500000
try:
        os.makedirs("with_logo")
except FileExistsError:
    pass
for file in os.listdir('.'):
    if file.lower().endswith('.jpg') or file.lower().endswith('.png') or file.lower().endswith('.bmp') or file.lower().endswith('.gif'):
        catlogo_resized=catlogo.resize((200,200))
        logo_width,logo_height=catlogo_resized.size
        file_name=file
        last_index=file_name.find('.')
        file=Image.open(file)
        width,height=file.size
        if width*height<size_limit:
            file=file.resize((300,300))
            width,height=file.size
            catlogo_resized=catlogo.resize((50,50))
            logo_width,logo_height=catlogo_resized.size
        file=file.copy()
        file.paste(catlogo_resized,(width-logo_width,height-logo_height),catlogo_resized)
        if file_name.endswith('.jpg'):
               file.save(os.path.join("with_logo",file_name[:last_index]+".jpg"))
        elif(file_name.endswith('.png')):
              file.save(os.path.join("with_logo",file_name[:last_index]+".png"))
        elif(file_name.endswith('.gif')):
              file.save(os.path.join("with_logo",file_name[:last_index]+".gif"))
        else:
              file.save(os.path.join("with_logo",file_name[:last_index]+".bmp"))
print("Done thanks for using")
        
            
        
    
