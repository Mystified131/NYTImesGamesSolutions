import numpy as np
import random
import cv2

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

for ctr in range(1,6):
    prob = (ctr*15)/100

    print("")
    
    print("Working on image: ", ctr)

    image = cv2.imread('image.jpg', 0) # Only for grayscale image
    noise_img = sp_noise(image, prob)

    outstr = "noiseimg." + str(ctr) + ".jpg"
    cv2.imwrite(outstr, noise_img)