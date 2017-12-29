""" Random functions testing what the API can do """

import sys
import spotipy
import spotipy.util

# Scopes as defined in the Spotify API
scope = 'user-library-read user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private'


""" Constant loop that waits for user input """
def input_loop():
    sp.trace = sp.trace_out = False
    while True:
        cmd = input("").lower()

        if cmd == "quit" or cmd == "q":
            sys.exit()
        elif cmd == "trace":
            sp.trace = sp.trace_out = not sp.trace 
            print("Tracing set to {0}".format(sp.trace))
            continue

        state = sp.current_playback()

        if cmd == "pause":
            playing = state.get('is_playing')
            if playing:
                sp.pause_playback()
                print("Paused")
        elif cmd == "play":
            playing = state.get('is_playing')
            if not playing:
                sp.start_playback()
                print('Playing')
        elif cmd == "song":
            print(state.get('item').get('name'))
        else:
            print("{0} is not a valid command".format(cmd))


# Intial execution begins here

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print('Usage: {0} username'.format(sys.argv[0]))

token = spotipy.util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)

    user = sp.current_user()
    print(user.get('id'))

else: 
    print("Couldn't obtain spotify authorization for {0}".format(sys.argv[1],))
    sys.exit()