import os
from models.IFRNet import Model
from utils import read
import imageio
from PIL import Image
import sys
maxframe= int(sys.argv[1])
offset= int(sys.argv[2])
fileList = []
frame_counter=0
for file in range(offset+1,maxframe):
    if (file == 1):
        fileList.append("./res_frames/frame"+str(file)+"_240.png")
        frame_counter = frame_counter +1
    elif (file != 1):
        fileList.append("./res_frames/frame"+str(file)+"_30.png")
        frame_counter = frame_counter +1
    if (file % 4 == 0):
        fileList.append("./res_frames/frame"+str(file)+"_240.png")
        frame_counter = frame_counter +1

writer = imageio.get_writer('./outputs/output.mp4', fps=30)
for im in fileList:
    writer.append_data(imageio.imread(im))
writer.close()
print("The video has been saved at ./outputs/output.mp4")
print("Total Frame of the video is:"+str(frame_counter))
