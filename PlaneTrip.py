import google.generativeai as genai
import requests
import base64
import json

headers = {
	"X-RapidAPI-Key": "1ca56e208cmsha9767e988aa61d6p1d0d39jsn2c3ea1ffe3fd",
	"X-RapidAPI-Host": "skyscanner80.p.rapidapi.com"
}

inputBaseLocation = "Chicago"
inputDepartureDate = "2024-06-15"
inputFinalDestination = "London"
inputReturnDate = "2024-06-26"

inputAdultsGoing = 1
inputCabinClassInt = 4
inputCabinClass = ""

if inputCabinClassInt == 1:
	inputCabinClass = "economy"
if inputCabinClassInt == 2:
	inputCabinClass = "premium_economy"
if inputCabinClassInt == 3:
	inputCabinClass = "business"
if inputCabinClassInt == 4:
	inputCabinClass = "first"


#url for API 
urlFlightAutoComplete = "https://skyscanner80.p.rapidapi.com/api/v1/flights/auto-complete"
urlForRoundTrip = "https://skyscanner80.p.rapidapi.com/api/v1/flights/search-roundtrip"
urlForPriceCalender = "https://skyscanner80.p.rapidapi.com/api/v1/flights/price-calendar"

#base location ID generator
querystringAutoTrip = {"query":inputBaseLocation,"market":"US","locale":"en-US"}
responsePlaneAutoComplete = requests.get(urlFlightAutoComplete, headers=headers, params=querystringAutoTrip)
planeAutoComplete = responsePlaneAutoComplete.json()
json_stringPlaneAutoComplete = json.dumps(planeAutoComplete)
data1 = json.loads(json_stringPlaneAutoComplete)
baseLocation = data1['data'][0]['id']

#destination location ID generator 
querystringAutoTrip = {"query":inputFinalDestination,"market":"US","locale":"en-US"}
responsePlaneAutoComplete = requests.get(urlFlightAutoComplete, headers=headers, params=querystringAutoTrip)
planeAutoComplete = responsePlaneAutoComplete.json()
json_stringPlaneAutoComplete = json.dumps(planeAutoComplete)
data1 = json.loads(json_stringPlaneAutoComplete)
destinationLocation = data1['data'][0]['id']

#round Trip
querystringForTrip = {"fromId":baseLocation,"toId":destinationLocation,"departDate":inputDepartureDate,"returnDate":inputReturnDate,"adults":inputAdultsGoing,"cabinClass":inputCabinClass,"currency":"USD","market":"US","locale":"en-US"}
responseForTrip = requests.get(urlForRoundTrip, headers=headers, params=querystringForTrip)
roundTrip = responseForTrip.json()
json_stringRoundTrip = json.dumps(roundTrip)
data1 = json.loads(json_stringRoundTrip)
#roundTripToken = data1['data']['token']
#print(roundTripToken)
#print(data1['data']['itineraries'])
roundTripCost = data1['data']['itineraries'][0]['price']['formatted']
print(roundTripCost)
roundTripCarrierName = data1['data']['filterStats']['carriers'][0]['name']
print(roundTripCarrierName)

roundTripChangeFlightAllowed = data1['data']['itineraries'][0]['farePolicy']['isChangeAllowed']
roundTripPartialChangeFlightAllowed = data1['data']['itineraries'][0]['farePolicy']['isPartiallyChangeable']
roundTripCancelFlightAllowed = data1['data']['itineraries'][0]['farePolicy']['isCancellationAllowed']
roundTripPartialRefundFlightAllowed = data1['data']['itineraries'][0]['farePolicy']['isPartiallyRefundable']

roundTripOriginAirport = data1['data']['itineraries'][0]['legs'][0]['origin']['name']
roundTripDestinationAirport = data1['data']['itineraries'][0]['legs'][0]['destination']['name']

flightTravel = [roundTripCarrierName, roundTripCost, roundTripOriginAirport, roundTripDestinationAirport, roundTripChangeFlightAllowed, roundTripPartialChangeFlightAllowed, roundTripCancelFlightAllowed, roundTripPartialRefundFlightAllowed]
print(flightTravel)