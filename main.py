# Python code to convert an image to ASCII image. 
import sys, random, argparse 
import numpy as np 
import math 
  
from PIL import Image 
  

# ref. https://www.geeksforgeeks.org/converting-image-ascii-image-python/

gscale = '@%#*+=-:. '
  
def getAverageL(image):   
    """ 
    Given PIL Image, return average value of grayscale value 
    """
    # get image as numpy array 
    im = np.array(image) 
  
    # get shape 
    w,h = im.shape 
  
    # get average 
    return np.average(im.reshape(w*h)) 
  

def covertImageToAscii(fileName, cols, scale): 
    """ 
    Given Image and dims (rows, cols) returns an m*n list of Images  
    """

    # open image and convert to grayscale 
    image = Image.open(fileName).convert('L') 
  
    # store dimensions 
    W, H = image.size[0], image.size[1] 

    # compute width of tile 
    w = W/cols 
  
    # compute tile height based on aspect ratio and scale 
    h = w/scale 
  
    # compute number of rows 
    rows = int(H/h) 
      
    # ascii image is a list of character strings 
    aimg = [] 
    # generate list of dimensions 
    for j in range(rows): 
        y1 = int(j*h) 
        y2 = int((j+1)*h) 
  
        # correct last tile 
        if j == rows-1: 
            y2 = H 
  
        # append an empty string 
        aimg.append("") 
  
        for i in range(cols): 
  
            # crop image to tile 
            x1 = int(i*w) 
            x2 = int((i+1)*w) 
  
            # correct last tile 
            if i == cols-1: 
                x2 = W 
  
            # crop image to extract tile 
            img = image.crop((x1, y1, x2, y2)) 
  
            # get average luminance 
            avg = int(getAverageL(img)) 
  
            # look up ascii char 
            gsval = gscale[int((avg*9)/255)] 
  
            # append ascii char to string 
            aimg[j] += gsval 
      
    # return txt image 
    return aimg 
  

def main(): 
    imgFile = "1.png"
    scale = 0.5
    cols = 80
  
    aimg = covertImageToAscii(imgFile, cols, scale) 
  
    for row in aimg: 
        print(row) 
    
# call main 
if __name__ == '__main__': 
    main() 


