import tensorflow as tf
from tqdm import tqdm
import os
import shutil
import cv2 as cv
import numpy as np
from keras.models import model_from_json
np.random.seed= 123
import random
from GeneratePlatesUsingModes0725 import generate_images1, BATCH_SIZE, load_image_test
from GeneratePlates import list_large_nums_b, list_chars, generate_typical_plates
from GeneratePlates import list_large_nums_b, list_chars, generate_typical_plates
from conf import number_of_plates
from time import sleep

path_combined = r'./combined'
path_ckpts= r'./ckpts'

de=tf.config.experimental.list_physical_devices('GPU')  # de = devices
tf.config.experimental.set_virtual_device_configuration(de[0],[tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])

generate = generate_images1

w = 330
h = 68

path_models= {}
path_jsonmodels= {}
list_models= []

for file in os.listdir(path_ckpts):
    if 'h5' in file:
        name= file.split('.')[0]
        list_models.append(name)
        path_models[name] = os.path.join(path_ckpts, name+'.h5')
    if 'json' in file:
        name= file.split('.')[0]
        path_jsonmodels[name] = os.path.join(path_ckpts, name+'.json')
list_models= [str(el) for el in list_models]

def generate_combineds(n, path_combined):
    for i in tqdm(range(n)):
        n1 = int(np.random.choice(len(list_large_nums_b)))
        n2 = int(np.random.choice(len(list_large_nums_b)))
        n3 = int(np.random.choice(len(list_chars)))
        n4 = int(np.random.choice(len(list_large_nums_b)))
        n5 = int(np.random.choice(len(list_large_nums_b)))
        n6 = int(np.random.choice(len(list_large_nums_b)))
        n7 = int(np.random.choice(len(list_large_nums_b)))
        n8 = 0 #int(np.random.choice(len(list_large_nums_b)) + 1)
        # ===================================================
        path_write, img = generate_typical_plates(n1, n2, n3, n4, n5, n6, n7, n8)
        img_real = cv.resize(img, (w, h))
        img_Blank = cv.imread('Blank2.jpg')
        img_Blank[150:150 + 68, 0:330, :] = img_real
        img_Blank[150:150 + 68, 512:512 + 330, :] = img_real
        
        mapping= {'06':'07', '07':'08', '11':'13', '13':'15', '10':'11', '19':'06', '12':'14', 
          '08':'10', '14':'16', '18':'12', '17':'19'}

        list_wrongs= ['06', '07', '11', '13', '10', '19', '12', '08','14', '18', '17']
        plate_num= path_write.split('/')[-1]
        wrong_part = plate_num[2:4]
        if wrong_part in list_wrongs:
            plate_num = "".join([plate_num[:2], mapping[wrong_part], plate_num[4:]])
        cv.imwrite(os.path.join(path_combined, plate_num), img_Blank)
    

def GenerateResults():
    for n_model, key in enumerate(list_models):
        print(f'==================== Model {n_model + 1}/{len(list_models)}: {key} ====================')
        with open(path_jsonmodels[key], 'r') as json_file_in:
            saved_json= json_file_in.read()
        loaded_model= model_from_json(saved_json)
        loaded_model.load_weights(path_models[key])
#         os.rmdir(path_combined)
        shutil.rmtree(path_combined)
        os.mkdir(path_combined)
        generate_combineds(int(number_of_plates/len(list(list_models))), path_combined)
        for img in tqdm(os.listdir(path_combined)):
            img_file = os.path.join(path_combined, img)
            test_dataset = tf.data.Dataset.list_files(img_file)
            test_dataset = test_dataset.map(load_image_test)
            test_dataset = test_dataset.batch(1)
            for inp, tar in test_dataset.take(1):
                generate(model=loaded_model, test_input=inp,
                                img_name= img.split('.')[0], flag= f'_{key}')

        del loaded_model
        sleep(5)
        

GenerateResults()
