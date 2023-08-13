import cv2 as cv
import numpy as np
import os
from tqdm import tqdm

#====================================================================================
path_charImages= r'./poorishaban_charachters_0529'
path_backs= r'./Charachters_Poorishaban/backs'
path_Black_nums= r'./Charachters_Poorishaban/Black_nums'
path_alef_nums= r'./Charachters_Poorishaban/White_nums/alef'
path_zf_nums= r'./Charachters_Poorishaban/White_nums/zf'
path_sabz_nums= r'./Charachters_Poorishaban/White_nums/sabz'
path_sd_nums= r'./Charachters_Poorishaban/White_nums/sd'
path_artesh_nums= r'./Charachters_Poorishaban/White_nums/artesh'
path_zard_nums= r'./Charachters_Poorishaban/White_nums/zard'

path_Chars= r'./Charachters_Poorishaban/Chars'
path_results= r'./combined'
#====================================================================================

sefid= cv.imread(os.path.join(path_backs,'sefid.png'))
sefid= cv.resize(sefid, (441, 102))

back_alef= cv.imread(os.path.join(path_backs,'alef.png'))
back_alef= cv.resize(back_alef, (441, 102))

zard= cv.imread(os.path.join(path_backs,'zard.png'))
zard= cv.resize(zard, (441, 102))

zf= cv.imread(os.path.join(path_backs,'zf.png'))
zf= cv.resize(zf, (441, 102))

sd= cv.imread(os.path.join(path_backs,'sd.png'))
sd= cv.resize(sd, (441, 102))

artesh= cv.imread(os.path.join(path_backs,'artesh.png'))
artesh= cv.resize(artesh, (441, 102))

sabz= cv.imread(os.path.join(path_backs,'sabz.png'))
sabz= cv.resize(sabz, (441, 102))
#==============================large b==============================================

large1 = cv.imread(os.path.join(path_Black_nums, '1.jpg'))
large2 = cv.imread(os.path.join(path_Black_nums, '2.jpg'))
large3 = cv.imread(os.path.join(path_Black_nums, '3.jpg'))
large4 = cv.imread(os.path.join(path_Black_nums, '4.jpg'))
large5 = cv.imread(os.path.join(path_Black_nums, '5.jpg'))
large6 = cv.imread(os.path.join(path_Black_nums, '6.jpg'))
large7 = cv.imread(os.path.join(path_Black_nums, '7.jpg'))
large8 = cv.imread(os.path.join(path_Black_nums, '8.jpg'))
large9 = cv.imread(os.path.join(path_Black_nums, '9.jpg'))
large0 = cv.imread(os.path.join(path_Black_nums, '0.jpg'))
#==============================large zard==============================================

