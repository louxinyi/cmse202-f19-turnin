from PIL import Image 
import numpy as np
oscar = Image.open("oscar.png")
oscar_grey = oscar.convert('L')
oscar_asarray = np.asarray(oscar_grey)

def convolve(image_array, mask, div=1, whiten=0):
    new_value = []
    for i in range(image_array.shape[0]-2):
        for j in range(image_array.shape[1]-2):
            a = image_array[i,j] * mask[0,0]
            b = image_array[i+1,j] * mask[1,0]
            c = image_array[i+2,j] * mask[2,0]
            d = image_array[i,j+1] * mask[0,1]
            e = image_array[i+1,j+1] * mask[1,1]
            f = image_array[i+2,j+1] * mask[2,1]
            g = image_array[i,j+2] * mask[0,2]
            h = image_array[i+1,j+2] * mask[1,2]
            k = image_array[i+2,j+2] * mask[2,2]
            
            destin = (a+b+c+d+e+f+g+h+k+whiten)/div
            if destin > 255:
                destin == 255
            if destin < 0:
                destin == 0
            new_value.append(destin)
            
    new_array = np.reshape(new_value,(image_array.shape[0]-2,image_array.shape[1]-2))
    new_array = new_array.astype('uint8')
    new_pic = Image.fromarray(new_array)
    
    return new_pic