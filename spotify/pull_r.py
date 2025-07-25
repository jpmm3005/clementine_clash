import requests
import scrape 
import json
import pandas as pd


access_token = scrape.access_token

headers = {
    "Authorization": f"Bearer {access_token}"
}

artist_id = "7tr9pbgNEKtG0GQTKe08Tz"
url = "https://api.spotify.com/v1/me/top/artists?limit=10&time_range=medium_term"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    top_artists_data = response.json()
    with open('top_artists.json', 'w') as f:
        json.dump(top_artists_data, f, indent=4)
    print("Top artists retrieved:")
    
    # Convert to DataFrame
    artist_list = [{
        "name": artist["name"],
        "popularity": artist["popularity"],
        "genres": artist["genres"],
        "followers": artist["followers"]["total"]
    } for artist in top_artists_data["items"]]

    df = pd.DataFrame(artist_list)
    print(df)
else:
    print("Error:", response.status_code, response.text)

