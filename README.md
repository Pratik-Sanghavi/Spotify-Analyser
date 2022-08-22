# Spotify-Analyser
A basic flask web application to display user's liked songs features, download liked songs' csv, download daily played history, graphs displaying daily played songs features, etc. User can select and download mp3 file of songs liked/played today (a bit glitchy though-I apologise!!😅).
Note:- For songs played today, only the most recent 50 songs are supported currently. I'm trying to figure out how I could incorporate songs beyond that. Do let me know if you figure something out (Thanks!)

## I) Dependencies:-
1. Flask<br>
`pip install flask`
2. Pandas<br>
`pip install pandas`
3. os<br>
`pip install os`
4. Spotipy<br>
`pip install spotipy`
5. ffmpeg<br>
`choco install ffmpeg`
6. Beautiful Soup<br>
`pip install beautifulsoup4`
7. Selenium<br>
`pip install selenium`
8. Chrome Webdriver (corresponding to your chrome version)<br>
Download chrome webdriver [here](https://chromedriver.chromium.org/downloads) and add file to PATH (System variable)
9. Requests<br>
`pip install requests`
10. youtube_dl<br>
Download youtube_dl [here](https://github.com/ytdl-org/youtube-dl) and add youtube_dl.exe(in bin) to PATH (System variable)<br>
`pip install youtube_dl`
11. dotenv <br>
`pip install python-dotenv`

Next time venv please!!! (Let me know if there's any other dependency)

## II) Setting up
1. Register on Spotify Developers and create an app to get client id and client secret. 
2. In edit settings on spotify developer dashboard page, fill in redirect uri as `http://127.0.0.1:5000/redirect`
3. Create a .env file in spotify_app folder and add:<br>
CLIENT_ID = "YOUR CLIENT ID"<br>
CLIENT_SECRET = "YOUR CLIENT SECRET"<br>


That should be sufficient I guess to get the flask application up and running (`python run.py`). Do let me know if I need to make any changes/furnish more details<br>

## III) Additional features planned
Initially I had intended this web application to serve as some sort of indicator of my mood. For this, what we can do is that every time I hear a new song, I can implement a form on the Daily Played page to make note of the mood I am in. This we can use to train a classifier to generate a color depending on my mood.
