import google.generativeai as genai
GOOGLE_API_KEY = "AIzaSyAK16t5eAfy3JAi0AKJk23Mupi5r_IKFP4"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

vacDescInput = str(input("Please give me a concise description of the vacation you'd like to go on (in 1 sentence): "))

locSuggestion = model.generate_content("I'd like to go on a vacation that best fits this description: " + vacDescInput + ".\n" +
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
print(response)
sentences = response.split("\n")

if sentences[len(sentences) - 1] == "":
    sentences.pop()

print(sentences)

# Split each string at the period and then flatten the list
split_list = [item for s in sentences for item in s.split('.', 1)]

# Correcting the format to ensure periods remain with the first part of each split
formatted_list = [item + '.' if not item.endswith('.') else item for item in split_list]

print("")

print(formatted_list)
