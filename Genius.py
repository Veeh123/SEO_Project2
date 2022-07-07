import requests
import json
import sqalchemy as db
import pandas as pd

def function1(x):
	return x * 0

def function2(x, y):
	return (x + y)

artist = input("input an Artist name: ")

url = "https://genius.p.rapidapi.com/search"

querystring = {"q":artist}

headers = {
	"X-RapidAPI-Key": "22251c60demsh8ba7718637f6696p162e43jsnd56247a114ef",
	"X-RapidAPI-Host": "genius.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)['response']['hits']
for item in data:
        # Print the artist and title of each result
    print(item['result']['primary_artist']['name']
              + ': ' + item['result']['title'])

genius_info = pd.DataFrame(data)
engine = db.create_engine('sqlite:///artist_hits.db')
genius_info.to_sql('user_artists, con=engine, if_exists='replace', index=False)
query_result = engine.execute("SELECT * FROM user_artists;").fetchall()
print(pd.DataFrame(query_result))