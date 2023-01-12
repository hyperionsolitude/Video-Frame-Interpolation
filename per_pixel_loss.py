from PIL import Image
import sys
import numpy as np
import matplotlib.pyplot as plt
import csv
loss = 0
totalframe= int(sys.argv[1])
frameloss=np.zeros(totalframe)
for index in range(1,totalframe+1):
    frameopen1 = Image.open("./compare_frames/frame"+str(4*index)+"_30.png")
    frameopen2 = Image.open("./compare_frames/frame"+str(4*index)+"_240.png")
    predicted_frame = frameopen1.load()
    actual_frame = frameopen2.load()
    widthval = frameopen1.size[0]
    heightval = frameopen1.size[1]
    for width in range(0,widthval):
        for height in range(0,heightval):
            red_channel_diff = abs(actual_frame[width,height][0] - predicted_frame[width,height][0])
            green_channel_diff = abs(actual_frame[width,height][1] - predicted_frame[width,height][1])
            blue_channel_diff = abs(actual_frame[width,height][2] - predicted_frame[width,height][2])
            average_value= (red_channel_diff + green_channel_diff + blue_channel_diff)/3
            loss = loss + average_value
    frameloss[index-1] = loss*100/(widthval*heightval*255)
    loss = 0
file = open("perframeloss.txt", "w+")
content = str(frameloss)
file.write(content)
file.close()
pltarray=np.arange(1,(totalframe+1))
plt.bar(pltarray,frameloss)
plt.xlabel('Frame Number')
plt.ylabel('Value')
plt.title('Absolute Loss Per Frame')
plt.savefig('figure2.png')