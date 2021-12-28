from PIL import Image
img=Image.open('zophie.jpg')
img2=Image.open('parrot.jpg')
copied_img=img.copy()
cropped_img=img.crop((300,300,600,600))
cropped_parrot=img2.crop((230,100,600,400))
img_width,img_height=img.size
cropped_img_width,cropped_img_height=cropped_img.size
##cropped_parrot_size=cropped_parrot.size
for left in range(0,img_width,cropped_img_width):
    for top in range(0,img_height,cropped_img_height):
        copied_img.paste(cropped_img,(left,top))
        if(top>cropped_img_height):
            copied_img.paste(cropped_parrot,(left,top))
    
##copied_img.paste(cropped_parrot,(0,0))
##copied_img.paste(cropped_img,(0,800))
copied_img.save("copy_paste3.jpg")
