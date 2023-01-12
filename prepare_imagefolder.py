import os
import shutil
import random

#this file creates a directory to use pytorch imagefolder directory
# to run actual image run go to detectiontrain/binary_react/youhome.py


# python youhome.py --data_dir /home/abhi/research/SmartHome/Data/image_folder_data -b 64  
# Note the first time i ran it i got 15%     

# base = '/home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data'
# dest = '/home/abhi/research/SmartHome/Data/image_folder_data'

# for p in os.listdir(base):
#     print("On p=", p)
#     for opt in os.listdir(os.path.join(base,p)):
#         print("On opt=",opt)
#         vids = os.listdir(os.path.join(base,p,opt))
#         for v in vids:
#             if v.split("_")[-1]=='frames':
#                 fdir = os.path.join(base,p,opt,v)
#                 frames = os.listdir(fdir)
#                 for f in frames:
#                     trainval_dir = os.path.join(dest,'train' if random.random()<.75 else 'val')
#                     new_label_dir = os.path.join(trainval_dir,opt)
#                     if not os.path.exists(new_label_dir):
#                         os.makedirs(new_label_dir)
#                     shutil.copyfile(os.path.join(base,p,opt,v,f),os.path.join(new_label_dir,p+'_'+v+'_'+f+'.jpg')) 
#                     #renaming to p101_cs12p4_frame24 or whatever



#this i manually changing base dest and trainval_dir = test or val for different folders
#used it to create person generalize
base = '/home/abhi/research/SmartHome/Data/youhome_mp4_data/train_split'
dest = '/home/abhi/research/SmartHome/Data/person_generalize'

for p in os.listdir(base):
    print("On p=", p)
    for opt in os.listdir(os.path.join(base,p)):
        print("On opt=",opt)
        vids = os.listdir(os.path.join(base,p,opt))
        for v in vids:
            if v.split("_")[-1]=='frames':
                fdir = os.path.join(base,p,opt,v)
                frames = os.listdir(fdir)
                for f in frames:
                    trainval_dir = os.path.join(dest,'train')
                    new_label_dir = os.path.join(trainval_dir,opt)
                    if not os.path.exists(new_label_dir):
                        os.makedirs(new_label_dir)
                    shutil.copyfile(os.path.join(base,p,opt,v,f),os.path.join(new_label_dir,p+'_'+v+'_'+f+'.jpg')) 
                    #renaming to p101_cs12p4_frame24 or whatever


"""
Crop person detections with 60% confident
Crop slightly larger than the person to get context - try 1.2 times image size
Use script Neo gave for confidence saving from yolov5, just crop 1.2 times.
"""
"""
#from another image folder:
base = '/home/abhi/research/SmartHome/Data/imgdata4event_2021_full_cropped'
dest = '/home/abhi/research/SmartHome/Data/full_data'

# python youhome.py --data_dir /home/abhi/research/SmartHome/Data/image_folder_data -b 64  
# Note the first time i ran it i got 15%     

# for p in os.listdir(base):
#     print("On p=", p)
for opt in os.listdir(base):
    print("On opt=",opt)
    fdir = os.path.join(base,opt)
    frames = os.listdir(fdir)
    for f in frames:
        trainval_dir = os.path.join(dest,'train' if random.random()<.75 else 'val')
        new_label_dir = os.path.join(trainval_dir,opt)
        if not os.path.exists(new_label_dir):
            os.makedirs(new_label_dir)
        shutil.copyfile(os.path.join(base,opt,f),os.path.join(new_label_dir,f)) 
        #renaming to p101_cs12p4_frame24 or whatever
"""