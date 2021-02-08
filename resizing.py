import cv2
import os
import numpy as np

imageformat = ".jpg"
path = '/home/vijesh/****PROJECT****/i-codes/error+fix'
imfilelist = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(imageformat)]
for el in imfilelist:
    img = cv2.imread(el)
    os.chdir('/home/vijesh')  # head region

    resiz = cv2.resize(img, (206, 270))
    cv2.imwrite(str(el) , resiz)
    cv2.imshow('frame', resiz)
    #cv2.waitKey(30)


# print 'staring frames=',startingframe
# print 'ending frames=',endingframe


cv2.destroyAllWindows()
