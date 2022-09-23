from django.shortcuts import render
import requests

# Create your views here.
def index(request):
  appid = 'c50e621666c9830dc5ea0bb0d3acc870'
  URL = 'https://api.openweathermap.org/data/2.5/weather?id='
  PARAMS = {'q': 'amsterdam', 'appid': appid, 'units': 'metric'}
  r = requests.get(url=URL, params=PARAMS)
  res = r.json()
  description = res['weather'][0]['description']
  icon = res['weather'][0]['icon']
  temp = res['main']['temp']
  return render(request, 'weatherapp/index.html', {'description': description, 'icon':icon, 'temp':temp})