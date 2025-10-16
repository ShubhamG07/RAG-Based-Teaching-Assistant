import os
import subprocess

files =os.listdir("Videos")

for file in files:
    print(file)
    subprocess.run(["ffmpeg","-i",f"Videos/{file}",f"Audios/{file}.mp3"])