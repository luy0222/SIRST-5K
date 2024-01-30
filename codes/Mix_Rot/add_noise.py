import os
from einops.layers.torch import Rearrange
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from misc import tensor2img
import cv2
import math

imagePath = 'Demos/input/NUDT-SIRST/images'
noisePath = 'Demos/noise'
savePath_0 = 'Demos/mix/images'
savePath_1 = 'Demos/mix/images0.1'
savePath_2 = 'Demos/mix/images0.2'
savePath_3 = 'Demos/mix/images0.3'
savePath_4 = 'Demos/mix/images0.4'
savePath_5 = 'Demos/mix/images0.5'

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

create_folder(save_Path_0)
create_folder(save_Path_1)
create_folder(save_Path_2)
create_folder(save_Path_3)
create_folder(save_Path_4)
create_folder(save_Path_5)

crop = transforms.Compose([transforms.Resize([256, 256])])
to_patch = Rearrange('b c (h1 h) (w1 w)  -> (b h1 w1) c h w ', h1=8, w1=8)
to_entire = Rearrange('(b h1 w1) c h w  -> b c (h1 h) (w1 w) ', h1=8, w1=8)


imgNames_l = os.listdir(imagePath)
imgNames_l = sorted(imgNames_l)
imgNames_s = [item[:6] for item in imgNames_l]
images = []


# crop image
for imgName in imgNames_l:
    img = Image.open(os.path.join(imagePath, imgName))
    img_tensor = torch.from_numpy((np.array(img) / 255.0)).permute(2, 0, 1)
    img_tensor = crop(img_tensor)
    images.append(img_tensor)


# crop noise
NoiseNames = os.listdir(noisePath)
NoiseNames = sorted(NoiseNames)
Noises = []
for NoiseName in NoiseNames:
    img = Image.open(os.path.join(noisePath, NoiseName))
    img_tensor = torch.from_numpy((np.array(img) / 255.0)).permute(2, 0, 1)
    img_tensor = crop(img_tensor)
    Noises.append(img_tensor)
Noises = torch.stack(Noises)


M = [0.1,0.2,0.3,0.4,0.5]
for i in imgNames_l:
    for m in M:
        index_i = imgNames_l.index(i)
        infuse_image = m * Noises + (1 - m) * images[index_i]
        if M.index(m) == 0:
            cv2.imwrite(os.path.join(savePath_1, "{}.png".format(i)), tensor2img(infuse_image))
        if M.index(m) == 1:
            cv2.imwrite(os.path.join(savePath_2, "{}.png".format(i)), tensor2img(infuse_image))
        if M.index(m) == 2:
            cv2.imwrite(os.path.join(savePath_3, "{}.png".format(i)), tensor2img(infuse_image))
        if M.index(m) == 3:
            cv2.imwrite(os.path.join(savePath_4, "{}.png".format(i)), tensor2img(infuse_image))
        if M.index(m) == 4:
            cv2.imwrite(os.path.join(savePath_5, "{}.png".format(i)), tensor2img(infuse_image))
        print(i, m, 'done')





# rot