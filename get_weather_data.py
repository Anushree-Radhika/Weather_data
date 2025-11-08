import requests

city_name = input("Enter the city name whose weather information you want to get:")
#you can generate your own API key and use
API_key = '2aabeb01c80822d556528830da40a9c5'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    print("\nThe city's name is:",data['name'])
    print('The longitudenal and latitudenal coordinates respectively are: ',data['coord']['lon'],'and',data['coord']['lat'])
    print('Weather is', data['weather'][0]['description'])
    print('The current temperature of the city in Celsius:',data['main']['temp'],'and feels like',data['main']['feels_like'],'with temperature minimum and maximum being',data['main']['temp_min'] ,'and',data['main']['temp_max'] )
    print('The current pressure is :',data['main']['pressure'])
    print('The current humidity is :',data['main']['humidity'])

    print('The current wind speed is :',data['wind']['speed'])
