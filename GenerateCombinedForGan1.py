import cv2 as cv
import os
from tqdm import tqdm
import numpy as np
from GeneratePlates import list_large_nums_b, list_chars, generate_typical_plates,generate_sabz_plates,generate_sd_plates
from GeneratePlates import generate_zf_plates, generate_zard_plates, generate_alef_plates, generate_artesh_plates

path_combined = r'./combined'
w = 330
h = 68
for i in tqdm(range(100)):
    n1 = int(np.random.choice(len(list_large_nums_b)))
    n2 = int(np.random.choice(len(list_large_nums_b)))
    n3 = int(np.random.choice(len(list_chars)))
    n4 = int(np.random.choice(len(list_large_nums_b)))
    n5 = int(np.random.choice(len(list_large_nums_b)))
    n6 = int(np.random.choice(len(list_large_nums_b)))
    n7 = int(np.random.choice(len(list_large_nums_b)))
    n8 = int(np.random.choice(len(list_large_nums_b)) + 1)
    # ===================================================
    path_write, img = generate_typical_plates(n1, n2, n3, n4, n5, n6, n7, n8)
    img_real = cv.resize(img, (w, h))
    img_Blank = cv.imread('Blank2.jpg')
    img_Blank[150:150 + 68, 0:330, :] = img_real
    img_Blank[150:150 + 68, 512:512 + 330, :] = img_real
    cv.imwrite(os.path.join(path_combined, path_write.split('/')[-1]), img_Blank)

