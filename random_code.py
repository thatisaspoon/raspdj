""" Random functions testing what the API can do """

import sys
import spotipy
import spotipy.util

""" Constant loop that waits for user input """
def input_loop():
    sp.trace = sp.trace_out = False
    while True:
        cmd = input("").lower()

        if cmd == "quit" or cmd == "q":
            sys.exit()

        state = sp.current_playback()

        if cmd == "pause":
            playing = state.get('is_playing')
            if playing:
                sp.pause_playback()
                print("Paused")
        if cmd == "play":
            playing = state.get('is_playing')
            if not playing:
                sp.start_playback()
                print('Playing')
        if cmd == "song":
            print(state.get('item').get('name'))
        if cmd == "trace":
            if sp.trace == True:
                sp.trace = sp.trace_out = False
            else:
                sp.trace = sp.trace_out = True
        


# Scopes as defined in the Spotify API
scope = 'user-library-read user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print('Usage: {0} username'.format(sys.argv[0]))

token = spotipy.util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)

    # Shows the HTTP GET and RESP packets
    sp.trace = True
    sp.trace_out = True

    user = sp.current_user()
    print(user.get('id'))

    playback = sp.current_playback()

    curr_song = playback.get('item')

    if curr_song:
        artist_list = curr_song.get('artists')
        artists = []
        for artist in artist_list:
            artists.append(artist.get('name'))

        print('Current song: {0} - {1}'.format(curr_song.get('name'), ', '.join(artists)))

    curr_device = playback.get('device')
    print('Current playback device: {0}'.format(curr_device.get('name')))

    curr_device_id = curr_device.get('id')

    input_loop()

else: 
    print("Couldn't obtain spotify authorization for {0}".format(sys.argv[1],))
    sys.exit()