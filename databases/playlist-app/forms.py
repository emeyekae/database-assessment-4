"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    # Add the necessary code to use this form
    name = StringField(
        "Playlist Name", validators=[InputRequired(message="Playlist Name cannot be blank")]
    )
    description = StringField(
        "Playlist Description", validators=[InputRequired(message="Playlist Description cannot be blank")]
    )


class SongForm(FlaskForm):
    """Form for adding songs."""
    # Add the necessary code to use this form
    title = StringField(
        "Song Title",
        validators=[InputRequired(message="Song Title cannot be blank")]
    )
    artist = StringField(
        "Song Artist",
        validators=[InputRequired(message="Song Aritist cannot be blank")]
    )


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
