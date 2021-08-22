import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os



cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,640)
cap.set(cv2.CAP_PROP_FPS , 60)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

mylist = os.listdir("")
print(mylist)
imglist = []

for imgpath in mylist:
    img = cv2.imread(f'Back_ground/{imgpath}')
    imglist.append(img)
print(len(mylist))

indexImg = 0

while True:
    success, img = cap.read()


    imgout = segmentor.removeBG(img,imglist[indexImg],threshold=0.55)
    imgStacked = cvzone.stackImages([img,imgout],2,1)
    fps, imgStacked = fpsReader.update(imgStacked,color = (0,0,255))
    print(indexImg)


    cv2.imshow("VIDEO",img)
    cv2.imshow("IMAGE OUT",imgStacked)
    key = cv2.waitKey(1)
    if key == ord("a"):
        indexImg -=1
    elif key == ord("b"):
        indexImg +=1
    elif key == ord("q"):
        break
