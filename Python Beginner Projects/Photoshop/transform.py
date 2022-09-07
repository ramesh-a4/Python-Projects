from image import Image
import png
import numpy as np
def adjust_brightness(image,factor):
    #scaling the values by factor
    #image is drakened if the value is less than 1 and brightened if the value is greater than 1
    x_pixels,y_pixels,num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_img.array[x,y,c] = image.array[x,y,c] * factor
    return new_img

def adjust_contrast(image,factor,mid = 0.5):
    #contrasting of the image is done by decreaseing the value by mid value, then scaleing by factor 
    # and then by increaseing by the mid value
    x_pixels,y_pixels,num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_img.array[x,y,c] = (image.array[x,y,c]-mid) * factor + mid
    return new_img

def blur(image,kernel_size):
    #kernel size takes account of number of pixels inorder to blur
    #kernel size should be entere in odd numbers
    #kernel size is taken and divided into two halves, half at bottom and half at top or(right/left)
    x_pixels,y_pixels,num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)

    neighbor_range = kernel_size//2
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbor_range),min(x_pixels-1,x+neighbor_range)+1):
                    for y_i in range(max(0,y-neighbor_range),min(y_pixels-1,y+neighbor_range)+1):
                        total += image.array[x_i,y_i,c]
                        new_img.array[x,y,c] = total / (kernel_size**2) #average

    return new_img

if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # brightened_img = adjust_brightness(lake,2)
    # brightened_img.write_image('brightened_image.png')

    # contrasted_img = adjust_contrast(lake,0.7)
    # contrasted_img.write_image("conrasted_image.png")

    blur_img = blur(city,7)
    blur_img.write_image("blured image.png")