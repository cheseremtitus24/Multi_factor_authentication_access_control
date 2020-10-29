import os

import cv2

'''
This code detects probe images and locks onto the ROI and 
saves the training data into the ../images/<new_user>/ folder
'''


# should be a function that takes in the userid for folder creation and the destination path
def training_data_set(user_id):
    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
    cap = cv2.VideoCapture(0)

    while True:
        # capture frame by frame

        ret, frame = cap.read()

        ### no capture image available

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray = cv2.cvtColor(frame, cv2.C)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        # todo: before saving the image it must first create folder with the particular user
        # identifier

        # gets current working directory
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # look for a directory named Images in the CWD
        image_dir = os.path.join(BASE_DIR, "img_tmp_dir")
        # print("Found Image directory is %s" % image_dir)

        # todo: create a folder that bears the passed in user_id from where the images data set will be saved
        path_to_save = os.path.join(image_dir, user_id)
        if not os.path.exists(path_to_save):
            os.makedirs(path_to_save)
            print("creating user directory")

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]  # ycord_start,ycord_end
            roi_color = frame[y:y + h, x:x + w]

            # save the image as gray scale (save in a loop)
            for i in range(30):
                img_item = str(i) + '.png'
                destination_image_path = os.path.join(path_to_save,img_item)
                #todo: how to save an image to a particular folder

                cv2.imwrite(destination_image_path, roi_gray)

            color = (255, 0, 0)  # BGR
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        # display the resulting frame
        cv2.imshow('frame', frame)
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    training_data_set("cheserem")