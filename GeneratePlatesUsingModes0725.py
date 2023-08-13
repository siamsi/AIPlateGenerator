import tensorflow as tf
from tqdm import tqdm
import os
import cv2 as cv
import numpy as np
from keras.models import model_from_json
np.random.seed= 123
import random
from conf import path_results

#de=tf.config.experimental.list_physical_devices('GPU')  # de = devices
#tf.config.experimental.set_virtual_device_configuration(de[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=512)])

import matplotlib.pyplot as plt
BUFFER_SIZE = 400
BATCH_SIZE = 16
IMG_WIDTH = 512
IMG_HEIGHT = 512

def load(image_file):
    image = tf.io.read_file(image_file)
    image = tf.io.decode_jpeg(image)
    w = tf.shape(image)[1]
    w = w // 2
    input_image = image[:, w:, :]
    real_image = image[:, :w, :]
    input_image = tf.cast(input_image, tf.float32)
    real_image = tf.cast(real_image, tf.float32)
    return input_image, real_image

def resize(input_image, real_image, height, width):
    input_image = tf.image.resize(input_image, [height, width], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    real_image = tf.image.resize(real_image, [height, width], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    return input_image, real_image

def random_crop(input_image, real_image):
    stacked_image = tf.stack([input_image, real_image], axis=0)
    cropped_image = tf.image.random_crop(stacked_image, size=[2, IMG_HEIGHT, IMG_WIDTH, 3])
    return cropped_image[0], cropped_image[1]

def normalize(input_image, real_image):
    input_image = (input_image / 127.5) - 1
    real_image = (real_image / 127.5) - 1
    return input_image, real_image

@tf.function()
def random_jitter(input_image, real_image):
    input_image, real_image = resize(input_image, real_image, 512, 512)
    if tf.random.uniform(()) > 0.5:
        input_image = tf.image.flip_left_right(input_image)
        real_image = tf.image.flip_left_right(real_image)
    return input_image, real_image

def load_image_test(image_file):
    input_image, real_image = load(image_file)
    input_image, real_image = resize(input_image, real_image,IMG_HEIGHT, IMG_WIDTH)
    input_image, real_image = normalize(input_image, real_image)
    return input_image, real_image

# Artesh, sabz, zard, s
def generate_images1(model, test_input, img_name= '', flag='1_'):
    prediction = model(test_input, training=True)
    img = np.array(((prediction[0] * 0.5 + 0.5) * 255))
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)[153:213, 1:330, ]
    img= cv.resize(img, (220, 51))
    img_name= img_name.split('_')[0]
    path_out= os.path.join(path_results, f'{img_name}{flag}.jpg')

    cv.imwrite(path_out, img)

# sabz, alef, sd, zf
def generate_images2(model, test_input, img_name= '', flag='1_'):
    prediction = model(test_input)
    plt.figure()
    path_out= os.path.join(path_results[key], f'{flag}{img_name}.jpg')
    plt.imsave(path_out, np.array((prediction[0] + 1) * 127.5, np.uint8)[153:251, 1:439, ])

#==================================================================