large1_zard = cv.imread(os.path.join(path_zard_nums, '1.jpg'))
large2_zard = cv.imread(os.path.join(path_zard_nums, '2.jpg'))
large3_zard = cv.imread(os.path.join(path_zard_nums, '3.jpg'))
large4_zard = cv.imread(os.path.join(path_zard_nums, '4.jpg'))
large5_zard = cv.imread(os.path.join(path_zard_nums, '5.jpg'))
large6_zard = cv.imread(os.path.join(path_zard_nums, '6.jpg'))
large7_zard = cv.imread(os.path.join(path_zard_nums, '7.jpg'))
large8_zard = cv.imread(os.path.join(path_zard_nums, '8.jpg'))
large9_zard = cv.imread(os.path.join(path_zard_nums, '9.jpg'))
large0_zard = cv.imread(os.path.join(path_zard_nums, '0.jpg'))
#================================large alef===============================================
large1_alef = cv.imread(os.path.join(path_alef_nums, '1.jpg'))
large2_alef = cv.imread(os.path.join(path_alef_nums, '2.jpg'))
large3_alef = cv.imread(os.path.join(path_alef_nums, '3.jpg'))
large4_alef = cv.imread(os.path.join(path_alef_nums, '4.jpg'))
large5_alef = cv.imread(os.path.join(path_alef_nums, '5.jpg'))
large6_alef = cv.imread(os.path.join(path_alef_nums, '6.jpg'))
large7_alef = cv.imread(os.path.join(path_alef_nums, '7.jpg'))
large8_alef = cv.imread(os.path.join(path_alef_nums, '8.jpg'))
large9_alef = cv.imread(os.path.join(path_alef_nums, '9.jpg'))
large0_alef = cv.imread(os.path.join(path_alef_nums, '0.jpg'))
#==============================large artesh==============================================
large1_artesh = cv.imread(os.path.join(path_artesh_nums, '1.jpg'))
large2_artesh = cv.imread(os.path.join(path_artesh_nums, '2.jpg'))
large3_artesh = cv.imread(os.path.join(path_artesh_nums, '3.jpg'))
large4_artesh = cv.imread(os.path.join(path_artesh_nums, '4.jpg'))
large5_artesh = cv.imread(os.path.join(path_artesh_nums, '5.jpg'))
large6_artesh = cv.imread(os.path.join(path_artesh_nums, '6.jpg'))
large7_artesh = cv.imread(os.path.join(path_artesh_nums, '7.jpg'))
large8_artesh = cv.imread(os.path.join(path_artesh_nums, '8.jpg'))
large9_artesh = cv.imread(os.path.join(path_artesh_nums, '9.jpg'))
large0_artesh = cv.imread(os.path.join(path_artesh_nums, '0.jpg'))
#===========================large zabz==============================================
large1_sabz = cv.imread(os.path.join(path_sabz_nums, '1.jpg'))
large2_sabz = cv.imread(os.path.join(path_sabz_nums, '2.jpg'))
large3_sabz = cv.imread(os.path.join(path_sabz_nums, '3.jpg'))
large4_sabz = cv.imread(os.path.join(path_sabz_nums, '4.jpg'))
large5_sabz = cv.imread(os.path.join(path_sabz_nums, '5.jpg'))
large6_sabz = cv.imread(os.path.join(path_sabz_nums, '6.jpg'))
large7_sabz = cv.imread(os.path.join(path_sabz_nums, '7.jpg'))
large8_sabz = cv.imread(os.path.join(path_sabz_nums, '8.jpg'))
large9_sabz = cv.imread(os.path.join(path_sabz_nums, '9.jpg'))
large0_sabz = cv.imread(os.path.join(path_sabz_nums, '0.jpg'))
#================================large zf===========================================
large1_zf = cv.imread(os.path.join(path_zf_nums, '1.jpg'))
large2_zf = cv.imread(os.path.join(path_zf_nums, '2.jpg'))
large3_zf = cv.imread(os.path.join(path_zf_nums, '3.jpg'))
large4_zf = cv.imread(os.path.join(path_zf_nums, '4.jpg'))
large5_zf = cv.imread(os.path.join(path_zf_nums, '5.jpg'))
large6_zf = cv.imread(os.path.join(path_zf_nums, '6.jpg'))
large7_zf = cv.imread(os.path.join(path_zf_nums, '7.jpg'))
large8_zf = cv.imread(os.path.join(path_zf_nums, '8.jpg'))
large9_zf = cv.imread(os.path.join(path_zf_nums, '9.jpg'))
large0_zf = cv.imread(os.path.join(path_zf_nums, '0.jpg'))
#===============================latge sd=============================================
large1_sd = cv.imread(os.path.join(path_sd_nums, '1.jpg'))
large2_sd = cv.imread(os.path.join(path_sd_nums, '2.jpg'))
large3_sd = cv.imread(os.path.join(path_sd_nums, '3.jpg'))
large4_sd = cv.imread(os.path.join(path_sd_nums, '4.jpg'))
large5_sd = cv.imread(os.path.join(path_sd_nums, '5.jpg'))
large6_sd = cv.imread(os.path.join(path_sd_nums, '6.jpg'))
large7_sd = cv.imread(os.path.join(path_sd_nums, '7.jpg'))
large8_sd = cv.imread(os.path.join(path_sd_nums, '8.jpg'))
large9_sd = cv.imread(os.path.join(path_sd_nums, '9.jpg'))
large0_sd = cv.imread(os.path.join(path_sd_nums, '0.jpg'))
#====================================================================================
w_large = 40
h_large= 83
large1 = cv.resize(large1, (w_large, h_large))
large2 = cv.resize(large2, (w_large, h_large))
large3 = cv.resize(large3, (w_large, h_large))
large4 = cv.resize(large4, (w_large, h_large))
large5 = cv.resize(large5, (w_large, h_large))
large6 = cv.resize(large6, (w_large, h_large))
large7 = cv.resize(large7, (w_large, h_large))
large8 = cv.resize(large8, (w_large, h_large))
large9 = cv.resize(large9, (w_large, h_large))
large0 = cv.resize(large0, (w_large, h_large))
#=============================
h_small= int(large1.shape[0]*0.83)
w_small = int(large1.shape[1]*0.99)
small1 = cv.resize(large1, (w_small, h_small))
small2 = cv.resize(large2, (w_small, h_small))
small3 = cv.resize(large3, (w_small, h_small))
small4 = cv.resize(large4, (w_small, h_small))
small5 = cv.resize(large5, (w_small, h_small))
small6 = cv.resize(large6, (w_small, h_small))
small7 = cv.resize(large7, (w_small, h_small))
small8 = cv.resize(large8, (w_small, h_small))
small9 = cv.resize(large9, (w_small, h_small))
small0 = cv.resize(large0, (w_small, h_small))
#===================================resize_zard==========================================
large1_zard = cv.resize(large1_zard, (w_large, h_large))
large2_zard = cv.resize(large2_zard, (w_large, h_large))
large3_zard = cv.resize(large3_zard, (w_large, h_large))
large4_zard = cv.resize(large4_zard, (w_large, h_large))
large5_zard = cv.resize(large5_zard, (w_large, h_large))
large6_zard = cv.resize(large6_zard, (w_large, h_large))
large7_zard = cv.resize(large7_zard, (w_large, h_large))
large8_zard = cv.resize(large8_zard, (w_large, h_large))
large9_zard = cv.resize(large9_zard, (w_large, h_large))
large0_zard = cv.resize(large0_zard, (w_large, h_large))
#=============================
small1_zard = cv.resize(large1_zard, (w_small, h_small))
small2_zard = cv.resize(large2_zard, (w_small, h_small))
small3_zard = cv.resize(large3_zard, (w_small, h_small))
small4_zard = cv.resize(large4_zard, (w_small, h_small))
small5_zard = cv.resize(large5_zard, (w_small, h_small))
small6_zard = cv.resize(large6_zard, (w_small, h_small))
small7_zard = cv.resize(large7_zard, (w_small, h_small))
small8_zard = cv.resize(large8_zard, (w_small, h_small))
small9_zard = cv.resize(large9_zard, (w_small, h_small))
small0_zard = cv.resize(large0_zard, (w_small, h_small))
#===================================resize_alef==========================================
large1_alef = cv.resize(large1_alef, (w_large, h_large))
large2_alef = cv.resize(large2_alef, (w_large, h_large))
large3_alef = cv.resize(large3_alef, (w_large, h_large))
large4_alef = cv.resize(large4_alef, (w_large, h_large))
large5_alef = cv.resize(large5_alef, (w_large, h_large))
large6_alef = cv.resize(large6_alef, (w_large, h_large))
large7_alef = cv.resize(large7_alef, (w_large, h_large))
large8_alef = cv.resize(large8_alef, (w_large, h_large))
large9_alef = cv.resize(large9_alef, (w_large, h_large))
large0_alef = cv.resize(large0_alef, (w_large, h_large))
#=============================
small1_alef = cv.resize(large1_alef, (w_small, h_small))
small2_alef = cv.resize(large2_alef, (w_small, h_small))
small3_alef = cv.resize(large3_alef, (w_small, h_small))
small4_alef = cv.resize(large4_alef, (w_small, h_small))
small5_alef = cv.resize(large5_alef, (w_small, h_small))
small6_alef = cv.resize(large6_alef, (w_small, h_small))
small7_alef = cv.resize(large7_alef, (w_small, h_small))
small8_alef = cv.resize(large8_alef, (w_small, h_small))
small9_alef = cv.resize(large9_alef, (w_small, h_small))
small0_alef = cv.resize(large0_alef, (w_small, h_small))
#===================================resize_sabz==========================================
large1_sabz = cv.resize(large1_sabz, (w_large, h_large))
large2_sabz = cv.resize(large2_sabz, (w_large, h_large))
large3_sabz = cv.resize(large3_sabz, (w_large, h_large))
large4_sabz = cv.resize(large4_sabz, (w_large, h_large))
large5_sabz = cv.resize(large5_sabz, (w_large, h_large))
large6_sabz = cv.resize(large6_sabz, (w_large, h_large))
large7_sabz = cv.resize(large7_sabz, (w_large, h_large))
large8_sabz = cv.resize(large8_sabz, (w_large, h_large))
large9_sabz = cv.resize(large9_sabz, (w_large, h_large))
large0_sabz = cv.resize(large0_sabz, (w_large, h_large))
#=============================
small1_sabz = cv.resize(large1_sabz, (w_small, h_small))
small2_sabz = cv.resize(large2_sabz, (w_small, h_small))
small3_sabz = cv.resize(large3_sabz, (w_small, h_small))
small4_sabz = cv.resize(large4_sabz, (w_small, h_small))
small5_sabz = cv.resize(large5_sabz, (w_small, h_small))
small6_sabz = cv.resize(large6_sabz, (w_small, h_small))
small7_sabz = cv.resize(large7_sabz, (w_small, h_small))
small8_sabz = cv.resize(large8_sabz, (w_small, h_small))
small9_sabz = cv.resize(large9_sabz, (w_small, h_small))
small0_sabz = cv.resize(large0_sabz, (w_small, h_small))
#===================================resize_zf==========================================
large1_zf = cv.resize(large1_zf, (w_large, h_large))
large2_zf = cv.resize(large2_zf, (w_large, h_large))
large3_zf = cv.resize(large3_zf, (w_large, h_large))
large4_zf = cv.resize(large4_zf, (w_large, h_large))
large5_zf = cv.resize(large5_zf, (w_large, h_large))
large6_zf = cv.resize(large6_zf, (w_large, h_large))
large7_zf = cv.resize(large7_zf, (w_large, h_large))
large8_zf = cv.resize(large8_zf, (w_large, h_large))
large9_zf = cv.resize(large9_zf, (w_large, h_large))
large0_zf = cv.resize(large0_zf, (w_large, h_large))
#=============================
small1_zf = cv.resize(large1_zf, (w_small, h_small))
small2_zf = cv.resize(large2_zf, (w_small, h_small))
small3_zf = cv.resize(large3_zf, (w_small, h_small))
small4_zf = cv.resize(large4_zf, (w_small, h_small))
small5_zf = cv.resize(large5_zf, (w_small, h_small))
small6_zf = cv.resize(large6_zf, (w_small, h_small))
small7_zf = cv.resize(large7_zf, (w_small, h_small))
small8_zf = cv.resize(large8_zf, (w_small, h_small))
small9_zf = cv.resize(large9_zf, (w_small, h_small))
small0_zf = cv.resize(large0_zf, (w_small, h_small))
#===================================resize_sd==========================================
large1_sd = cv.resize(large1_sd, (w_large, h_large))
large2_sd = cv.resize(large2_sd, (w_large, h_large))
large3_sd = cv.resize(large3_sd, (w_large, h_large))
large4_sd = cv.resize(large4_sd, (w_large, h_large))
large5_sd = cv.resize(large5_sd, (w_large, h_large))
large6_sd = cv.resize(large6_sd, (w_large, h_large))
large7_sd = cv.resize(large7_sd, (w_large, h_large))
large8_sd = cv.resize(large8_sd, (w_large, h_large))
large9_sd = cv.resize(large9_sd, (w_large, h_large))
large0_sd = cv.resize(large0_sd, (w_large, h_large))
#=============================
small1_sd = cv.resize(large1_sd, (w_small, h_small))
small2_sd = cv.resize(large2_sd, (w_small, h_small))
small3_sd = cv.resize(large3_sd, (w_small, h_small))
small4_sd = cv.resize(large4_sd, (w_small, h_small))
small5_sd = cv.resize(large5_sd, (w_small, h_small))
small6_sd = cv.resize(large6_sd, (w_small, h_small))
small7_sd = cv.resize(large7_sd, (w_small, h_small))
small8_sd = cv.resize(large8_sd, (w_small, h_small))
small9_sd = cv.resize(large9_sd, (w_small, h_small))
small0_sd = cv.resize(large0_sd, (w_small, h_small))
#===================================resize_artesh==========================================
large1_artesh = cv.resize(large1_artesh, (w_large, h_large))
large2_artesh = cv.resize(large2_artesh, (w_large, h_large))
large3_artesh = cv.resize(large3_artesh, (w_large, h_large))
large4_artesh = cv.resize(large4_artesh, (w_large, h_large))
large5_artesh = cv.resize(large5_artesh, (w_large, h_large))
large6_artesh = cv.resize(large6_artesh, (w_large, h_large))
large7_artesh = cv.resize(large7_artesh, (w_large, h_large))
large8_artesh = cv.resize(large8_artesh, (w_large, h_large))
large9_artesh = cv.resize(large9_artesh, (w_large, h_large))
large0_artesh = cv.resize(large0_artesh, (w_large, h_large))
#=============================
small1_artesh = cv.resize(large1_artesh, (w_small, h_small))
small2_artesh = cv.resize(large2_artesh, (w_small, h_small))
small3_artesh = cv.resize(large3_artesh, (w_small, h_small))
small4_artesh = cv.resize(large4_artesh, (w_small, h_small))
small5_artesh = cv.resize(large5_artesh, (w_small, h_small))
small6_artesh = cv.resize(large6_artesh, (w_small, h_small))
small7_artesh = cv.resize(large7_artesh, (w_small, h_small))
small8_artesh = cv.resize(large8_artesh, (w_small, h_small))
small9_artesh = cv.resize(large9_artesh, (w_small, h_small))
small0_artesh = cv.resize(large0_artesh, (w_small, h_small))
#====================================================================================
#====================================================================================
dal = cv.imread(os.path.join(path_Chars, 'd.jpg'))
sad = cv.imread(os.path.join(path_Chars, 'sad.jpg'))
sin = cv.imread(os.path.join(path_Chars, 'sin.jpg'))
ya = cv.imread(os.path.join(path_Chars, 'ya.jpg'))

