import os
import subprocess

# adjust reconfig_vid metadata here
fps         = "fps=5"
resolution  = "320x240"


# read file name from directories with one item
def name_extract(path):
    filename = str(os.listdir(path)[0])
    name = os.path.join(path, filename)
    return name

# remove contents in directories
def cleaning(path):
    for filename in os.listdir(path):
        os.remove(os.path.join(path, filename))


# the following codes only run when this py file is being executed
if __name__ == "__main__":

    # executing reconfiguration of raw vod
    cleaning(r'C:\Users\user\Desktop\video timestamp project\ffmpeg vod')
    raw_vod_name = (name_extract(r"C:\Users\user\Desktop\video timestamp project\raw vod") )
    subprocess.run([ "ffmpeg", "-i"  , raw_vod_name
                        , "-filter:v",  fps , "-s", resolution, "-preset",  "ultrafast"
                        , r"C:\Users\user\Desktop\video timestamp project\ffmpeg vod\Reconfig_vod.mp4"], shell=True)
