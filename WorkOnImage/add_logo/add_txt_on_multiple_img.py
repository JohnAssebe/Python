from PIL import Image,ImageFont,ImageDraw
import os
text=input("please enter text to write on the image: ")
for file in os.listdir('.'):
    if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
        file_name=file
        last_index=file_name.find('.')
        file=Image.open(file)
        img_draw=ImageDraw.Draw(file)
        width,height=file.size
        font_folder="FONT_FOLDER"
        arial=ImageFont.truetype(os.path.join(font_folder,'arial.ttf'),20)
        img_draw.text((width-len(text)*20,height-len(text)*10),text,fill="Black",font=arial)
        if file_name.endswith('.jpg'):
               file.save(os.path.join("draw_text",file_name[:last_index]+".jpg"))
        else:
              file.save(os.path.join("draw_text",file_name[:last_index]+".png"))  
print("Done :) see images in draw_text folder")
