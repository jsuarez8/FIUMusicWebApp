from musicWebAppFlask import main_functions
import requests


def request_key():
    apiDict = main_functions.read_from_file("musicWebAppFlask/JSON_Documents/api_keys.json")
    return apiDict['key']


def request_top_artists(country_code):
    url = "https://api.musixmatch.com/ws/1.1/chart.artists.get" \
          "?country=" + country_code + "&page_size=10&apikey=" + request_key()
    response = requests.get(url).json()
    return response


def request_top_tracks(country_code, chart_name):
    url2 = "https://api.musixmatch.com/ws/1.1/chart.tracks.get" \
           "?country=" + country_code + "&chart_name=" + chart_name + "&page_size=10&apikey=" + request_key()
    response2 = requests.get(url2).json()
    return response2
