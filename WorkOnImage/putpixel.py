from PIL import Image,ImageColor
img=Image.new("RGBA",(400,400))
for i in range(400):
    for k in range(200):
        img.putpixel((i,k),(250,250,0))
for i in range(400):
    for k in range(200,400):
        img.putpixel((i,k),ImageColor.getcolor("Gray","RGBA"))
img.save("putpixel.png")
