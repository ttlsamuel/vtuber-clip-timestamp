PROJECT DESCRIPTION:
We are trying to find the timestamp of a frame in a video,
 which matches a specific frame from a clip.

PROJECT GOAL:
To create a website that can serve the above purpose.
The idea is: by inputting an image from a clip, and a stream url (YouTube exclusively),
             the site will return the exact timestamp of that clip image in the stream.

Extended ideas:
- using audio comparison as a method to find the timestamp
- the stream url input bar accepts twitch stream as an input

PROJECT PROGRESS (How to run):
1. Place one clip iamge in the "clip img" file "and one video in the "raw vod" file.
2. Execute main_script.py

Caution:
- Check all directories!
- Requires ffmpeg to run the programme
- Make sure that "clip img" and "raw vod" folder contains only the necessary files! 

TO-DO:
- lower the time for image comparison.
- consider making the whole project an executable.
