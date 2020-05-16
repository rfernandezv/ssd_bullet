import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches
import cv2
import os

data = pd.read_csv('train.csv',delimiter=";")
resumeData = pd.DataFrame({'image_name':[],'x1':[],'y1':[],'x2':[],'y2':[], 'type':[]})

resumeData['image_name'] = data['image_name']
resumeData['x1'] = data['xmin']
resumeData['x2'] = data['xmax']
resumeData['y1'] = data['ymin']
resumeData['y2'] = data['ymax']
resumeData['type'] = data['type']


image_name_temp = 'X'
cont = 0

file = open("./trainval.txt", "w")

for _,row in resumeData.iterrows():
    cont = cont + 1
    
    if image_name_temp != 'X':
        if image_name_temp != row.image_name:            
            
            # exportar
            export = resumeData.loc[resumeData['image_name'] == image_name_temp]
            positionExt = image_name_temp.find('.JPG')
            name = image_name_temp[0:positionExt]
            
            file.write(name + "\n")

            
            ####
            
            # limpiar valores #
            #print("image_name: "+image_name_temp+", cont: "+str(cont))
            cont = 0
            ###
       
    image_name_temp = row.image_name
    
 # exportar

file.close()