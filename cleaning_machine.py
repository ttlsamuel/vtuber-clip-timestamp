#DO NOT RUN BEFORE YOU CHECK THE TO-BE-DELETED CONTENTS#
########################################################
import os

def cleaning(path):
    for filename in os.listdir(path):
        os.remove(os.path.join(path, filename))

cleaning(r'C:\Users\user\Desktop\video timestamp project\clip img')
cleaning(r'C:\Users\user\Desktop\video timestamp project\stream frame')
cleaning(r'C:\Users\user\Desktop\video timestamp project\stream vod')