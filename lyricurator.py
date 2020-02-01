from lyrics_util import *


def prepare_tweet():
    while True:
        artists = get_artists_links()

        if not artists:
            continue

        selected_artist = random.choice(artists)

        # 'selected_song' is a tuple where 1st is song name and 2nd is its link
        artist_name, selected_song = get_artist_name_and_song(selected_artist)

        if not artist_name or not selected_song:
            continue

        song_lyrics = get_lyrics(selected_song[1])

        if not song_lyrics:
            continue

        lyrics_portion = get_lyrics_portion(song_lyrics)

        if lyrics_portion:
            return artist_name, selected_song[0], lyrics_portion


print(prepare_tweet())