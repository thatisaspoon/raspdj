""" Command line version of Spotify control via the web API """

import sys
import spotipy
import spotipy.util

# Scopes as defined in the Spotify API
scope = 'user-library-read user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private'

def play_pause():
    playing = sp.currently_playing().get('is_playing')
    if playing:
        sp.pause_playback()
        print('Paused')
    else:
        sp.start_playback()
        print("Playing")

def song_info():
    track = sp.currently_playing().get('item')
    if track:
        name = track.get('name')

        artist_list = track.get('artists')
        artists = []
        for artist in artist_list:
            artists.append(artist.get('name'))
        
        print("{0} by {1}".format(name, ', '.join(artists)))
    else:
        print("No track is playing")

def main_loop():
    print('henlo')

    while True:
        cmd = input("").lower()

        if cmd == "quit" or cmd == "q":
            break

        elif cmd == "trace":
            sp.trace = sp.trace_out = not sp.trace 
            print("Tracing set to {0}".format(sp.trace))
            continue

        # Playback controls
        elif cmd == "next":
            sp.next_track()
            song_info()

        elif cmd == "prev":
            sp.previous_track()
            song_info()

        elif cmd == "pause":
            play_pause()

        elif cmd == "play":
            play_pause()

        # Info controls
        elif cmd == "song":
            song_info()


    sys.exit()

#username = input("Spotify username: ")

# Set to a constant since it's really only me using this atm
username = 'thatisaspoon'

token = spotipy.util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    user = sp.current_user()
    print("Obtained token for {0}".format(username,))
    main_loop()

else: 
    print("Couldn't obtain spotify authorization for {0}".format(username,))
    sys.exit()
