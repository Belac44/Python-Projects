import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "6c430222e0c74dd79e0d4ece1e6e0e68"
SPOTIFY_CLIENT_SECRET="ec0120a9c5d04627a43aeb2ebfc1e6dc"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
search_url = f"{BILLBOARD_URL}{date}/"

response = requests.get(search_url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("li h3.c-title")
writers = soup.select("li span.c-label.a-no-trucate")

songs = [title.getText().strip() for title in titles]
writer = [writer.getText().strip() for writer in writers]

song_uris = []
year = date.split("-")[0]
for song, artist in zip(songs, writer):
    result = sp.search(q=f"track:{song} artist:{artist} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} by {artist} doesn't exist in Spotify. Skipped.")

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)