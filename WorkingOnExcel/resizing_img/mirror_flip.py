from PIL import Image
img=Image.open('zophie.jpg')
img.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
