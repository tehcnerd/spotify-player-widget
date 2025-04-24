# spotify-player-widget
an aesthetic spotify player widget that doesn't need a premium account for playback control. (local workaround)
# Snapshots 
![image](https://github.com/user-attachments/assets/b806abe1-8b38-4cc8-af27-d15ccc127e92)
![image](https://github.com/user-attachments/assets/a07b74ce-d1a2-4184-963d-fe13939e6744)

# requirements 
spotipy python library for api calls 
```pip install spotipy```

a spotify developer account, create an application with Web API.
![image](https://github.com/user-attachments/assets/e88d0df8-87d3-4ef9-a338-9e2ed99c6f7e)
add a redirect URL. (will come in handy when running the widget for the first time.)

get the ```client id (api key)``` and ```client secret```.

when running the ```spotifyui.py``` for the first time, you might be redirected (or not) to the *redirect-url* (in our case its ```https://www.google.com```) and will be
prompted to type in the same url in the CLI or the terminal, type the *redirect-url* you used in your Spotify Developer Application to verify the api call.

Note : No need to do it after initialising it for the first time. It stored it in cache.
