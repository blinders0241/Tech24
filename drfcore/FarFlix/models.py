from django.db import models
from django.utils import timezone
from django.forms.fields import FloatField as FloatFormField
# Create your models here.


class FarFlixMoviesModel(models.Model):
    FilePath = models.CharField(max_length=220,default=None)
    movieName_Disk = models.CharField(max_length=220,default=None)
    FileSize = models.FloatField(default=0.0)
    FileType = models.CharField(max_length=20,default=None)
    movieCode_IMDB = models.CharField(max_length=30,default=None)
    Title_IMDB = models.CharField(max_length=190,default=None)
    Year_IMDB = models.CharField(max_length=30,default=None)
    Genres_IMDB = models.CharField(max_length=130,default=None)
    Classified = models.CharField(max_length=100,default=None)
    def __str__(self) -> str:
        return self.Title_IMDB + ' | '+ str(self.Year_IMDB)
    

class FFMovieDetailsModel(models.Model):
    Title_IMDB = models.CharField(max_length=190,default=None)
    Year_IMDB = models.CharField(max_length=30,default=None)
    Genres_IMDB = models.CharField(max_length=130,default=None)
    Directors_IMDB = models.CharField(max_length=130,default=None)
    Writers_IMDB = models.CharField(max_length=230,default=None)
    Cast_IMDB = models.CharField(max_length=330,default=None)
    Plot_IMDB = models.CharField(max_length=2030,default=None)
    Runtime_IMDB = models.CharField(max_length=130,default=None)
    Country_IMDB = models.CharField(max_length=130,default=None)
    Language_IMDB = models.CharField(max_length=130,default=None)
    Awards_IMDB = models.CharField(max_length=130,default=None)
    Rating_IMDB = models.CharField(max_length=30,default=None)
    MovieCode_IMDB = models.CharField(max_length=30,default=None)
    Watched = models.CharField(max_length=30,default="N")
    def __str__(self) -> str:
        return self.Title_IMDB + ' | '+ str(self.Year_IMDB)+ ' | '+ str(self.Language_IMDB)