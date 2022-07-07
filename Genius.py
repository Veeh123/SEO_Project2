import requests
import json
import sqlalchemy as db
import pandas as pd



def Genius():
#cont = True
	while True:	

		artist = input("input an Artist name: ")

		url = "https://genius.p.rapidapi.com/search"

		querystring = {"q":artist}

		headers = {
			"X-RapidAPI-Key": "22251c60demsh8ba7718637f6696p162e43jsnd56247a114ef",
			"X-RapidAPI-Host": "genius.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		data = json.loads(response.text)['response']['hits']
		name = []
		song_title = []
		for item in data:
			name.append(item['result']['primary_artist']['name'])
			song_title.append(item['result']['title'])

		derived_data = {'name': name, 'Song Title': song_title}
		genius_info = pd.DataFrame(derived_data)
		engine = db.create_engine('sqlite:///artist_hits.db')
		genius_info.to_sql('artist_songs', con=engine, if_exists='replace', index=False)
		query_result = engine.execute("SELECT * FROM artist_songs;").fetchall()
		print(pd.DataFrame(query_result))

		user_answer = input('Would you like to continue(Y/N)?: ')
		if user_answer == 'N':
			# stop the program when done
			print('Thank you for using our genius API <_>!!')
			break
Genius()

