import requests
from pprint import pprint 

def extraction(url):
    response = requests.get(url)
    return response.json()

def transform(data):
    palavras = []
    for item in data:
        body = item["body"]
        body_upper = body.upper()
        body_replaced = body_upper.replace("\n","")
        palavras.append(body_replaced)
    return palavras 

url = "https://jsonplaceholder.typicode.com/posts"
data_raw = extraction(url)
pprint(data_raw)
data_stg = transform(data_raw)
pprint(data_stg)
        
         