alef = cv.imread(os.path.join(path_Chars, 'alefred.jpg'))
b = cv.imread(os.path.join(path_Chars, 'b.jpg'))
p = cv.imread(os.path.join(path_Chars, 'pgreen.jpg'))
taxi = cv.imread(os.path.join(path_Chars, 'taxi.jpg'))

th = cv.imread(os.path.join(path_Chars, 'thgreen.jpg'))
jim = cv.imread(os.path.join(path_Chars, 'j.jpg'))
z = cv.imread(os.path.join(path_Chars, 'z.jpg'))
r = cv.imread(os.path.join(path_Chars, 'r.jpg'))

shin = cv.imread(os.path.join(path_Chars, 'shcream.jpg'))
ta = cv.imread(os.path.join(path_Chars, 'ta.jpg'))
ein = cv.imread(os.path.join(path_Chars, 'einyellow.jpg'))

f = cv.imread(os.path.join(path_Chars, 'f.jpg'))
gh = cv.imread(os.path.join(path_Chars, 'gh.jpg'))
k = cv.imread(os.path.join(path_Chars, 'k.jpg'))
g = cv.imread(os.path.join(path_Chars, 'g.jpg'))
l = cv.imread(os.path.join(path_Chars, 'l.jpg'))
m = cv.imread(os.path.join(path_Chars, 'm.jpg'))
n = cv.imread(os.path.join(path_Chars, 'n.jpg'))
v = cv.imread(os.path.join(path_Chars, 'v.jpg'))
h = cv.imread(os.path.join(path_Chars, 'h.jpg'))

