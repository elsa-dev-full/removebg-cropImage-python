
############################ -- Main -- ############################

from PIL import Image
import numpy as np
import scipy as sp
import scipy.ndimage.morphology

def Cropper(start, end):
    for x in range(start, end + 1):
        PUBLIC_IMAGE_NAME = 'img-' + str(x) + '-no-bg'
        im = Image.open('results/removebg/' + PUBLIC_IMAGE_NAME + '.png')
        data = np.asarray(im)
        filled = sp.ndimage.morphology.binary_fill_holes(data)
        objects, num_objects = sp.ndimage.label(filled)
        object_slices =  sp.ndimage.find_objects(objects)

        crop_image = Image.fromarray(data[object_slices[0]])
        crop_image.save('results/cropped/' + PUBLIC_IMAGE_NAME + '-cropped.png')
        
        print('Cropped for img-' + str(x) + '-no-bg.png in cropper.py')

if __name__ == '__main__':
    Cropper(0,45)

############## These are similar cropper function below ##############

# from PIL import Image

# image=Image.open('results/removebg/img-13-no-bg.png')

# imageBox = image.getbbox()
# print(imageBox)
# cropped=image.crop(imageBox)
# cropped.save('results/L_2d_cropped.png')

####################################################################

# from PIL import Image, ImageChops

# def trim(im):
#     bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
#     diff = ImageChops.difference(im, bg)
#     diff = ImageChops.add(diff, diff, 2.0, -100)
#     #Bounding box given as a 4-tuple defining the left, upper, right, and lower pixel coordinates.
#     #If the image is completely empty, this method returns None.
#     bbox = diff.getbbox()
#     print(bg, diff, bbox)
#     if bbox:
#         return im.crop(bbox)

# if __name__ == "__main__":
#     bg = Image.open("results/removebg/img-13-no-bg.png") # The image to be cropped
#     new_im = trim(bg)
#     new_im.save('results/L_2d_cropped_trim.png')

#####################################################################

# import requests
# from PIL import Image
# import numpy as np

# im = Image.open('results/removebg/img-13-no-bg.png')
# im.load()
# image_data = np.asarray(im)
# image_data_bw = image_data.max(axis=2)
# non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
# non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
# print(non_empty_columns, "\n\n", non_empty_rows, "\n\n", image_data)

# cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
# image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]
# new_image = Image.fromarray(image_data_new)
# new_image.save('results/img-13-cropped-PIL.png')

#####################################################################