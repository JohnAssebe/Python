from PIL import Image
img=Image.open('zophie.jpg')
img.rotate(90).save("rotate90.jpg")
img.rotate(6,expand=True).save('rotated_expand.png')
