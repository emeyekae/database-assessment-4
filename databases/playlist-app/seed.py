"""Seed file to make sample data for pets db."""

from models import Song,Playlist,PlaylistSong, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

#Playlists
# If table isn't empty, empty it
Playlist.query.delete()

# Add playlists
pl1 = Playlist(name='Jazz', description="Jazzy Music")
pl2 =Playlist(name='Motown', description="Motown Music")
pl3 =Playlist(name='Soul', description="Soul Music")
pl4 =Playlist(name='Soft Rock', description="Mellow Rock and Roll Music")
pl5 =Playlist(name='Hard Rock', description="Hard Rock and Roll Music")

# Add new objects to session, so they'll persist
db.session.add(pl1)
db.session.add(pl2)
db.session.add(pl3)
db.session.add(pl4)
db.session.add(pl5)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Songs
# If table isn't empty, empty it
Song.query.delete()

# Add songs
s1 =Song(title='Let it be', artist="Beatles")
s2 =Song(title='My Favorite Things', artist="John Coltrane")
s3 =Song(title='Take Five', artist="Dave Brubeck")
s4 =Song(title='Heard It Through the Grapevine', artist="Marvin Gaye")
s5 =Song(title='What Becomes of the Brokenhearted?', artist="Jimmy Ruffin")
s6 =Song(title="Let’s Stay Together", artist="Al Green")
s7 =Song(title='Respect', artist="Aretha Franklin")
s8 =Song(title='Peaceful Easy Feeling', artist="Eagles")
s9 =Song(title='Basket Case', artist="Green Day")
s10=Song(title='London Calling', artist="The Clash")

# Add new objects to session, so they'll persist
db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(s4)
db.session.add(s5)
db.session.add(s6)
db.session.add(s7)
db.session.add(s8)
db.session.add(s9)
db.session.add(s10)

# Commit--otherwise, this never gets saved!
db.session.commit()

#playlist_songs
# If table isn't empty, empty it
PlaylistSong.query.delete()

# Add Playlists/Songs combinations 
c1 =PlaylistSong(playlist_id=1, song_id=2)
c2 =PlaylistSong(playlist_id=2, song_id=5)
c3 =PlaylistSong(playlist_id=3, song_id=6)
c4 =PlaylistSong(playlist_id=4, song_id=1)
c5 =PlaylistSong(playlist_id=5, song_id=9)

# Add new objects to session, so they'll persist
db.session.add(c1)
db.session.add(c2)
db.session.add(c3)
db.session.add(c4)
db.session.add(c5)


# Commit--otherwise, this never gets saved!
db.session.commit()