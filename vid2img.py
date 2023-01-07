import cv2
import sys
path= sys.argv[1]
vidcap = cv2.VideoCapture(path)
success,image = vidcap.read()
count = 1
while success:
  cv2.imwrite("./imgs/frame%d.png" % count, image)  #frame to img      
  success,image = vidcap.read()
  count=count+1
print(count)
