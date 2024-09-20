PROJECT DESCRIPTION:
The project aims to create a Python-based tool that can find the timestamp of a frame in a video, 
which matches a specific frame from a clip.

PROJECT GOAL:
To create a website that can serve the above purpose.
The idea is: by inputting an image from a clip, and a stream url (YouTube exclusively),
             the site will return the exact timestamp of that clip image in the stream.
             (technical difficulty: obtaining youtube video is inefficient)

Extended ideas:
- using audio comparison as a method to find the timestamp
- the stream url input bar accepts twitch stream as an input

PROJECT PROGRESS (How to run):
1. Place one clip iamge in the "clip img".
2. Place your video in the "raw vod" file if you have any to provide.
3. Execute main_script.py
4. If you did not provide any video, input a youtube url and choose the desired format for video downloading 
5. Wait for the script to compute the timestamp for you
6. (Recommended) Enter y to delete files in the "ffmpeg vod" vile

Caution:
- Check all directories!
- Requires ffmpeg and yt-dlp to run the programme
- Make sure that "clip img" folder contains your clip image (one only)
- "ffmpeg vod" and "raw vod" folder cannot contain more than one file!

TO-DO:
- consider making the whole project an executable.
- look for alternatives of obtaining youtube video
