# This prog distributes the data set into respective test and training folders

import argparse
import os
# todo:call the populate_images.py  save taken pictures from opencv with face detection that will save only the
#  region of Interest to a file


# Write the working code for the  populate images that integrates the whole as

import os

# gets current working directory


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# look for a directory named Images in the CWD
image_dir = os.path.join(BASE_DIR, "images")
print("Found Image directory is %s" % image_dir)

##This class should have a function that immediately saves the images to a tmp directory.


# Already done for us supposed to be how to separated into training data from a set of images



# todo: locate the path [../images/<new_user>/Train & validate data folders

# find an algorithm that is able to randomly move the data into respective folders
# through splitting via input eg [1,2,3,4,5,6] are the images of a login user
#  the algorithm will try to randomly mix the numbers and then add them separately into respective foldrer [validation(2,4,6), training(5,1,3)]

# locating path of the training and validation data


# todo:done: 1. take images of roi's
#			2. save to a created images_tmp_dir that the populate_imgs is saved and should be have an identifier that is passed that creates the user directory by name. can use pickle to save the identifier name when code is passed from one tkinter window frame to another
