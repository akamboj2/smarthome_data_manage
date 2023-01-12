import numpy as np
import cv2
import os
import tqdm
import random

"""
creates text files of the format shown here:
https://github.com/OpenGVLab/efficient-video-recognition
<path_1> <label_1>
<path_2> <label_2>
...
<path_n> <label_n>


NOTE: make sure the out_train and out_val files are empty before this (or if you want to append new things that can work too)
"""


#29 activites
gt_labels = ["Cook.Cut"             ,
        "Cook.Usemicrowave"     ,
        "Cook.Useoven"          ,
        "Cook.Usestove"         ,
        "Drink.Frombottle"      ,
        "Drink.Fromcup"         ,
        "Eat.Snack"             ,
        "Eat.Useutensil"        ,
        "Exercise"              ,
        "Getup"                 ,
        "Lay.Onbed"             ,
        "Nap"                   ,
        "Play.Boardgame"        ,
        "Read"                  ,
        "Use.Coffeemachine"     ,
        "Use.Computer"          ,
        "Use.Dishwasher"        ,
        "Use.Gamecontroller"    ,
        "Use.Kettle"            ,
        "Use.Mop"               ,
        "Use.Phone"             ,
        "Use.Refrig"            ,
        "Use.Shelf"             ,
        "Use.Sink"              ,
        "Use.Switch"            ,
        "Use.Tablet"            ,
        "Use.Vaccum"            ,
        "Watch.TV"              ,
        "Write"                             
        ]


base = '/home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data'
out_train = 'evl_format/train.txt'
out_val = 'evl_format/val.txt'
files = []
train_ct, val_ct = {i:0 for i in gt_labels},{i:0 for i in gt_labels}

with open(out_train,'a') as train_file, open(out_val,'a') as val_file:
    for p in os.listdir(base):
        print("At p:",p)
        for option in os.listdir(os.path.join(base,p)):
            for vid in os.listdir(os.path.join(base,p,option)):
                #make sure it's a video not frames
                if os.path.splitext(vid)[1] !='.h264':
                    continue

                #create video path
                f = os.path.join(base,p,option,vid)

                #detect corrupted videos
                corrupt=False
                cap = cv2.VideoCapture(f)
                i=0
                while(cap.isOpened()):
                    ret, frame = cap.read()
                    if ret==False: 
                        # print("done at %d" % i)
                        break
                    # cv2.imwrite(os.path.join(new_path,'frame_%d.jpg'% i),frame) #NOTE: UNCOMMENT WHEN U WANT TO actually write the images
                    i+=1
                    if frame.shape[0]==120:
                        print("CORRUPTED DIRECTORY: ", f)
                        corrupt = True
                        break
                cap.release()
                cv2.destroyAllWindows()
                if corrupt:
                    #ignore file if corrupted
                    continue

                #finally add to output file
                if random.random() > .2:
                    train_file.write(f+" "+str(gt_labels.index(option))+'\n')
                    train_ct[option]+=1
                else:
                    val_file.write(f+" "+str(gt_labels.index(option))+'\n')
                    val_ct[option]+=1

#make sure none of the categories have 0 in train and some in val!
print("train_count",train_ct)
print("val_count",val_ct)


"""
(cv) abhi@abhi-MS-7C56:~/research/SmartHome/Data$ python create_evl_format.py 
At p: p199
At p: p101
CORRUPTED DIRECTORY:  /home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data/p101/Cook.Usemicrowave/00101_c4s1.h264
CORRUPTED DIRECTORY:  /home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data/p101/Cook.Usemicrowave/00101_c4s0.h264
At p: p106
At p: p104
CORRUPTED DIRECTORY:  /home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data/p104/Eat.Snack/00104_c1s0.h264
At p: p103
At p: p105
At p: p102
train_count {'Cook.Cut': 17, 'Cook.Usemicrowave': 13, 'Cook.Useoven': 15, 'Cook.Usestove': 13, 'Drink.Frombottle': 86, 'Drink.Fromcup': 93, 'Eat.Snack': 95, 'Eat.Useutensil': 65, 'Exercise': 32, 'Getup': 23, 'Lay.Onbed': 25, 'Nap': 34, 'Play.Boardgame': 69, 'Read': 89, 'Use.Coffeemachine': 9, 'Use.Computer': 91, 'Use.Dishwasher': 13, 'Use.Gamecontroller': 59, 'Use.Kettle': 14, 'Use.Mop': 21, 'Use.Phone': 90, 'Use.Refrig': 8, 'Use.Shelf': 20, 'Use.Sink': 17, 'Use.Switch': 94, 'Use.Tablet': 87, 'Use.Vaccum': 25, 'Watch.TV': 33, 'Write': 92}
val_count {'Cook.Cut': 3, 'Cook.Usemicrowave': 5, 'Cook.Useoven': 5, 'Cook.Usestove': 7, 'Drink.Frombottle': 26, 'Drink.Fromcup': 19, 'Eat.Snack': 16, 'Eat.Useutensil': 17, 'Exercise': 8, 'Getup': 7, 'Lay.Onbed': 5, 'Nap': 6, 'Play.Boardgame': 22, 'Read': 23, 'Use.Coffeemachine': 1, 'Use.Computer': 20, 'Use.Dishwasher': 7, 'Use.Gamecontroller': 11, 'Use.Kettle': 6, 'Use.Mop': 9, 'Use.Phone': 25, 'Use.Refrig': 2, 'Use.Shelf': 10, 'Use.Sink': 3, 'Use.Switch': 18, 'Use.Tablet': 25, 'Use.Vaccum': 5, 'Watch.TV': 7, 'Write': 21}

"""