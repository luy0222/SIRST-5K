import os
from PIL import Image

image_Path_1 = 'Demos/mix/0.1'
save_Path_1 = 'Demos/output/0.1_32_images'


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
create_folder(save_Path_1)




def rot_patch_3(save_path,image_path, coordinate,k, index):
    img = Image.open(image_path)
    width, height = img.size
    base_name = os.path.basename(image_path)
    base_name, _ = os.path.splitext(base_name)

    # Create patch
    if  (coordinate[0] >= 1 and coordinate[0] <= 255) and (coordinate[1] >= 1 and coordinate[1] <= 255):
        a = (coordinate[0]-1, coordinate[1]-1, coordinate[0]+1, coordinate[1]+1)
    elif coordinate[0] < 1  and (coordinate[1] >= 1 and coordinate[1] <= 255):
        a = (0, coordinate[1] - 1, 2, coordinate[1] + 1)
    elif  coordinate[0] > 255 and (coordinate[1] >= 1 and coordinate[1] <= 255):
        a = (254, coordinate[1]-1, 256, coordinate[1]+1)
    elif  (coordinate[0] >= 1 and coordinate[0] <= 255) and coordinate[1] < 1 :
        a = (coordinate[0]-1, 0, coordinate[0]+1, 2)
    elif  (coordinate[0] >= 1 and coordinate[0] <= 255) and  coordinate[1] > 255:
        a = (coordinate[0]-1, 254, coordinate[0]+1, 256)
    elif  coordinate[0] < 1  and coordinate[1] < 1 :
        a= (0, 0, 2, 2)
    elif   coordinate[0] > 255 and coordinate[1] > 255:
        a = (254,254, 256, 256)
    elif  coordinate[0] < 1  and  coordinate[1] > 255:
        a = (0, 254, 2,256)
    elif coordinate[1] < 1  and  coordinate[0] > 255 :
        a = (254, 0, 256,2)

    patch = img.crop(a)

    # flip patch
    flipped_patch = patch.rotate(90 * k)

    new_img = Image.new('RGB', (width, height))
    new_img.paste(img, (0, 0))
    new_img.paste(flipped_patch, a)
    # save picture
    new_img.save(os.path.join(save_path, "{}_k{}_j{}.png".format(base_name, k, index)))

def rot_patch_5(save_path,image_path, coordinate,k, index):
    img = Image.open(image_path)
    width, height = img.size
    base_name = os.path.basename(image_path)
    base_name, _ = os.path.splitext(base_name)
    if  (coordinate[0] >= 2 and coordinate[0] <= 254) and (coordinate[1] >= 2 and coordinate[1] <= 254):
        a = (coordinate[0]-2, coordinate[1]-2, coordinate[0]+2, coordinate[1]+2)
    elif coordinate[0] < 2  and (coordinate[1] >= 2 and coordinate[1] <= 254):
        a = (0, coordinate[1] - 2, 4, coordinate[1] + 2)
    elif  coordinate[0] > 254 and (coordinate[1] >= 2 and coordinate[1] <= 254):
        a = (252, coordinate[1]-2, 256, coordinate[1]+2)
    elif  (coordinate[0] >= 2 and coordinate[0] <= 254) and coordinate[1] < 2 :
        a = (coordinate[0]-2, 0, coordinate[0]+2, 4)
    elif  (coordinate[0] >= 2 and coordinate[0] <= 254) and  coordinate[1] > 254:
        a = (coordinate[0]-2, 252, coordinate[0]+2, 256)
    elif  coordinate[0] < 2  and coordinate[1] < 2 :
        a= (0, 0, 4, 4)
    elif   coordinate[0] > 254 and coordinate[1] > 254:
        a = (252,252, 256, 256)
    elif  coordinate[0] < 2  and  coordinate[1] > 254:
        a = (0, 252, 4,256)
    elif coordinate[1] < 2  and  coordinate[0] > 254 :
        a = (252, 0, 256,4)
    patch = img.crop(a)
    flipped_patch = patch.rotate(90 * k)
    new_img = Image.new('RGB', (width, height))
    new_img.paste(img, (0, 0))
    new_img.paste(flipped_patch, a)
    new_img.save(os.path.join(save_path, "{}_k{}_j{}.png".format(base_name, k, index)))

def rot_patch_7(save_path,image_path, coordinate,k, index):
    img = Image.open(image_path)
    width, height = img.size
    base_name = os.path.basename(image_path)
    base_name, _ = os.path.splitext(base_name)
    if  (coordinate[0] >= 3 and coordinate[0] <= 253) and (coordinate[1] >= 3 and coordinate[1] <= 253):
        a = (coordinate[0]-3, coordinate[1]-3, coordinate[0]+3, coordinate[1]+3)
    elif coordinate[0] < 3  and (coordinate[1] >= 3 and coordinate[1] <= 253):
        a = (0, coordinate[1] - 3, 6, coordinate[1] + 3)
    elif  coordinate[0] > 253 and (coordinate[1] >= 3 and coordinate[1] <= 253):
        a = (250, coordinate[1]-3, 256, coordinate[1]+3)
    elif  (coordinate[0] >= 3 and coordinate[0] <= 253) and coordinate[1] < 3 :
        a = (coordinate[0]-3, 0, coordinate[0]+3, 6)
    elif  (coordinate[0] >= 3 and coordinate[0] <= 253) and  coordinate[1] > 253:
        a = (coordinate[0]-3, 250, coordinate[0]+3, 256)
    elif  coordinate[0] < 3  and coordinate[1] < 3 :
        a= (0, 0, 6, 6)
    elif   coordinate[0] > 253 and coordinate[1] > 253:
        a = (250,250, 256, 256)
    elif  coordinate[0] < 3  and  coordinate[1] > 253:
        a = (0, 250, 6 ,256)
    elif coordinate[1] < 3  and  coordinate[0] > 253 :
        a = (250, 0, 256,6)
    patch = img.crop(a)
    flipped_patch = patch.rotate(90 * k)
    new_img = Image.new('RGB', (width, height))
    new_img.paste(img, (0, 0))
    new_img.paste(flipped_patch, a)
    new_img.save(os.path.join(save_path,"{}_k{}_j{}.png".format(base_name,k,index)))

