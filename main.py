import requests
from bs4 import BeautifulSoup


import spotipy
date = input("What year yould you like to travel to? Type the data in this format YYYY-MM-DD")





response =requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
soup = BeautifulSoup(response.text,"html.parser")
song_names = soup.select("li  ul li  h3",id="title-of-a-story",class_="c-title")
song_names = [name.getText().strip() for name in song_names]
print(song_names)


token = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIFY_URL,
                            client_secret=SPOTIFY_KEY,
                            redirect_uri="http://example.com",
                            state=None, scope="playlist-modify-private", cache_path=None,
                            username=None, proxies=None, show_dialog=False,
                            requests_session=True, requests_timeout=None)
sp = spotipy.Spotify(auth_manager=token)
link = sp.user_playlist_create(user= sp.current_user()["id"],name=f"{date}",public=False,description="no")

url_list = []
for track in song_names:
    try:
        url_list.append(sp.search(q="track:" + track, limit=1, offset=0, type="track")["tracks"]["items"][0]["external_urls"]["spotify"])

    except IndexError:
        continue
print(url_list)
sp.playlist_add_items(playlist_id = link["external_urls"]["spotify"],items= url_list,position=None)