s= cv.imread(os.path.join(path_Chars, 'sblue.jpg'))
d= cv.imread(os.path.join(path_Chars, 'diblue.jpg'))
c= cv.imread(os.path.join(path_Chars, 'c.jpg'))
# c= cv.resize(c, (int(c.shape[1]*1.1), c.shape[0]))

CharKeyMap= {'alef':'01',
             'b':'02',
             'taxi':'03',
             'jim':'04',
             'dal':'05',
             'sin':'06',
             'sad':'07',
             'ta':'08',
             'ein':'09',
             'gh':'10',
             'l':'11',
             'm':'12',
             'n':'13',
             'v':'14',
             'h':'15',
             'ya':'16',
             'r':'17',
             'k':'18',
             'c':'19',
             'p':'20',
             'g':'22',
             'd':'33',
             's':'34',
             'f':'23',
             'shin':'24',
             'th':'45',
             'z':'26'}
#====================================================================================

list_large_nums_b=[large1, large2, large3, large4, large5, large6, large7, large8, large9]
list_small_nums_b=[small1, small2, small3, small4, small5, small6, small7, small8, small9, small0]

list_large_nums_zf=[large1_zf, large2_zf, large3_zf, large4_zf, large5_zf, large6_zf, large7_zf, large8_zf, large9_zf]
list_small_nums_zf=[small1_zf, small2_zf, small3_zf, small4_zf, small5_zf, small6_zf, small7_zf, small8_zf, small9_zf, small0_zf]