def rot_patch_9(save_path,image_path, coordinate,k, index):
    img = Image.open(image_path)
    width, height = img.size
    base_name = os.path.basename(image_path)
    base_name, _ = os.path.splitext(base_name)
    if  (coordinate[0] >= 8 and coordinate[0] <= 248) and (coordinate[1] >= 8 and coordinate[1] <= 248):
        a = (coordinate[0]-4, coordinate[1]-4, coordinate[0]+4, coordinate[1]+4)
    elif coordinate[0] < 8  and (coordinate[1] >= 8 and coordinate[1] <= 248):
        a = (0, coordinate[1] - 4, 8, coordinate[1] + 4)
    elif  coordinate[0] > 248 and (coordinate[1] >= 8 and coordinate[1] <= 248):
        a = (248, coordinate[1]-4, 256, coordinate[1]+4)
    elif  (coordinate[0] >= 8 and coordinate[0] <= 248) and coordinate[1] < 8 :
        a = (coordinate[0]-4, 0, coordinate[0]+4, 8)
    elif  (coordinate[0] >= 8 and coordinate[0] <= 248) and  coordinate[1] > 248:
        a = (coordinate[0]-4, 248, coordinate[0]+4, 256)
    elif  coordinate[0] < 8  and coordinate[1] < 8 :
        a= (0, 0, 8, 8)
    elif   coordinate[0] > 248 and coordinate[1] > 248:
        a = (248,248, 256, 256)
    elif  coordinate[0] < 8  and  coordinate[1] > 248:
        a = (0, 248, 8,256)
    elif coordinate[1] < 8  and  coordinate[0] > 248 :
        a = (248, 0, 256,8)
    patch = img.crop(a)
    flipped_patch = patch.rotate(90 * k)
    new_img = Image.new('RGB', (width, height))
    new_img.paste(img, (0, 0))
    new_img.paste(flipped_patch, a)
    new_img.save(os.path.join(save_path,"{}_k{}_j{}.png".format(base_name,k,index)))

def rot_patch_32(save_path,image_path, coordinate,k, index):
    img = Image.open(image_path)
    width, height = img.size
    base_name = os.path.basename(image_path)
    base_name, _ = os.path.splitext(base_name)
    if  (coordinate[0] >= 32 and coordinate[0] <= 224) and (coordinate[1] >= 32 and coordinate[1] <= 224):
        a = (coordinate[0]-16, coordinate[1]-16, coordinate[0]+16, coordinate[1]+16)
    elif coordinate[0] < 32  and (coordinate[1] >= 32 and coordinate[1] <= 224):
        a = (0, coordinate[1] - 16, 32, coordinate[1] + 16)
    elif  coordinate[0] > 224 and (coordinate[1] >= 32 and coordinate[1] <= 224):
        a = (224, coordinate[1]-16, 256, coordinate[1]+16)
    elif  (coordinate[0] >= 32 and coordinate[0] <= 224) and coordinate[1] < 32 :
        a = (coordinate[0]-16, 0, coordinate[0]+16, 32)
    elif  (coordinate[0] >= 32 and coordinate[0] <= 224) and  coordinate[1] > 224:
        a = (coordinate[0]-16, 224, coordinate[0]+16, 256)
    elif  coordinate[0] < 32  and coordinate[1] < 32 :
        a= (0, 0, 32, 32)
    elif   coordinate[0] > 224 and coordinate[1] > 224:
        a = (224,224, 256, 256)
    elif  coordinate[0] < 32  and  coordinate[1] > 224:
        a = (0, 224, 32,256)
    elif coordinate[1] < 32  and  coordinate[0] > 224 :
        a = (224, 0, 256, 32)
    patch = img.crop(a)
    flipped_patch = patch.transpose(Image.FLIP_LEFT_RIGHT).rotate(90 * k)
    new_img = Image.new('RGB', (width, height))
    new_img.paste(img, (0, 0))
    new_img.paste(flipped_patch, a)
    new_img.save(os.path.join(save_path,"{}_k{}_j{}.png".format(base_name,k,index)))



with open('coordinates.txt', 'r') as file:
    file = file.readlines()
    imgNames_l = os.listdir(image_Path_1)
    imgNames_l = sorted(imgNames_l)
    imgNames_s = [item[:6] for item in imgNames_l]
    images = []
    for line in file:
        for img in imgNames_s:
            if file.index(line) == imgNames_s.index(img):
                str_list = (line.strip(' '))
                str_list = [eval(t) for t in str_list.split('|')]
                for j in str_list:
                    for k in range(4):
                            rot_patch_32(os.path.join(save_Path_1),
                                        os.path.join(image_Path_1, "{}.png".format(imgNames_s[imgNames_s.index(img)])),
                                        str_list[str_list.index(j)], k,str_list.index(j))
                            print('save image', imgNames_s[imgNames_s.index(img)], save_Path_1)
