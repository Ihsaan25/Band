from django.db import models

# Create your models here.
class Song(models.Model):
    """
    Represents a song in the music library.

    :ivar str song_text: The title or text of the song.
    :ivar datetime pub_date: The date and time when the song was published.
    """
    song_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns the string representation of the Song object.

        :returns: The title or text of the song.
        :rtype: str
        """
        return self.song_text

class Choice(models.Model):
    """
    Represents a choice for a song in the music library.

    :ivar Song song: The song to which this choice belongs.
    :ivar str song_name: The name of the song.
    :ivar int votes: The number of votes received for this choice.
    """
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns the string representation of the Choice object.

        :returns: The name of the song.
        :rtype: str
        """
        return self.song_name
    