list_large_nums_sd=[large1_sd, large2_sd, large3_sd, large4_sd, large5_sd, large6_sd, large7_sd, large8_sd, large9_sd]
list_small_nums_sd=[small1_sd, small2_sd, small3_sd, small4_sd, small5_sd, small6_sd, small7_sd, small8_sd, small9_sd, small0_sd]

list_large_nums_alef=[large1_alef, large2_alef, large3_alef, large4_alef, large5_alef, large6_alef, large7_alef, large8_alef, large9_alef]
list_small_nums_alef=[small1_alef, small2_alef, small3_alef, small4_alef, small5_alef, small6_alef, small7_alef, small8_alef, small9_alef, small0_alef]

list_large_nums_sabz=[large1_sabz, large2_sabz, large3_sabz, large4_sabz, large5_sabz, large6_sabz, large7_sabz, large8_sabz, large9_sabz]
list_small_nums_sabz=[small1_sabz, small2_sabz, small3_sabz, small4_sabz, small5_sabz, small6_sabz, small7_sabz, small8_sabz, small9_sabz, small0_sabz]

list_large_nums_artesh=[large1_artesh, large2_artesh, large3_artesh, large4_artesh, large5_artesh, large6_artesh, large7_artesh, large8_artesh, large9_artesh]
list_small_nums_artesh=[small1_artesh, small2_artesh, small3_artesh, small4_artesh, small5_artesh, small6_artesh, small7_artesh, small8_artesh, small9_artesh, small0_artesh]

