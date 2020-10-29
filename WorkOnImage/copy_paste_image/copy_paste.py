from PIL import Image
img=Image.open('zophie.jpg')
img2=Image.open('parrot.jpg')
copied_img=img.copy()
cropped_img=img.crop((300,300,600,600))
crooped_parrot=img2.crop((230,100,600,400))
copied_img.paste(crooped_parrot,(0,0))
copied_img.paste(cropped_img,(0,800))
copied_img.save("copy_paste.jpg")
