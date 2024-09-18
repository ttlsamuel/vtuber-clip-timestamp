# Expand to see project details
"""
PROJECT DESCRIPTION:
We are trying to find the timestamp of a frame in a vtuber stream,
 which matches a specific frame from a vtuber clip.

PROJECT GOAL:
To create a website that can serve the above purpose.
The idea is: by inputting an image from a clip, and a stream url (YouTube exclusively),
             the site will return the exact timestamp of that clip image in the stream.
Extended ideas: - using audio comparison as a method to find the timestamp
                - the stream url input bar accepts twitch stream as an input
                - full image and full image comparison right now, maybe consider template matching?

PROJECT PROGRESS:
This programme can now check which frame matches the clip frame on a local environment,
 and then return the corresponding timestamp.
To extract frames from the stream, use ffmpeg.

Caution:
- Check whether you have the right file extension name for ffmpeg command.
- Check the type of image in the clip img file, it will be converted to jpg.
- Check all directories!

TO-DO:
- lower the time for converting stream vod to frames by not using the jpeg format.
 (or alternatively, use other methods instead of ffmpeg)
- lower the time for image comparison.
- consider making the whole project an executable.
"""

# necessary imports
from datetime import datetime
start_time = datetime.now()
import os
import cv2
import re

# frame from the clip
path = r'C:\Users\user\Desktop\video timestamp project\clip img'
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path, 'main.jpg'))
clip_img = cv2.imread(r"C:\Users\user\Desktop\video timestamp project\clip img\main.jpg")
clip_img = cv2.resize(clip_img, (360, 240))

# stream frames path
path = r'C:\Users\user\Desktop\video timestamp project\stream frame'

# necessary variables
fps = 10
most_similar_pixelDiff_num = float("inf")
most_matching_frame = ""
num_of_total_frames = len(os.listdir(path))


# looping over frames and return the one that's most similar
for filename in os.listdir(path):
    #BEWARE OF the format of the stream frames
    img2 = cv2.imread(path + '\\' + filename)
    img2 = cv2.resize(img2, (360, 240))

    gray1 = cv2.cvtColor(clip_img, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)

    #determining if the current frame is better than all previous frames
    if diff.sum() < most_similar_pixelDiff_num:
        most_similar_pixelDiff_num = diff.sum()
        most_matching_frame = filename



# results
print("The most matching frame is: " + most_matching_frame)
print("The number of different pixel(s) is: " + str(most_similar_pixelDiff_num))
print("The total number of frames is: " + str(num_of_total_frames))
print('\n')

# calculating and displaying timestamp
int_most_matching_frame = int(re.findall(r'\d+', most_matching_frame)[0])
timestamp =  int((int_most_matching_frame/num_of_total_frames)*(num_of_total_frames/fps))
time = timestamp; time = time % (24 * 3600); hour = time // 3600
time %= 3600; minutes = time // 60; time %= 60; seconds = time
print("The approximate timestamp is: " + str(hour)
      + " hour(s) " + str(minutes) + " minute(s) " + str(seconds) + " second(s).")


# for checking run time
end_time = datetime.now()
print('Runtime: {}'.format(end_time - start_time))