list_large_nums_zard=[large1_zard, large2_zard, large3_zard, large4_zard, large5_zard, large6_zard, large7_zard, large8_zard, large9_zard]
list_small_nums_zard=[small1_zard, small2_zard, small3_zard, small4_zard, small5_zard, small6_zard, small7_zard, small8_zard, small9_zard, small0_zard]

list_chars= [b, jim, dal, c, sin, sad, ta, gh, l, m, n, v, h, ya]
list_chars_w= ['b', 'jim', 'dal', 'r', 'c', 'sin', 'sad', 'ta', 'gh', 'k', 'l', 'm', 'n', 'v', 'h', 'ya']
#====================================================================================

start= 47
startV= 8
dis= 1
shape1= large9.shape[1]
shape11= large3.shape[0]
shape12= taxi.shape[1]
const= 2
#------------------ CityCode------
shape2= small1.shape[0]
shape3= small1.shape[1]
loc1= 352
dis2= 0
#====================================================================================
def genearte_plate(back, start, startV, dis, shape1,shape11, const, shape2, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8):
    back[startV:startV+shape11,start:start+shape1, :] =ch1
    back[startV:startV+shape11,start+shape1+dis:start+dis+2*shape1, :] =ch2
    #-----------------------------------------
    back[17:17+ b.shape[0],start+dis+2*shape1+const:start+dis+2*shape1+const+b.shape[1], :] = ch3
    #----------------------------------------
    back[startV:startV+shape11,start+2*dis+2*shape1+2*const+ shape12:start+2*dis+3*shape1+2*const+ shape12, :] =ch4
    back[startV:startV+shape11,start+3*dis+3*shape1+2*const+ shape12:start+3*dis+4*shape1+2*const+ shape12, :] =ch5
    back[startV:startV+shape11,start+4*dis+4*shape1+2*const+ shape12:start+4*dis+5*shape1+2*const+ shape12, :] =ch6
    #----------------------------------------
    back[22:22+shape2,loc1:loc1+shape3, :] =ch7
    back[22:22+shape2,loc1+shape3+dis2:loc1+2*shape3+dis2, :] =ch8

    return back

#============================Generate typical plates================================================
def generate_typical_plates(n1, n2, n3, n4, n5, n6, n7, n8):
    ch1 = list_large_nums_b[n1]
    ch2 = list_large_nums_b[n2]
    ch3 = list_chars[n3]
    ch3_w= list_chars_w[n3]
    ch4 = list_large_nums_b[n4]
    ch5 = list_large_nums_b[n5]
    ch6 = list_large_nums_b[n6]

    ch7 = list_small_nums_b[n7]
    ch8 = list_small_nums_b[n8]
    img = genearte_plate(sefid, start, startV, dis, shape1, shape11, const, shape2,
                         ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)
    if n8== len(list_large_nums_b):
        n8= 0
        filename = "".join([str(n7+1), str(n8), CharKeyMap[ch3_w], str(n1+1), str(n2+1),str(n4+1), str(n5+1), str(n6+1), '_0.jpg'])
    else:
        filename = "".join(
            [str(n7 + 1), str(n8 + 1), CharKeyMap[ch3_w], str(n1 + 1), str(n2 + 1), str(n4 + 1), str(n5 + 1),
             str(n6 + 1), '_0.jpg'])
    path_write = os.path.join(path_results, filename)
    return path_write, img

