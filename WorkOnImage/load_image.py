from PIL import Image
image=Image.open('zophie.jpg')
print(image.format)
print(image.size)
print(image.filename)
print(image.format_description)
image.save("zophie.jpg")
