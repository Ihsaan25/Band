from django.db import models

# Create your models here.
class Song(models.Model):
    song_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.song_text

class Choice(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.song_name
    
