from datetime import datetime
from timestamp_functions import *
import cv2

start_time = datetime.now()

# loading both video and frame
clip_img_name   = name_extract(r'C:\Users\user\Desktop\video timestamp project\clip img')
clip_img        = cv2.imread(clip_img_name)
vod_name        = name_extract(r"C:\Users\user\Desktop\video timestamp project\ffmpeg vod")
vod             = cv2.VideoCapture(vod_name)


# necessary variables
most_similar_pixelDiff_num      = float("inf")
most_matching_frame             = 0
readFrame                       = 0
vod_fps                         = vod.get(cv2.CAP_PROP_FPS)
vod_width                       = int(vod.get(cv2.CAP_PROP_FRAME_WIDTH))
vod_height                      = int(vod.get(cv2.CAP_PROP_FRAME_HEIGHT))
clip_img_resize                 = cv2.resize(clip_img, (vod_width, vod_height) )
gray_clip_img                   = cv2.cvtColor(clip_img_resize, cv2.COLOR_BGR2GRAY)


# template matching
while True:
    ret, frame = vod.read()
    if frame is None:
        break

    readFrame += 1

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff  = cv2.absdiff(gray_clip_img, gray_frame)

    # determining if the current frame is better than all previous frames
    if diff.sum() < most_similar_pixelDiff_num:
        most_similar_pixelDiff_num = diff.sum()
        most_matching_frame = readFrame


# results
print("The most matching frame is: " + str(most_matching_frame))
print("The number of different pixel(s) is: " + str(most_similar_pixelDiff_num))
print("The total number of frames is: " + str(readFrame))

# calculating and displaying timestamp
timestamp =  float((most_matching_frame/readFrame) * (readFrame / vod_fps))
time = timestamp; time = time % (24 * 3600); hour = time // 3600
time %= 3600; minutes = time // 60; time %= 60; seconds = time
print("The approximate timestamp is: " + str(int(hour))
      + " hour(s) " + str(int(minutes)) + " minute(s) " + str("{:.1f}".format(seconds)) + " second(s).")


# for checking run time
end_time = datetime.now()
print('Runtime: {}'.format(end_time - start_time))

vod.release()





