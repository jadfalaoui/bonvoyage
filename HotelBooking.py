import requests
import json
import requests

urlForAutoComplete = "https://skyscanner80.p.rapidapi.com/api/v1/hotels/auto-complete"
urlForHotelPrices = "https://skyscanner80.p.rapidapi.com/api/v1/hotels/prices"
urlForSearch = "https://skyscanner80.p.rapidapi.com/api/v1/hotels/search"


destinationLocation = "London"
checkInDate = "2024-06-16"
checkOutDate = "2024-06-26"
roomNumber = 4
adultsComing = 5
priceTotal = "PRICE_TOTAL"
starsWantedForHotel = 4

headers = {
	"X-RapidAPI-Key": "fa3ebe3994mshf4255cceae92845p1c034ajsn1048793cb092",
	"X-RapidAPI-Host": "skyscanner80.p.rapidapi.com"
}

#For Auotcomplete
querystringForAutoComplete = {"query":destinationLocation,"market":"US","locale":"en-US"}
stringForAutoComplete = requests.get(urlForAutoComplete, headers=headers, params=querystringForAutoComplete)
forAutoComplete = stringForAutoComplete.json()
json_stringForAutoComplete = json.dumps(forAutoComplete)
data1 = json.loads(json_stringForAutoComplete)
baseLocationEntityId = data1['data'][0]['entityId']

#For Search
querystringForHotelSearch = {"entityId":baseLocationEntityId,"checkin":checkInDate,"checkout": checkOutDate,"rooms":roomNumber,"adults":adultsComing,"resultsPerPage":"1","page":"1","priceType":"PRICE_TOTAL","sorting":"-stars","stars":starsWantedForHotel,"currency":"USD","market":"US","locale":"en-US"}
stringForHotelSearch = requests.get(urlForSearch, headers=headers, params=querystringForHotelSearch)
forHotelSearch = stringForHotelSearch.json()
json_stringForHotelSearch = json.dumps(forHotelSearch)
data1 = json.loads(json_stringForHotelSearch)
hotelName = data1['data']['results']['hotelCards'][0]['name']

#ForRelativeDistance
hotelRelativeDistance = data1['data']['results']['hotelCards'][0]['distance']

#For Price
hotelPrice = data1['data']['results']['hotelCards'][0]['lowestPrice']['price']

hotelInformation = [hotelName, hotelPrice, hotelRelativeDistance]

print(hotelInformation)

