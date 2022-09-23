from django.shortcuts import render

# Create your views here.
def index(request):
  appid = 'c50e621666c9830dc5ea0bb0d3acc870'
  URL = 'https://api.openweathermap.org/data/2.5/weather?id='
  return render(request, 'weatherapp/index.html', {'num': num})