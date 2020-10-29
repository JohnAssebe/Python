from PIL import Image
from PIL import ImageColor
image=Image.new('RGBA',(400,400),'gray')
image.save("img_new.png")
image2=Image.new('RGBA',(400,400))
image2.save("transparent_image.png")
image3=Image.new('RGBA',(900,900),"yellow")
image3.save("yellow_image.png")
image4=Image.new('RGBA',(900,900),(120,150,255,255))
image4.save("RGBA_passed_image.png")