#============================Generate artesh plates================================================
def generate_artesh_plates(n1, n2, n3, n4, n5, n6, n7, n8):
    ch1 = list_large_nums_artesh[n1]
    ch2 = list_large_nums_artesh[n2]
    ch3 = shin
    ch3_w= 'shin'
    ch4 = list_large_nums_artesh[n4]
    ch5 = list_large_nums_artesh[n5]
    ch6 = list_large_nums_artesh[n6]

    ch7 = small1_artesh
    ch8 = small1_artesh
    img = genearte_plate(artesh, start, startV, dis, shape1, shape11, const, shape2,
                         ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)
    filename = "".join(['11', CharKeyMap[ch3_w], str(n1+1), str(n2+1),str(n4+1), str(n5+1), str(n6+1), '_1.jpg'])
    path_write = os.path.join(path_results, filename)
    return path_write, img
# #============================Generate zf plates================================================
def generate_zf_plates(n1, n2, n3, n4, n5, n6, n7, n8, isRandom=True):
    ch1 = list_large_nums_zf[n1]
    ch2 = list_large_nums_zf[n2]
    if isRandom:
        n3 = int(np.random.choice(2))
        ch3 = [z, f][n3]
        ch3_w= ['z', 'f'][n3]
    else:
        if n3 == 26:
            ch3 = z
            ch3_w = 'z'
        else:
            ch3 = f
            ch3_w = 'f'
    ch4 = list_large_nums_zf[n4]
    ch5 = list_large_nums_zf[n5]
    ch6 = list_large_nums_zf[n6]

    ch7 = small1_zf
    ch8 = small1_zf
    img = genearte_plate(zf, start, startV, dis, shape1, shape11, const, shape2,
                         ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)
    filename = "".join(['11', CharKeyMap[ch3_w], str(n1+1), str(n2+1), str(n4+1), str(n5+1), str(n6+1), '_2.jpg'])
    path_write = os.path.join(path_results, filename)
    return path_write, img
# #============================Generate sd plates================================================
def generate_sd_plates(n1, n2, n3, n4, n5, n6, n7, n8, isRandom=True):
    ch1 = list_large_nums_sd[n1]
    ch2 = list_large_nums_sd[n2]
    if isRandom:
        n3 = int(np.random.choice(2))
        ch3 = [s, d][n3]
        ch3_w = ['s', 'd'][n3]
    else:
        if n3 == 34:
            ch3 = s
            ch3_w = 's'
        else:
            ch3 = d
            ch3_w = 'd'
    ch4 = list_large_nums_sd[n4]
    ch5 = list_large_nums_sd[n5]
    ch6 = list_large_nums_sd[n6]

    ch7 = list_small_nums_sd[n7]
    ch8 = list_small_nums_sd[n8]
    img = genearte_plate(sd, start, startV, dis, shape1, shape11, const, shape2,
                         ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)
    filename = "".join(
        [str(n7 + 1), str(n8 + 1), CharKeyMap[ch3_w], str(n1 + 1), str(n2 + 1), str(n4 + 1), str(n5 + 1),
         str(n6 + 1), '_3.jpg'])
    path_write = os.path.join(path_results, filename)
    return path_write, img

# #============================Generate sabz plates================================================
def generate_sabz_plates(n1, n2, n3, n4, n5, n6, n7, n8, isRandom=True):
    ch1 = list_large_nums_sabz[n1]
    ch2 = list_large_nums_sabz[n2]
    if isRandom:
        n3 = int(np.random.choice(2))
        ch3 = [p, th][n3]
        ch3_w= ['p', 'th'][n3]
    else:
        if n3 == 20:
            ch3 = p
            ch3_w = 'p'
        else:
            ch3 = th
            ch3_w = 'th'
    ch4 = list_large_nums_sabz[n4]
    ch5 = list_large_nums_sabz[n5]
    ch6 = list_large_nums_sabz[n6]
    ch7 = small1_sabz
    ch8 = small1_sabz
    img = genearte_plate(sabz, start, startV, dis, shape1, shape11, const, shape2,
                         ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)
    filename = "".join(['11', CharKeyMap[ch3_w], str(n1+1), str(n2+1),str(n4+1), str(n5+1), str(n6+1), '_4.jpg'])
    path_write = os.path.join(path_results, filename)
    return path_write, img
