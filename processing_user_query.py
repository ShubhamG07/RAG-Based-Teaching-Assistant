import pandas as pd
import numpy as np
import joblib
import requests
import json
from groq import Groq
from sklearn.metrics.pairwise import cosine_similarity


def create_emb(text_list):
    # r=requests.post("http://localhost:11434/api/embed",json={
    #     "model":"bge-m3",
    #     "input":text_list
    # })

   

    # embedding=r.json()["embeddings"]
    # return embedding


    url = "https://api.jina.ai/v1/embeddings"
    headers = {
        "Authorization": f"Bearer your_jina_api_key",  # get from https://jina.ai/embeddings
        "Content-Type": "application/json"
    }
    data = {
        "model": "jina-embeddings-v2-base-en",
        "input": text_list
    }

    resp = requests.post(url, json=data, headers=headers)
  

    embeddings = [item["embedding"] for item in resp.json()["data"]]
    # print(embeddings)
    return embeddings


def generate_response(prompt):
   
    client = Groq(

        api_key="Your_groq_API_Key",

    )


    chat_completion = client.chat.completions.create(

        messages=[

            {

                "role": "user",

                "content": prompt,

            }

        ],

        model="llama-3.3-70b-versatile",

    )


    return chat_completion.choices[0].message.content


df=joblib.load("embeddings.joblib")

incoming_question=input("Enter a question : ")

question_embedding=create_emb([incoming_question])[0]

# print(question_embedding)
# print(np.vstack(df["embedding"].values))
# print(np.vstack(df["embedding"]).shape)

similarity= cosine_similarity(np.vstack(df["embedding"]),[question_embedding]).flatten()

top_results=10

max_idx=similarity.argsort()[::-1][0:top_results]
new_df = df.loc[max_idx]
# print(new_df[["video_no.","title","part","text"]])

prompt=f'''Here are the video chunks containing video no. ,video title, part, video text, start time of text and end time of that text

{new_df[["video_no.","title","part","text","start","end"]].to_json(orient='records')}

"{incoming_question}"

The user asked this question related to video chunks,you have to answer where and how much content is thought in which video (and at what timestamp) and guide user to go to that specific part of that video, if its part 1 just conver time in minutes and tell at that time in that particular video title(dont tell part no.), if its in part other than part 1 then add 10 minute in total time for each part before that part till part 1 and give time in minutes and second and tell only video title with it (not part). If user asked unrelated question tell them you can only answer question related to this course. Do not ask any  further question to them automatically.
'''

with open("prompt.txt","w") as f:
    f.write(prompt)
# for i, item in new_df.iterrows():
#     print(item["video_no."],item["title"],item["part"],item["text"],item["start"],item["end"])

response = generate_response(prompt)
print(response)


with open("response.txt","w") as f:
    f.write(response)