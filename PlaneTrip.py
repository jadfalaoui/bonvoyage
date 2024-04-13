
import google.generativeai as genai
import requests
import base64
import json

headers = {
	"X-RapidAPI-Key": "1ca56e208cmsha9767e988aa61d6p1d0d39jsn2c3ea1ffe3fd",
	"X-RapidAPI-Host": "skyscanner80.p.rapidapi.com"
}

inputBaseLocation = "Madrid"
inputDepartureDate = "2024-11-04"
inputFinalDestination = "Chicago"
inputReturnDate = "2024-11-09"

inputAdultsGoing = 5
inputCabinClassInt = 4
inputCabinClass = ""

if inputCabinClassInt == 1:
	inputCabinClass = "economy"
if inputCabinClass == 2:
	inputCabinClass = "premium_economy"
if inputCabinClass == 3:
	inputCabinClass = "business"
if inputCabinClass == 4:
	inputCabinClass = "first"


#url for API 
urlFlightAutoComplete = "https://skyscanner80.p.rapidapi.com/api/v1/flights/auto-complete"
urlForRoundTrip = "https://skyscanner80.p.rapidapi.com/api/v1/flights/search-roundtrip"
urlForPriceCalender = "https://skyscanner80.p.rapidapi.com/api/v1/flights/price-calendar"

#base location ID generator
querystringAutoTrip = {"query":inputBaseLocation,"market":"US","locale":"en-US"}
responsePlaneAutoComplete = requests.get(urlFlightAutoComplete, headers=headers, params=querystringAutoTrip)
planeAutoComplete = responsePlaneAutoComplete.json()
json_string = json.dumps(planeAutoComplete)
data = json.loads(json_string)
baseLocation = data['data'][0]['id']

#destination location ID generator 
querystringAutoTrip = {"query":inputFinalDestination,"market":"US","locale":"en-US"}
responsePlaneAutoComplete = requests.get(urlFlightAutoComplete, headers=headers, params=querystringAutoTrip)
planeAutoComplete = responsePlaneAutoComplete.json()
json_string = json.dumps(planeAutoComplete)
data = json.loads(json_string)
destinationLocation = data['data'][0]['id']



querystringForTrip = {"fromId":baseLocation,"toId":destinationLocation,"departDate":inputDepartureDate,"returnDate":inputReturnDate,"adults":inputAdultsGoing,"cabinClass":inputCabinClass,"currency":"USD","market":"US","locale":"en-US"}
responseForTrip = requests.get(urlForRoundTrip, headers=headers, params=querystringForTrip)
print(responseForTrip.json())

#Price generator
querystring = {"fromId":baseLocation,"toId":destinationLocation,"departDate":inputDepartureDate,"returnDate":inputReturnDate,"currency":"USD","market":"US","locale":"en-US"}
response = requests.get(urlForPriceCalender, headers=headers, params=querystring)
print(response.json())







