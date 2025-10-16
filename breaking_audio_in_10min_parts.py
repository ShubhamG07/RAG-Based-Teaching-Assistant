import os
import subprocess
from pydub import AudioSegment

files =os.listdir("Audios")

len_audio=[]

for file in files:
    file_path = os.path.join("Audios",file)
    audio = AudioSegment.from_file(file_path)
    len_audio.append(len(audio)/1000)

print(len_audio)
j=0

for file in files:
    i=0
    k=0
    while(i<=len_audio[j]):
         print(f"processing video {j+1} part- {k+1}")
         subprocess.run(["ffmpeg","-ss",str(i),"-i",f"Audios/{file}","-t",str(600),"-acodec","copy",f"Audio/{j+1}_{file}_part-{k+1}.mp3"])
         i=i+600
         k=k+1
    j=j+1
