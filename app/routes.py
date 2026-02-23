from flask import Blueprint, render_template, request, redirect, url_for, flash
from .extensions import db
from .models import Song
from sqlalchemy import func

bp = Blueprint("main", __name__)

@bp.get("/")
def home():
    return redirect(url_for("main.songs_list"))

@bp.get("/songs")
def songs_list():
    q = request.args.get("q", "").strip()
    query = Song.query
    if q:
        query = query.filter(Song.title.ilike(f"%{q}%"))

    songs = query.order_by(Song.created_at.desc()).all()

    # Dashboard counts (not affected by search)
    total = Song.query.count()
    draft = Song.query.filter_by(status="Draft").count()
    registered = Song.query.filter_by(status="Registered").count()
    released = Song.query.filter_by(status="Released").count()

    return render_template(
        "songs_list.html",
        songs=songs,
        q=q,
        total=total,
        draft=draft,
        registered=registered,
        released=released,
    )

@bp.route("/songs/new", methods=["GET", "POST"])
def songs_new():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        writers = request.form.get("writers", "").strip() or None
        album = request.form.get("album", "").strip() or None
        status = request.form.get("status", "Draft").strip() or "Draft"
        notes = request.form.get("notes", "").strip() or None

        if not title:
            flash("Title is required.", "error")
            return render_template("songs_new.html")

        song = Song(title=title, writers=writers, album=album, status=status, notes=notes)
        db.session.add(song)
        db.session.commit()

        flash("Song added.", "success")
        return redirect(url_for("main.songs_list"))

    return render_template("songs_new.html")

@bp.route("/songs/<int:song_id>/edit", methods=["GET", "POST"])
def songs_edit(song_id: int):
    song = Song.query.get_or_404(song_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        writers = request.form.get("writers", "").strip() or None
        album = request.form.get("album", "").strip() or None
        status = request.form.get("status", "Draft").strip() or "Draft"
        notes = request.form.get("notes", "").strip() or None

        if not title:
            flash("Title is required.", "error")
            return render_template("songs_edit.html", song=song)

        song.title = title
        song.writers = writers
        song.album = album
        song.status = status
        song.notes = notes

        db.session.commit()
        flash("Song updated.", "success")
        return redirect(url_for("main.songs_list"))

    return render_template("songs_edit.html", song=song)


@bp.post("/songs/<int:song_id>/delete")
def songs_delete(song_id: int):
    song = Song.query.get_or_404(song_id)
    db.session.delete(song)
    db.session.commit()
    flash("Song deleted.", "success")
    return redirect(url_for("main.songs_list"))