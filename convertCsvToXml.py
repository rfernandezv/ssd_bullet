import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches
import cv2
import xml.etree.cElementTree as ET

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

for _,row in resumeData.iterrows():
    cont = cont + 1
    
    if image_name_temp != 'X':
        if image_name_temp != row.image_name:            
            
            # exportar
            export = resumeData.loc[resumeData['image_name'] == image_name_temp]
            positionExt = image_name_temp.find('.JPG')
            name = image_name_temp[0:positionExt]            
            nameXml = name + '.xml'
            
            img = cv2.imread('./VOCdevkit/VOC2007/JPEGImages/'+ name + '.JPG')
            # get dimensions of image
            dimensions = img.shape
            
            height = img.shape[0]
            width = img.shape[1]

            root = ET.Element("annotation")            
            
            ET.SubElement(root, "foler").text = "VOC2007"
            ET.SubElement(root, "filename").text = name + ".JPG"
            
            source = ET.SubElement(root, "source")
            ET.SubElement(source, "database").text = "The VOC2007 Database"
            ET.SubElement(source, "annotation").text = "PASCAL VOC2007"
            ET.SubElement(source, "image").text = "RFV"
            
            size = ET.SubElement(root, "size")
            ET.SubElement(size, "width").text = str(int(width))
            ET.SubElement(size, "height").text = str(int(height))
            ET.SubElement(size, "depth").text = "3"
            
            ET.SubElement(root, "segmented").text = "0"
            
            for _,rowExport in export.iterrows():
                objectElement = ET.SubElement(root, "object")
                ET.SubElement(objectElement, "name").text = "bullet"
                ET.SubElement(objectElement, "pose").text = "Left"
                ET.SubElement(objectElement, "truncated").text = "1"
                ET.SubElement(objectElement, "difficult").text = "0"
                
                bndbox = ET.SubElement(objectElement, "bndbox")
                ET.SubElement(bndbox, "xmin").text = str(int(rowExport.x1))
                ET.SubElement(bndbox, "ymin").text = str(int(rowExport.y1))
                ET.SubElement(bndbox, "xmax").text = str(int(rowExport.x2))
                ET.SubElement(bndbox, "ymax").text = str(int(rowExport.y2))
                
            
            tree = ET.ElementTree(root)
            tree.write("./VOCdevkit/VOC2007/Annotations/"+nameXml)
            
            ####
            
            # limpiar valores #
            #print("image_name: "+image_name_temp+", cont: "+str(cont))
            cont = 0
            ###
       
    image_name_temp = row.image_name
    
 # exportar

export = resumeData.loc[resumeData['image_name'] == image_name_temp]
positionExt = image_name_temp.find('.JPG')
name = image_name_temp[0:positionExt]            
nameXml = name + '.xml'
            
img = cv2.imread('./VOCdevkit/VOC2007/JPEGImages/'+ name + '.JPG')
# get dimensions of image
dimensions = img.shape
            
height = img.shape[0]
width = img.shape[1]

root = ET.Element("annotation")            
            
ET.SubElement(root, "foler").text = "VOC2007"
ET.SubElement(root, "filename").text = name + ".JPG"
            
source = ET.SubElement(root, "source")
ET.SubElement(source, "database").text = "The VOC2007 Database"
ET.SubElement(source, "annotation").text = "PASCAL VOC2007"
ET.SubElement(source, "image").text = "RFV"
            
size = ET.SubElement(root, "size")
ET.SubElement(size, "width").text = str(int(width))
ET.SubElement(size, "height").text = str(int(height))
ET.SubElement(size, "depth").text = "3"
            
ET.SubElement(root, "segmented").text = "0"
            
for _,rowExport in export.iterrows():
    objectElement = ET.SubElement(root, "object")
    ET.SubElement(objectElement, "name").text = "bullet"
    ET.SubElement(objectElement, "pose").text = "Left"
    ET.SubElement(objectElement, "truncated").text = "1"
    ET.SubElement(objectElement, "difficult").text = "0"
                
    bndbox = ET.SubElement(objectElement, "bndbox")
    ET.SubElement(bndbox, "xmin").text = str(int(rowExport.x1))
    ET.SubElement(bndbox, "ymin").text = str(int(rowExport.y1))
    ET.SubElement(bndbox, "xmax").text = str(int(rowExport.x2))
    ET.SubElement(bndbox, "ymax").text = str(int(rowExport.y2))
                
            
    tree = ET.ElementTree(root)
    tree.write("./VOCdevkit/VOC2007/Annotations/"+nameXml)
####

