import os
import numpy as np
import torch
from models.IFRNet import Model
from utils import read
from imageio import mimsave
from PIL import Image
import cv2
import sys
import shutil
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
torch.cuda.set_device(device)
model = Model().cuda().eval()
model.load_state_dict(torch.load('./checkpoints/IFRNet/IFRNet_GoPro.pth'))
i= 4*int(sys.argv[1])
offset= int(sys.argv[2])
prev_img = read("./res_frames/frame"+str(offset+i)+"_30.png")
next_img = read("./res_frames/frame"+str(offset+i+1)+"_30.png")
tensor_img_prev = (torch.tensor(prev_img.transpose(2, 0, 1)).float() / 255.0).unsqueeze(0).cuda()
tensor_img_next = (torch.tensor(next_img.transpose(2, 0, 1)).float() / 255.0).unsqueeze(0).cuda()
tensor_img_pred = torch.tensor(1/2).view(1, 1, 1, 1).float().cuda()
imgt_pred = model.inference(tensor_img_prev, tensor_img_next, tensor_img_pred)
imgt_pred_np = (imgt_pred[0].data.permute(1, 2, 0).cpu().numpy() * 255.0).astype(np.uint8)
shutil.copy("./res_frames/frame"+str(offset+i)+"_240.png","./compare_frames/frame"+str(offset+i)+"_240.png")
image = Image.fromarray(imgt_pred_np.astype('uint8')).convert('RGB')
image.save("./compare_frames/frame"+str(offset+i)+"_30.png")