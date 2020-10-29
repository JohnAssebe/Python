from PIL import Image,ImageDraw,ImageFont
import os
img=Image.open('zophie.png')
draw=ImageDraw.Draw(img)
width,height=img.size
font_folder="FONT_FOLDER"
#ttf mean truetype file last parameter is font size for text
arial_font=ImageFont.truetype(os.path.join(font_folder,'arial.ttf'),24)
draw.text((width-200,height-100),"Yohannes Assebe",fill='Black',font=arial_font)
img.save(os.path.join('draw_text','img_with_txt.jpg'))
print("Done ")












        
            
        
    
