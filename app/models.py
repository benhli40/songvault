from datetime import datetime
from .extensions import db

class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    writers = db.Column(db.String(255), nullable=True)  # e.g. "Benjamin Liles"
    album = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), nullable=False, default="Draft")  # Draft/Registered/Released
    notes = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Song {self.id} {self.title!r}>"