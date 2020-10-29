from PIL import Image
img=Image.open('zophie.jpg')
cropped=img.crop((200,400,500,700))
cropped.save("croppedImage.jpg")
