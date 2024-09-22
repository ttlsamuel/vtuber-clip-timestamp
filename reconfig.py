from file_func import name_extract, cleaning
import subprocess
import os

# adjust reconfig_vid metadata here
fps         = "fps=5"
resolution  = "320x240"

def reconfigure():
    # executing reconfiguration of raw vod
    cleaning(r'C:\Users\user\Desktop\video timestamp project\ffmpeg vod')
    raw_vod_name = (name_extract(r"C:\Users\user\Desktop\video timestamp project\raw vod") )
    subprocess.run([ "ffmpeg", "-i"  , raw_vod_name
                        , "-filter:v",  fps , "-s", resolution, "-preset",  "ultrafast"
                        , r"C:\Users\user\Desktop\video timestamp project\ffmpeg vod\reconfig_vod.mp4"], shell=True)
    os.rename(r'C:\Users\user\Desktop\video timestamp project\ffmpeg vod\reconfig_vod.mp4',
              r'C:\Users\user\Desktop\video timestamp project\ffmpeg vod\\' + 'RECONFIG ' +
              os.listdir(r"C:\Users\user\Desktop\video timestamp project\raw vod")[0] )


if __name__ == "__main__":
    reconfigure()
