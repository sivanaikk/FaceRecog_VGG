import os
os.system("tput setaf 34")
print("WAIT TO ENTER INTO PREDICTION STEP .....")
os.system("tput setaf 8")

from keras.models import load_model
from keras.preprocessing import image
import numpy as np


model = load_model('face_recog.h5')

os.system("tput setaf 27")
print("Copy and Paste the image HERE to predict .....")
while True :
    os.system("tput setaf 11")
    file = input("Enter the absolute path to photo :")
    img_width, img_height = 224, 224
    img = image.load_img(file , target_size = (img_width, img_height))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)

    pred = model.predict(img)

    if pred[0][0] == 1.0 :
        print('You are Bharath')
    elif pred[0][1] == 1.0 :
        print('You are Charan.')
    else : 
    	print('You are Siva')
    enter = input("Enter 0 to exit :")
    if enter == 0 :
            exit()
            
