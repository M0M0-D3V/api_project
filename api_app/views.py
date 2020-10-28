from django.shortcuts import render
import requests

from mtgsdk import Card
# Create your views here.


# def index(request):
#     response = requests.get('http://freegeoip.net/json/')
#     geodata = response.json()
#     context = {
#         'ip': geodata['ip'],
#         'country': geodata['country_name']
#     }
#     return render(request, 'index.html', context)

def index(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    context = {
        'search_result': search_result
    }
    return render(request, 'index.html', context)


def mtg(request):
    response = requests.get('https://api.magicthegathering.io/v1/cards')
    cards = response.json()
    names = []
    # print(cards)
    # for i in range(len(cards)):
    # names.append(cards.name)
    context = {
        'names': names,
        'cards': cards,
    }
    return render(request, 'mtg.html', context)