# #============================Generate zard plates================================================
def generate_zard_plates(n1, n2, n3, n4, n5, n6, n7, n8, isRandom=True):
    ch1 = list_large_nums_zard[n1]
    ch2 = list_large_nums_zard[n2]
    if isRandom:
        n3 = int(np.random.choice(2))
        ch3 = [taxi, ein][n3]
        ch3_w= ['taxi', 'ein'][n3]
    else:
        if n3 == 3:
            ch3 = taxi
            ch3_w = 'taxi'
        else:
            ch3 = ein
            ch3_w = 'ein'
    ch4 = list_large_nums_zard[n4]
    ch5 = list_large_nums_zard[n5]
    ch6 = list_large_nums_zard[n6]
    ch7 = list_small_nums_zard[n7]
    ch8 = list_small_nums_zard[n8]
    img = genearte_plate(zard, start, startV, dis, shape1, shape11, const, shape2,
                         ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)


    if n8== len(list_large_nums_b):
        n8= 0
        filename = "".join(
            [str(n7 + 1), str(n8), CharKeyMap[ch3_w], str(n1 + 1), str(n2 + 1), str(n4 + 1), str(n5 + 1),
             str(n6 + 1), '_5.jpg'])
    else:
        filename = "".join([str(n7+1), str(n8+1), CharKeyMap[ch3_w], str(n1+1), str(n2+1),str(n4+1), str(n5+1), str(n6+1), '_5.jpg'])
    path_write = os.path.join(path_results, filename)
    return path_write, img
# #============================Generate alef plates================================================
def generate_alef_plates(n1, n2, n3, n4, n5, n6, n7, n8):
    ch1 = list_large_nums_alef[n1]
    ch2 = list_large_nums_alef[n2]
    ch3 = alef
    ch3_w= 'alef'
    ch4 = list_large_nums_alef[n4]
    ch5 = list_large_nums_alef[n5]
    ch6 = list_large_nums_alef[n6]

    ch7 = list_small_nums_alef[n7]
    ch8 = list_small_nums_alef[n8]
    img = genearte_plate(back_alef, start, startV, dis, shape1, shape11, const, shape2,
                         ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)

    if n8== len(list_large_nums_b):
        n8= 0
        filename = "".join(
            [str(n7 + 1), str(n8), CharKeyMap[ch3_w], str(n1 + 1), str(n2 + 1), str(n4 + 1), str(n5 + 1),
             str(n6 + 1), '_6.jpg'])
    else:
        filename = "".join([str(n7+1), str(n8+1), CharKeyMap[ch3_w], str(n1+1), str(n2+1),str(n4+1), str(n5+1), str(n6+1), '_6.jpg'])
    path_write = os.path.join(path_results, filename)
    return path_write, img
# #============================Generate random plates================================================
# for i in tqdm(range(200)):
#     n1 = int(np.random.choice(len(list_large_nums_b)))
#     n2 = int(np.random.choice(len(list_large_nums_b)))
#     n3 = int(np.random.choice(len(list_chars)))
#     n4 = int(np.random.choice(len(list_large_nums_b)))
#     n5 = int(np.random.choice(len(list_large_nums_b)))
#     n6 = int(np.random.choice(len(list_large_nums_b)))
#     n7 = int(np.random.choice(len(list_large_nums_b)))
#     n8 = int(np.random.choice(len(list_large_nums_b)) + 1)
#     generate_typical_plates(n1, n2, n3, n4, n5, n6, n7, n8)
#     generate_sabz_plates(n1, n2, n3, n4, n5, n6, n7, n8)
#     generate_sd_plates(n1, n2, n3, n4, n5, n6, n7, n8)
#     generate_zf_plates(n1, n2, n3, n4, n5, n6, n7, n8)
#     generate_artesh_plates(n1, n2, n3, n4, n5, n6, n7, n8)
#     generate_alef_plates(n1, n2, n3, n4, n5, n6, n7, n8)
#     generate_zard_plates(n1, n2, n3, n4, n5, n6, n7, n8)
# #============================Generate Legacy plates================================================
# print('===================Generating Legacy plates==========================')

