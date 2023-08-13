import os

path_dst= r'./ckpts'
path_models= {}
path_jsonmodels= {}
list_models= []

for file in os.listdir(path_dst):
    if 'h5' in file:
        name= file.split('.')[0]
        list_models.append(name)
        path_models[name] = os.path.join(path_dst, name+'.h5')
    if 'json' in file:
        name= file.split('.')[0]
        path_jsonmodels[name] = os.path.join(path_dst, name+'.json')
