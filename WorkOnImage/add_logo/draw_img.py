from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
import os
try:
  os.makedirs('Draw_image')
except FileExistsError:
    pass
img_new=Image.new("RGBA",(350,350),"white")
draw_img=ImageDraw.Draw(img_new)
draw_img.point(((1,2),(2,1),(4,5)),fill='red')
draw_img.line([2,3,4,5,6,7,8,9],fill='black')
draw_img.polygon([15,16,30,56,40,50,70,12],fill='blue',outline="red")
img_new.save(os.path.join("Draw_image","drawImage.png"))
print("Done go to Draw_image folder to see the image")
