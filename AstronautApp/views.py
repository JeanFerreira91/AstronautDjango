from pprint import pprint
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url = 'http://api.open-notify.org/astros.json'
    url_request = requests.get(url)
    data = url_request.json()
    total_astronauts = data['number']
    context = {
        'data': data,
        'total_astronauts': total_astronauts
    }
    pprint(data)
    return render(request, 'AstronautApp/index.html', context)