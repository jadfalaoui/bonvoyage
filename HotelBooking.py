import requests

url = "https://skyscanner80.p.rapidapi.com/api/v1/hotels/prices"

querystring = {"id":"218005414","checkin":"<REQUIRED>","checkout":"<REQUIRED>","rooms":"1","adults":"2","currency":"USD","market":"US","locale":"en-US"}

headers = {
	"X-RapidAPI-Key": "fa3ebe3994mshf4255cceae92845p1c034ajsn1048793cb092",
	"X-RapidAPI-Host": "skyscanner80.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())