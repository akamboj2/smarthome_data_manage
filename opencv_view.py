import numpy as np
import cv2

# cap = cv2.VideoCapture('/home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data/p101/Cook.Cut/00101_c4s0.h264')
#NOTE: THIS EXAMPLE BELOW IS A CORRUPTED VIDEO OR SOMETHING!
# /home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data/p101/Cook.Usemicrowave/00101_c4s0.h264 --> faulty example!
cap = cv2.VideoCapture('/home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data/p101/Cook.Usemicrowave/00101_c4s0.h264')

#Uncomment this to to play whole video through the video
stepthrough = True
while(True):
    ret, frame = cap.read()
    if frame is None: break

    fps = cap.get(cv2.CAP_PROP_FPS)
    print('frames per second =',fps)
    print('frame size:',frame.shape)
    cv2.imshow('frame',frame)
    if stepthrough:
        while(True):
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()



#Uncomment below to write all frames to a directory
# i=0
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==False: 
#         print("done at %d" % i)
#         break
#     # cv2.imwrite('faulty_testframes/testing_%d.jpg'% i,frame)

#     i+=1
# cap.release()

# cv2.destroyAllWindows()



# I don't really remember what this does? maybe can delete. looks like show and write a frame??
# import cv2
# video = cv2.VideoCapture('/home/abhi/research/SmartHome/Data/youhome_mp4_data/mp4data/p101/Cook.Usemicrowave/00101_c4s0.h264')

# fps = video.get(cv2.CAP_PROP_FPS)
# print('frames per second =',fps)

# minutes = 0
# seconds = 2
# frame_id = int(fps*(minutes*60 + seconds))
# print('frame id =',frame_id)

# video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
# ret, frame = video.read()

# t_msec = 1000*(minutes*60 + seconds)
# video.set(cv2.CAP_PROP_POS_MSEC, t_msec)
# ret, frame = video.read()

# print(frame.shape)
# cv2.imshow('frame', frame); cv2.waitKey(0)
# cv2.imwrite('my_video_frame.png', frame)