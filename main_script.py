from datetime import datetime
from file_func import *
from yt_dlp_dl import yt_download
from reconfig import reconfigure
from audio import audio_matching
import os, sys, cv2

start_time = datetime.now()

clip_img_path    = r'C:\Users\user\Desktop\video timestamp project\clip img'
ffmpeg_vod_path  = r"C:\Users\user\Desktop\video timestamp project\ffmpeg vod"
raw_vod_path     = r"C:\Users\user\Desktop\video timestamp project\raw vod"


# if user provides youtube url
if input("Enter y (in small letter) if you wish to provide a url: ") == "y":
    yt_download()

# if user choose audio matching, skip the frame matching part
if input("Enter a (in small) letter if you want to choose audio matching: ") == "a":
    audio_matching()
    input("All commands executed without error. Press Enter to exit programme. ")
    sys.exit(0)


# run frame matching from here
reconfigure()

if not os.listdir(ffmpeg_vod_path):
    vod_name = name_extract(raw_vod_path)
else:
    vod_name = name_extract(ffmpeg_vod_path)


# loading both video and frame
clip_img_name   = name_extract(clip_img_path)
clip_img        = cv2.imread(clip_img_name, cv2.IMREAD_GRAYSCALE)
vod             = cv2.VideoCapture(vod_name)


# necessary variables
most_similar_pixelDiff_num      = float("inf")
most_matching_frame             = 0
readFrame                       = 0
vod_fps                         = vod.get(cv2.CAP_PROP_FPS)
vod_width                       = int(vod.get(cv2.CAP_PROP_FRAME_WIDTH))
vod_height                      = int(vod.get(cv2.CAP_PROP_FRAME_HEIGHT))
clip_img_resize                 = cv2.resize(clip_img, (vod_width, vod_height) )


# template matching
while True:
    ret, frame = vod.read()
    if frame is None:
        break

    readFrame += 1
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(clip_img_resize, gray_frame)

    # determining if the current frame is better than all previous frames
    if diff.sum() < most_similar_pixelDiff_num: # can we optimize this part? (in c++ or don't use diff sum)
        most_similar_pixelDiff_num = diff.sum()
        most_matching_frame = readFrame


# results
# print("The most matching frame is:          " + str(most_matching_frame))
# print("The number of different pixel(s) is: " + str(most_similar_pixelDiff_num))
# print("The total number of frames is:       " + str(readFrame))

# calculating and displaying timestamp
timestamp =  float((most_matching_frame/readFrame) * (readFrame / vod_fps))
time_output(timestamp)

# for checking run time
end_time = datetime.now()
print('Runtime: {}'.format(end_time - start_time))

vod.release()
cleaning(r'C:\Users\user\Desktop\video timestamp project\ffmpeg vod')

input("All commands executed without error. Press Enter to exit programme. ")
