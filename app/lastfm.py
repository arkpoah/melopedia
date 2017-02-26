import urllib2, urllib
import json
from config import LASTFM_API_KEY

def artist_infos(artist):
  url = "http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=" + urllib.quote_plus(artist) + "&api_key=" + LASTFM_API_KEY + "&format=json"
  response = urllib2.urlopen(url)
  data = json.load(response)
  artist_info = {
          "img_url": "",
          "url": "",
          "description":"",
          }
  try:
      artist_info = {'img_url': data["artist"]["image"][1]["#text"], 'url': data["artist"]["url"], "description": data["artist"]["bio"]["summary"]}
  except: pass

  return artist_info
