import numpy as np
import random
import cv2
import sys
from PIL import Image 

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

print("")

print("Welcome to the image guessing game.")

print("")

print("Each time you input, the noise level will go down by 5 percent on the image.")

print("")

print("Try to guess who or what you are seeing as soon as you can.")

print("")

anslst = ["Ringo Starr", "Ringo", "Starr", "Beatle", "Beatle's Drummer", "A Beatle"]

for ctr in range(10,0,-1):
    
    prob = (ctr*5)/100

    input("Press enter to start: ")

    print("")
    
    print("Working on image intensity: ", ctr)

    image = cv2.imread('image.jpg', 0) # Only for grayscale image
    noise_img = sp_noise(image, prob)

    cv2.imwrite("mysteryimage.jpg", noise_img)

    print("")

    img = Image.open('mysteryimage.jpg')
    
    img.show() 

    ans = input("Look at the jpg in the new tab, and take your best guess as to who or what you see: ")

    print("")

    corr = 0

    for elem in anslst:
        if ans.lower() == elem.lower():
            corr = 1

    if corr > 0:

        print("You are correct! The image is of Ringo Starr, the Beatles' drummer!")

        print("")

        sys.exit()

    if corr == 0:

        print("That is not correct! Keep trying and guessing!")

        print("")
