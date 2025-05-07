import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def region_of_interest(img, vertices):
  mask = np.zeros_like(img) # create blank image
  channel_count = img.shape[2] # grab color map from original image
  match_mask_color = (255,) * channel_count #
  cv2.fillPoly(mask, vertices, match_mask_color) # ROI becomes while while outside is black
  masked_image = cv2.bitwise_and(img, mask) # makes ROI visible and keeps outside black
  
  return masked_image

# helps print out image with dimensions instead of the regular imread()
image = mpimg.imread('(insert image name)')

region_of_interest_vertices = [(0,height),(width/2, height/2), (width,height),]

cropped_image = region_of_interest(image, np.array([region_of_interest_vertices], np.int32),)

plt.figure()
plt.imshow(cropped_image)
plt.imshow(image)

gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_RGB2GRAY)

cannyed_image = cv2.Canny(gray_image, 100, 200)

plt.imshow(cannyed_image)
plt.show()
