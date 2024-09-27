from datetime import datetime
from file_func import name_extract, time_output
import os
import re

# using audio_offset_finder By BBC
def audio_matching():

    print("Executing programme, please wait...")

    start_time = datetime.now()
    clip_audio = (name_extract(r"C:\Users\user\Desktop\video timestamp project\clip audio") )
    raw_audio  = (name_extract(r"C:\Users\user\Desktop\video timestamp project\raw vod") )
    audio_txt  = r"C:\Users\user\Desktop\video timestamp project\audio_timestamp.txt"

    # running command and storing output into a text file
    os.system("audio-offset-finder " + "--find-offset-of " +  "\"" + clip_audio +  "\""+ " --within "
              + "\"" + raw_audio + "\""
              + ">" + "\"" + audio_txt + "\"")

    # read timestamp from text file
    with open(audio_txt) as f:
        audio_time = f.readline()
        audio_time = re.findall(r"\d*\.*\d+", audio_time)
        audio_time = float(str(audio_time[0]))


    time_output(audio_time)
    end_time = datetime.now()
    print('Runtime: {}'.format(end_time - start_time) + "\n")


if __name__ == '__main__':
    audio_matching()

