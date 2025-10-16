import requests
import os
import json
import pandas as pd
import numpy as np
import joblib

def create_emb(text_list):
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

# a=create_emb(["Cat sat on mat","Rat run on the mat"])
# print(a)

files=os.listdir("Json")
chunk_id=0
my_dict=[]

for file in files:
    with open(f"Json/{file}") as f:
        content=json.load(f)
    print(f"creating embeddings for {file}")
    embeddings=create_emb([c["text"] for c in content["chunks"]])
   
    for i,chunk in enumerate(content["chunks"]):
        chunk["chunk_id"]=chunk_id
        chunk["embedding"]=embeddings[i]
        my_dict.append(chunk)
        chunk_id +=1

df=pd.DataFrame.from_records(my_dict)

joblib.dump(df,"embeddings.joblib")

