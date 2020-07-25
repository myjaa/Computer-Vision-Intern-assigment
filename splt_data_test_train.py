import os
import shutil
import random

folder_name=['train','validation']
current=os.getcwd()
try:
    for i in folder_name:
        os.mkdir(os.path.join(current,i))
except:
    pass

image_address = os.path.join(current,'images')
train_address = os.path.join(current, 'train')
validation_address = os.path.join(current, 'validation')

images = os.listdir(image_address)
train_len=int(len(images)*0.8)
validation_len=len(images)-train_len

alternate=0
for image in images:
    if image.endswith('.xml'):
        pass
    else:
        alternate=random.randint(0,1)
        if alternate:
            if len(os.listdir(train_address))<train_len:
                shutil.copyfile(os.path.join(image_address,image), os.path.join(train_address,image))
                shutil.copyfile(os.path.join(image_address, f'{image[:-4]}.xml'), os.path.join(train_address, f'{image[:-4]}.xml'))
            else:
                shutil.copyfile(os.path.join(image_address, image),os.path.join(validation_address, image))
                shutil.copyfile(os.path.join(image_address, f'{image[:-4]}.xml'), os.path.join(validation_address, f'{image[:-4]}.xml'))
        else:
            if len(os.listdir(validation_address)) < validation_len:
                shutil.copyfile(os.path.join(image_address, image),os.path.join(validation_address, image))
                shutil.copyfile(os.path.join(image_address, f'{image[:-4]}.xml'), os.path.join(validation_address, f'{image[:-4]}.xml'))
            else:
                shutil.copyfile(os.path.join(image_address, image),os.path.join(train_address, image))
                shutil.copyfile(os.path.join(image_address, f'{image[:-4]}.xml'), os.path.join(train_address, f'{image[:-4]}.xml'))
