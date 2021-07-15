from spotify_app import app, TOKEN_INFO, clientid, clientsecret
from flask import render_template, request, redirect, url_for, session, send_file
import os
import pandas as pd
import time
import spotipy
import datetime
from spotify_app.function_def import create_spotify_oauth, get_liked_songs, create_dataframe, get_token, get_daily_played

@app.route('/')
@app.route('/home')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    # request -> authorization_code(code)
    # access_token, refresh_token
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('getTracks',_external = True))

@app.route('/getTracks')
def getTracks():
    try:
        token_info = get_token()
    except:
        print("User not logged in!")
        redirect(url_for('login',_external = False))
    sp = spotipy.Spotify(auth=token_info['access_token'])
    all_songs = get_liked_songs(sp)
    df = create_dataframe(all_songs=all_songs, sp=sp, caller=0)
    if not os.path.exists("./Data"):
        os.makedirs("./Data")
    df.to_csv('./Data/liked_songs.csv', index=False)
    # sample_data = df.sample(n=10)

    return render_template('liked_songs.html', 
                            user = str(clientid),
                            dance = str(df['Danceability'].mean()),
                            energy = str(df['Energy'].mean()),
                            key_mean = str(df['Key'].mean()),
                            key_max = str(df['Key'].max()),
                            speech = str(df['Speechiness'].mean()),
                            acoustic = str(df['Acousticness'].mean()),
                            instrument_mean = str(df['Instrumentalness'].mean()),
                            instrument_max = str(df['Instrumentalness'].max()),
                            live = str(df['Liveness'].mean()),
                            valence = str(df['Valence'].mean()),
                            tempo_mean = str(df['Tempo'].mean()),
                            tempo_max = str(df['Tempo'].max())
                            )

@app.route('/download_liked_songs')
def download_liked_songs():
    return send_file('../Data/liked_songs.csv',
                     mimetype='text/csv',
                     attachment_filename='liked_songs.csv',
                     as_attachment=True)

@app.route('/download_played_today')
def download_played_today():
    return send_file('../Data/played_today.csv',
                     mimetype='text/csv',
                     attachment_filename='played_today.csv',
                     as_attachment=True)

@app.route('/played_today')
def played_today():
    try:
        token_info = get_token()
    except:
        print("User not logged in!")
        redirect(url_for('login',_external = False))
    sp = spotipy.Spotify(auth=token_info['access_token'])
    daily_played = get_daily_played(sp=sp)
    df = create_dataframe(all_songs=daily_played, sp=sp, caller=1)
    df['Played_On'] = pd.to_datetime(df['Played_On'])
    df = df[df.Played_On.dt.date == datetime.date.today()]
    df.to_csv('./Data/played_today.csv', index=False)
    
    return render_template('played_today.html', 
                            user = str(clientid),
                            dance = str(df['Danceability'].mean()),
                            energy = str(df['Energy'].mean()),
                            key_mean = str(df['Key'].mean()),
                            key_max = str(df['Key'].max()),
                            speech = str(df['Speechiness'].mean()),
                            acoustic = str(df['Acousticness'].mean()),
                            instrument_mean = str(df['Instrumentalness'].mean()),
                            instrument_max = str(df['Instrumentalness'].max()),
                            live = str(df['Liveness'].mean()),
                            valence = str(df['Valence'].mean()),
                            tempo_mean = str(df['Tempo'].mean()),
                            tempo_max = str(df['Tempo'].max())
                            )