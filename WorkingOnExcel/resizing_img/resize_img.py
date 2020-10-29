from PIL import Image
img=Image.open('zophie.jpg')
width,height=img.size
resized_img=img.resize((int(width/2),int(height/2)))
resized_img.save("resized_img.jpg")
