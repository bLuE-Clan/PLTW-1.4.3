'''
JDoe_JSmith_1_4_3: Change pixels in an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

###
# Make a rectangle of pixels yellow
###
  
height = len(img)
width = len(img[0])
for r in range(420, 470):
    for c in range(135, 165):
        if sum(img[r][c])>400: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[0, 255, 0] # R + B = magenta

  
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()