


from pyzbar.pyzbar import decode
import numpy as np
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))

    for barcode in decode(img):


        ###GETTING THE DATA######
        my_data = barcode.data.decode('utf-8')
        print(my_data)


        ##### GETTING THE POINTS#####
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))


        ####### PLOTING THE POLYGEN####
        cv2.polylines(img,[pts],True,(255,0,255),5)


        ######PRINTING THE DATA####
        pts2 = barcode.rect
        cv2.putText(img,my_data,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0),2)


    cv2.imshow("Result", img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
         break



