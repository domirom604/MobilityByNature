from PIL import Image
import os
import glob
a=25
path='C:/Users/dromanow/Desktop/Znak/New'

pathT='C:/Users/dromanow/Desktop/finall'

# C:\Users\dromanow\Desktop\Znak
# images = glob.glob("Images/*.jpg")
images = glob.glob('C:/Users/dromanow/Desktop/Znak/New/*.png')
# for image in images:
#     with open(image, 'rb') as file:
#         img = Image.open(file)
#         # new_image = img.resize((256, 256))
#         # new_image = new_image.rotate(-90)
#         path_to_save=path+"/"+str(a)+".png"
#         img.save(path_to_save)
#         a+=1

# for image in images:
#     with open(image, 'rb') as file:
#         img = Image.open(file)
#         os.mkdir(pathT+"/"+str(a)+"_json")
#         path_to_save=pathT+"/"+str(a)+"_json"+"/"+str(a)+".png"
#         img.save(path_to_save)
#         a+=1

for b in range (107,108):
    old=pathT+"/"+ str(b) + "_json" + "/"+ str(b)+".png"
    new = pathT + "/" + str(b) + "_json" + "/" + "img"+ ".png"
    os.rename(old, new)

    with open(new, 'rb') as file:
        img = Image.open(file)

        path_to_save=pathT + "/" + str(b) + "_json" + "/" + "label"+ ".png"
        img.save(path_to_save)

    b += 1
