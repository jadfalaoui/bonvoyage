import google.generativeai as genai
GOOGLE_API_KEY = "AIzaSyAK16t5eAfy3JAi0AKJk23Mupi5r_IKFP4"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

description = "Day 1:\nMorning:\n\t-Breakfast at Chocolatería San Ginés (Traditional Spanish breakfast spot with churros and chocolate)
        -Visit the Royal Palace of Madrid (Explore the grandeur of the Spanish monarchy)
Noon:
        -Lunch at Botín (World's oldest restaurant, serving traditional Spanish cuisine)
        -Walk through El Retiro Park (Relax and explore the beautiful gardens)
Night:
        -Attend a Flamenco show at Tablao Cordobes (Experience the vibrant and passionate dance form)
***
Day 2:
Morning:
        -Breakfast at La Mallorquina (Famous for its pastries and coffee)
        -Visit the Prado Museum (Admire masterpieces from Spanish and international artists)
Noon:
        -Lunch at Mercado de San Miguel (Gourmet market with a wide variety of food stalls)
        -Explore the Gran Vía (Madrid's iconic shopping and entertainment street)
Night:
        -Dinner at Casa Lucio (Michelin-starred restaurant known for its traditional Spanish dishes)
***
Day 3:
Morning:
        -Breakfast at Viena Capellanes (Modern breakfast cafe with a variety of options)
        -Take a day trip to Toledo (Visit the historic city with its medieval architecture and stunning cathedral)
Noon:
        -Lunch at Venta de Aires (Traditional Spanish restaurant on the outskirts of Toledo)
        -Explore the narrow streets and hidden gems of Toledo
Night:
        -Dinner at El Corral de la Morería (Renowned Flamenco venue with exquisite cuisine)
***
Day 4:
Morning:
        -Breakfast at Mantequerías York (Charming café with a wide selection of breakfast items)
        -Visit the Reina Sofía Museum (Home to Picasso's Guernica and other modern and contemporary art)
Noon:
        -Lunch at La Latina (Lively neighborhood with a variety of tapas bars and restaurants)
        -Explore the historic La Latina neighborhood (Discover its traditional charm and lively atmosphere)
Night:
        -Dinner at Casa Alberto (Traditional seafood restaurant with a lively ambiance)
***
Day 5:
Morning:
        -Breakfast at Federal Café (Hip and modern breakfast spot with a healthy and international menu)
        -Shop at El Rastro Flea Market (Explore Madrid's largest flea market for unique finds)
Noon:
        -Lunch at Cava Baja (Street with numerous tapas bars)
        -Take a farewell walk around the city center (Soak in the sights and sounds of Madrid)
"