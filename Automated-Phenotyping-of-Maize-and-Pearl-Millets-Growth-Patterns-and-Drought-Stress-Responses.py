import numpy as np
import cv2
from glob import glob
import os
import csv
import pandas
import itertools
from datetime import datetime


hello = glob("/work/schnablelab/cbutera2/Diversity_grasses_4mo/*/Vis_SV*/*.png")  
hi1 = glob("/work/schnablelab/cbutera2/Diversity_grasses_4mo/*/*.txt")


hi = sorted(hi1*5)
hi = sorted(hi)
hello = sorted(hello)



export = []
#Pixel to real length relationship
con1 = 1490/1919
con2 = 1490/1330   
con3 = 1490/756.5

for i,x  in zip(hello, hi):
    img = cv2.imread(i,1)
    cwd = os.path.abspath(i)
    cwd2 = cwd.split('/')
    date = cwd2[5]
    dated = date[-27:]
    dated = dated[:-17]
    dat = datetime.strptime(dated, "%Y-%m-%d")
    zoom1 = "all"
    zoom2 = "2017-11-23"
    zoom2 = datetime.strptime(zoom2, "%Y-%m-%d")
    zoom3 = "2017-12-16"
    zoom3 = datetime.strptime(zoom3, "%Y-%m-%d")
    day1 = "2017-10-13"
    day1 = datetime.strptime(day1, "%Y-%m-%d")
    days = dat - day1
    days = str(days)
    days = days[:-13]
    if days == "":
        days = "0"
    else:
        pass

       #Plant height code 
    if dat > zoom2 and dat <zoom3:
        crop = img[0:1537, 650:2000]
        con = con2
        res= cv2.Canny(crop, 100, 500)
        point= np.nonzero(res)
        points = np.array(point)
        if points.size:
            y = points[0, 0]
            y1 = 1537 - y
        else:
            continue
        
    elif dat >= zoom3:
        crop = img[22:1672, 880:1730]
        con = con3
        res= cv2.Canny(crop, 100, 500)
        point= np.nonzero(res)
        points = np.array(point)
        if points.size:
            y = points[0, 0]
            y1 = 1650 - y
        else:
            continue
    else:
        crop = img[0:1712, 420:2200]
        con = con1
        res= cv2.Canny(crop, 500, 500)
        point= np.nonzero(res)
        points = np.array(point)
        if points.size:
            y = points[0, 0]
            y1 = 1712 - y
        else:
            continue

    ymm = str(y1 * con)
    ymmm = ymm[:7]
    
    # if ymmm == "2542.39":
    #     ymmm = ""
    # elif ymmm =="1618.46":
    #     ymmm = ""
    # else:
    #     pass

    
    name = cwd2[5]
    named = name[26:]
    named = named[:-28]
    water = open(x, "rt")
    waterml = water.readlines()
    ml = (waterml[9])
    ml2 = ml[19:]
    ml2 = int(ml2)
    
    #Pixel count code

    pixel = crop
    hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
    lower_red = np.array([1,55,1])
    upper_red = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)   
    count = np.count_nonzero(mask)
    #counted =  0.0617*count + 16.702
    counted = count * con
    counted = str(counted)
    counted = counted[0:8]
    export.append([named, ymmm, cwd2[6], ml2, days, dated, counted, count])
    water.close()
    
    
    
exported = pandas.DataFrame(export)
exported.to_csv('The List with pixel count daniel.csv')



