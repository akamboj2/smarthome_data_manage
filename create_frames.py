import numpy as np
import cv2
import os
import tqdm

base = 'youhome_mp4_data/mp4data'
files = []
for p in os.listdir(base):
    print("At p:",p)
    for option in os.listdir(os.path.join(base,p)):
        for vid in os.listdir(os.path.join(base,p,option)):
            f = os.path.join(base,p,option,vid)
            files.append(f)

            new_path = os.path.splitext(f)[0]+'_frames'
            # os.mkdir(new_path) #NOTE UNCOMMENT TO CREATE NEW DIRECTORY
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
                    print("CORRUPTED DIRECTORY: ", new_path)
                    break
            cap.release()
            cv2.destroyAllWindows()

print(len(files))


"""
#TODO: Check correct frame size and faulty frame size and see if you can detect what the faulty image directories are.

(cv) abhi@abhi-MS-7C56:~/research/SmartHome/Data$ python create_frames.py 
At p: p199
At p: p101
CORRUPTED DIRECTORY:  youhome_mp4_data/mp4data/p101/Cook.Usemicrowave/00101_c4s1_frames
CORRUPTED DIRECTORY:  youhome_mp4_data/mp4data/p101/Cook.Usemicrowave/00101_c4s0_frames
At p: p106
At p: p104
CORRUPTED DIRECTORY:  youhome_mp4_data/mp4data/p104/Eat.Snack/00104_c1s0_frames
At p: p103
At p: p105
At p: p102
3368
"""