import requests
from pprint import pprint

# GET https://api.chucknorris.io/jokes/random
# https://randomuser.me/
# https://v2.jokeapi.dev/
# https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious
# https://v2.jokeapi.dev/joke/Programming
if __name__ == '__main__':
    # data = requests.get('https://api.chucknorris.io/jokes/random')
    # data = requests.get("https://randomuser.me/api/")
    data = requests.get("https://v2.jokeapi.dev/joke/Programming")
    # discord, perlu login buat dapetin passwordnya / API token
    # API token, baru kamu bisa main2 ke discord
    pprint(data.json())
