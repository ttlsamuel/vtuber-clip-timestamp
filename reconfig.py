from file_func import name_extract, cleaning
import subprocess

# adjust reconfig_vid metadata here
fps         = "fps=5"
resolution  = "320x240"

def reconfigure():
    # executing reconfiguration of raw vod
    cleaning(r'C:\Users\user\Desktop\video timestamp project\ffmpeg vod')
    raw_vod_name = (name_extract(r"C:\Users\user\Desktop\video timestamp project\raw vod") )
    subprocess.run([ "ffmpeg", "-i"  , raw_vod_name
                        , "-filter:v",  fps , "-s", resolution, "-preset",  "ultrafast"
                        , r"C:\Users\user\Desktop\video timestamp project\ffmpeg vod\Reconfig_vod.mp4"], shell=True)
