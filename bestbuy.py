import requests

url = "https://bestbuyraygorodskijv1.p.rapidapi.com/getAllCategories"

payload = "apiKey=%3CREQUIRED%3E"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "BestBuyraygorodskijV1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)