from flask import render_template, redirect, url_for, request
from app import app
from album import albums

albums = []

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        newAlbumID = request.form.get("albumID", "")
        newAlbumName = request.form.get("albumName", "")
        newAlbumType = request.form.get("albumType", "")
        newReleaseDate = request.form.get("releaseDate", "")

        newAlbum = Album(albumID=newAlbumID, albumName=newAlbumName,
        albumType=newAlbumType, releaseDate=newReleaseDate)
        albums.append(newAlbum)
        return redirect (url_for("index"))
    return render_template('index.html' , pageheader="album", albums=albums)