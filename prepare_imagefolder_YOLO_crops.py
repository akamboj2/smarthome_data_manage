import os
import shutil
import random
import sys
sys.path.insert(0, '/home/abhi/research/SmartHome/yolov5')

from detect import run #hoping this will import my locally clone version

#this file assumes prepare_imagefolder_directory has been run and base points to that imagefolder directory

base = '/home/abhi/research/SmartHome/Data/image_folder_data' #'/home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data'
dest = '/home/abhi/research/SmartHome/Data/image_folder_yolo_cropped_data'

# python youhome.py --data_dir /home/abhi/research/SmartHome/Data/image_folder_yolo_cropped_data -b 64 -s --save_folder ./save_yolo_cropped_params/

for tvsplit in os.listdir(base):
    print("On split=", tvsplit)
    for opt in os.listdir(os.path.join(base,tvsplit)):
        print("On opt=", opt)
        run(weights='yolov5x.pt', imgsz=(640, 640), conf_thres=.6, source=os.path.join(base,tvsplit,opt), 
            project=os.path.join(dest,tvsplit),name=opt, save_crop=True, classes=0, nosave=True
            )


"""
Crop person detections with 60% confident
Crop slightly larger than the person to get context - try 1.2 times image size
Use script Neo gave for confidence saving from yolov5, just crop 1.2 times.
"""