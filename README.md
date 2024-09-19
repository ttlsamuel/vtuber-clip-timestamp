PROJECT DESCRIPTION:
We are trying to find the timestamp of a frame in a vtuber stream,
 which matches a specific frame from a vtuber clip.

PROJECT GOAL:
To create a website that can serve the above purpose.
The idea is: by inputting an image from a clip, and a stream url (YouTube exclusively),
             the site will return the exact timestamp of that clip image in the stream.

Extended ideas:
- using audio comparison as a method to find the timestamp
- the stream url input bar accepts twitch stream as an input
- full image and full image comparison right now, maybe consider template matching?

PROJECT PROGRESS:
This programme can now check which frame matches the clip frame on a local environment,
 and then return the corresponding timestamp.
To extract frames from the stream, use ffmpeg.

Caution:
- Check whether you have the right file extension name for ffmpeg command.
- Check all directories!
- Check the fps variable in video_timestamp_project.py, it affects the timestamp calculation!

TO-DO:
- lower the time for converting stream vod to frames by not using the jpeg format.
 (or alternatively, use other methods instead of ffmpeg)
- lower the time for image comparison.
- consider making the whole project an executable.
