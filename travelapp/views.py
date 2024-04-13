from django.shortcuts import render
import pathlib
import textwrap
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# Create your views here.

GOOGLE_API_KEY= "AIzaSyAoaSv_0V1dxXfkdorC10rKbH3R5i68Fmw"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
def blackbox(data):
    city = data["city"]
    groupType = data["groupType"]
    spunk = data["spunk"]
    relax = data["relax"]
    expense = data["expense"]
    response = model.generate_content("I am traveling to "+city+", my group consists of "+groupType+". On a scale of 1 to 10, I would like the trip to have the following attributes - Spunky:"+spunk+"/10, Relaxing:"+relax+"/10, Expensive:"+expense+"/10. Give me a travel plan for 4 days corresponding to these constraints.(Do not give ratings for each element of the plan, I trust that you took the parameters in consideration for each choice.)")
    return response.text

def index(request):
    context = {}
    return render(request,'index.html')

def locChoices(data):
    #"Please give me a concise description of the vacation you'd like to go on (in 1 sentence): "
    vacDescr = "asian famous cities" #data["vacDescr"]

    locSuggestion = model.generate_content("I'd like to go on a vacation that best fits this description: " + vacDescr + ".\n" +
    "Please provide 5 cities (with their country) that would best fit this description, along with a brief description in of around " +
    "5 to 12 words that best describes the theme of the trip. Make the themes vary within reason between the 5 options. Also try and vary " + 
    "how expensive the 5 locations are (so that not all 5 places are super expensive nor super cheap) unless specified otherwise by the description.\n" + 
    "For each pair of location and theme, please exactly use the following format: " +  
    "\"<City>, <Country>.<Theme>\"\n" + 
    "When formatting, please follow these rules exactly:\n" +
    "1. For each pair of location and theme, only use the period character exactly once: once at the end of the location part, " + 
    "separating the location from the theme. Never use a period elsewhere, even if it is correct to do so. For example, instead of " + 
    "outputting: \"Washington D.C.\", please output \"Washington DC\" instead.\n" + 
    "2. For each pair of location and theme, please do not insert a space after the splitting period. There must be only one period following " +
    "the country that splits the location and theme sections, and there must not be a space after the period.\n" + 
    "3. Please use a new line after every pair of location and theme.\n")

    response = locSuggestion.text
    sentences = response.split("\n")

    if sentences[len(sentences) - 1] == "":
        sentences.pop()

    # Split each string at the period and then flatten the list
    split_list = [item for s in sentences for item in s.split('.', 1)]

    # Correcting the format to ensure periods remain with the first part of each split
    formatted_list = [item + '.' if not item.endswith('.') else item for item in split_list]

    return formatted_list

class AIAPIView(APIView):
    def post(self, request, *args, **kwargs):
        input_data = request.data
        print(input_data)

        locList = locChoices(input_data)
        print(locList)
        #Return formatted list of blackbox data
        result = blackbox(input_data)

        return Response(result, status=status.HTTP_200_OK)
    