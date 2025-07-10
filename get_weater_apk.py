import requests
 
city_name=input('enter the city name: ')
API_key='1d47cc4b988583f55c55e3527f50a7d0'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&unit=metric'

response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print('weather is:',data['weather'][0]['description'])
    print("themprature is:",data[ 'main']['temp'])
    print('humidity is:',data['main']['humidity'])