import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import google.generativeai as gemini

GOOGLE_API_KEY= "AIzaSyAoaSv_0V1dxXfkdorC10rKbH3R5i68Fmw"

gemini.configure(api_key=GOOGLE_API_KEY)

model = gemini.GenerativeModel('gemini-pro')

     
age = int(input("Age: "))
groupSize = int(input("Group size: "))
budget = int(input("Budget: "))
city = input("City: ")
vacationType=input("Vacation type: ")

response = model.generate_content("I'm "+str(age)+" years old and traveling with a group of "+str(groupSize)+ " to "+city+" with a budget of USD"+str(budget)+" and looking for a "+vacationType+" style of vacation, suggest a comprehensive list of activities")
print(response.text)



