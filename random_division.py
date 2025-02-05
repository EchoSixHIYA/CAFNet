import os
import random
import shutil


def moveFile(input1, input2, save1, save2):
    pathDir = os.listdir(input1)
    random.seed(1)
    picknumber = 120    # number of test dataset
    sample = random.sample(pathDir, picknumber)
    print(sample)
    list_len = len(sample)
    print(list_len)
    list = []
    for i in range(len(sample)):
        list.append(sample[i].split('.')[0])
    print(list)
    for flie_name in list:
        path_img = os.path.join(input1, flie_name + '.jpg')
        shutil.move(path_img, save1)
        path_lab = os.path.join(input2, flie_name + '.jpg')
        shutil.move(path_lab, save2)


if __name__ == '__main__':
    input_path1 = 'data/kvasir-SEG/Train/images/'
    input_path2 = 'data/kvasir-SEG/Train/masks/'
    save_img = 'data/kvasir-SEG/Test/images/'
    save_lab = 'data/kvasir-SEG/Test/masks/'
    if not os.path.exists(save_lab):
        os.makedirs(save_lab)
    if not os.path.exists(save_img):
        os.makedirs(save_img)
    moveFile(input_path1, input_path2, save_img, save_lab)
