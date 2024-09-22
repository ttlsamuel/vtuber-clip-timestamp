from datetime import datetime
import subprocess

def yt_download():
    start_time = datetime.now()

    yt_link = input("Enter your youtube url here: ")
    subprocess.run(["yt-dlp", "-F", yt_link])

    dl_format = input( "\n" + "Choose your download format by entering the corresponding id: ")
    subprocess.run(["yt-dlp", "--output" , r"C:\Users\user\Desktop\video timestamp project\raw vod\%(title)s.%(ext)s"
                       , "--embed-thumbnail", "-f", dl_format, "--merge-output-format", "mp4" , yt_link])

    end_time = datetime.now()
    print('Runtime: {}'.format(end_time - start_time) + "\n")


if __name__ == '__main__':
    yt_download()
