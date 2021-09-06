from flask import Flask
from flask import request
from flask import jsonify
from player import MPVPlayer
import json

app = Flask(__name__)
mp = MPVPlayer()

@app.route('/')
def root():
    return 'PlayerD working'

@app.route('/status')
def status():
    return mp.get_status()

@app.route('/action')
def action():

    action = request.args.get('type')
    arg = request.args.get('arg')

    if action == "resume":
        mp.resume()
    elif action == "pause":
        mp.pause()
    elif action == "close":
        mp.close()
    elif action == "go_at":
        if arg == None:
            return {'status': 400}
        mp.go_at(arg)
    elif action == "volume":
        if arg == None:
            return {'status': 400}
        mp.set_volume(arg)
    elif action == "play":
        if arg == None:
            return {'status': 400}
        mp.play(arg)
    elif action == "playlist_append":
        if arg == None:
            return {'status': 400}
        mp.playlist_append(arg)
    elif action == "playlist_remove":
        if arg == None:
            return {'status': 400}
        mp.playlist_remove(arg)
    elif action == "playlist_clear":
        mp.playlist_clear(arg)
    elif action == "playlist_go":
        if arg == None:
            return {'status': 400}
        mp.playlist_go(arg)

    return {'status': 200}