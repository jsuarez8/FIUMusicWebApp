from musicWebAppFlask import app, forms, api_methods
from flask import render_template, request


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/topArtists', methods=["GET", "POST"])
def topArtists():
    my_form_artists = forms.MusicForms(request.form)
    if request.method == "POST":
        selected_country = request.form["country"]
        top_artists = api_methods.request_top_artists(selected_country)
        lst_artists = []
        for i in top_artists["message"]["body"]["artist_list"]:
            artist = (i["artist"]["artist_name"], i["artist"]["artist_twitter_url"])
            lst_artists.append(artist)
        return render_template("top_artists_results.html", response=lst_artists)
    return render_template("topArtists.html", form=my_form_artists)


@app.route('/topTracks', methods=["GET", "POST"])
def topTracks():
    my_form = forms.MusicForms(request.form)
    if request.method == "POST":
        selected_chart = request.form["chart"]
        selected_country = request.form["country"]
        top_tracks = api_methods.request_top_tracks(selected_country, selected_chart)
        lst_track=[]
        for i in top_tracks["message"]["body"]["track_list"]:
            track_and_charts = (i["track"]["track_name"], i["track"]["artist_name"], i["track"]["track_share_url"])
            lst_track.append(track_and_charts)
        return render_template("top_tracks_results.html", response=lst_track)
    return render_template("topTracks.html", form=my_form)
