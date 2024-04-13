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

class AIAPIView(APIView):
    def post(self, request, *args, **kwargs):
        input_data = request.data
        print(input_data)
        result = blackbox(input_data)
        return Response(result, status=status.HTTP_200_OK)
    