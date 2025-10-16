import os
from groq import Groq
import json

# Initialize the Groq client
client = Groq( api_key="Your_Groq_API_key")

files =os.listdir("Audio")


for f in files:
    # Specify the path to the audio file
    filename = os.path.join("Audio", f)
    number=f.split("_")[0]
    title=f.split("_")[1].split(".mp4")[0]
    part=f.split("mp3_")[1].split(".mp3")[0]


    with open(filename, "rb") as file:
        # Create a translation of the audio file
        translation = client.audio.translations.create(
        file=(filename, file.read()), # Required audio file
        model="whisper-large-v3", # Required model to use for translation
        prompt="Specify context or spelling",  # Optional
        response_format="verbose_json"
        )

   
        chunks=[]

        for s in translation.segments:
            chunks.append({"video_no.":number,"title":title,"part":part,"start":s["start"],"end":s["end"],"text":s["text"]})

        chunks_with_metadata={"chunks":chunks,"text":translation.text}

        with open(f"Json/{f}.json","w") as m:
            json.dump(chunks_with_metadata,m)
            

        # print(chunks)

        # with open("output.json","w") as f:
        #     json.dump(chunks,f)