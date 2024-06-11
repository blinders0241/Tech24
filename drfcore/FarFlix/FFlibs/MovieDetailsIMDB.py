import sys
from imdb import IMDb,IMDbDataAccessError
import pandas as pd
pd.set_option('display.width',1200)
pd.set_option('display.max_columns',15)
pd.set_option('display.max_rows',30)
from django.conf import settings
from datetime import datetime
now = datetime.now() 
from requests.exceptions import Timeout


class MovieDetailsIMDB:
    def __init__(self):
        pass 
    def get_movie_details(self, Movie_IMDBCODE):
        movie_details = []
        movie_code = Movie_IMDBCODE
        ia = IMDb()
        def getTitle(movie):
            try:
                title = movie.get('title')
                return title
            except Exception as e:
                print(f"Error for {movie} > {e}")
                title="Nothing from IMDB"
                return title
        def getYear(movie):
            try:
                year = movie.get('year')
                return year
            except Exception as e:
                print(f"Error for {movie} > {e}")
                year="Nothing from IMDB"
                return year
        def getGenre(movie):
            try:
                genres = ", ".join(movie.get('genres'))
                return genres
            except Exception as e:
                print(f"Error for {movie} > {e}")
                genres="Nothing from IMDB"
                return genres
        def getDirectors(movie):
            try:
                directors = ", ".join([person['name'] for person in movie.get('directors')])
                return directors
            except Exception as e:
                print(f"Error for {movie} > {e}")
                directors="Nothing from IMDB"
                return directors
        def getWriters(movie):
            try:
                writers = ", ".join([person['name'] for person in movie.get('writers')])
                return writers
            except Exception as e:
                print(f"Error for {movie} > {e}")
                writers="Nothing from IMDB"
                return writers
        def getWriters(movie):
            try:
                writers = ", ".join([person['name'] for person in movie.get('writers')])
                return writers
            except Exception as e:
                # print(f"Error for {movie} > {e}")
                writers="Nothing from IMDB"
                return writers
        def getCast(movie):
            try:
                cast = ", ".join([person['name'] for person in movie.get('cast')[:10]]) 
                return cast
            except Exception as e:
                print(f"Error for {movie} > {e}")
                cast="Nothing from IMDB"
                return cast
        def getPlot(movie):
            try:
                plot = movie.get('plot outline')
                return plot
            except ia._exceptions.IMDbDataAccessError as e:
                # print(f"An error occurred: {e}")
                plot="Nothing from IMDB"
                return plot
        def getRunTIme(movie):
            try:
                runtime = movie.get('runtime')
                return runtime
            except Exception as e:
                print(f"Error for {movie} > {e}")
                runtime="Nothing from IMDB"
                return runtime
        def getCountry(movie):
            try:
                country = ", ".join(movie.get('countries'))
                return country
            except Exception as e:
                print(f"Error for {movie} > {e}")
                country="Nothing from IMDB"
                return country
        def getLanguage(movie):
            try:
                language = ", ".join(movie.get('languages'))
                return language
            except Exception as e:
                print(f"Error for {movie} > {e}")
                language="Nothing from IMDB"
                return language
        def getAwards(movie):
            try:
                awards = movie.get('awards')
                return awards
            except Exception as e:
                print(f"Error for {movie} > {e}")
                awards="Nothing from IMDB"
                return awards
        def getRatings(movie):
            try:
                rating = movie.get('rating')
                return rating
            except Exception as e:
                print(f"Error for {movie} > {e}")
                rating="Nothing from IMDB"
                return rating

        retries = 3
        while retries > 0:
            # print("Trying time",retries)
            try:
                movie = ia.get_movie(movie_code)
                if movie:
                    title = getTitle(movie)
                    year = getYear(movie)
                    genres = getGenre(movie)
                    directors = getDirectors(movie)
                    writers = getWriters(movie)
                    cast = getCast(movie)  # Get only the first 10 cast members
                    plot = getPlot(movie)
                    runtime = getRunTIme(movie)
                    country = getCountry(movie)
                    language = getLanguage(movie)
                    awards = getAwards(movie)
                    rating = getRatings(movie)
                    movie_details.append([title, year, genres, directors, writers, cast, plot, runtime, country, language, awards, rating, movie_code])
                    df = pd.DataFrame(movie_details, columns=["Title", "Year", "Genres", "Directors", "Writers", "Cast", "Plot", "Runtime", "Country", "Language", "Awards", "Rating","MovieCode"])
                    # print (df)
                    return df
            except Exception as e:
                print(e)
                retries = retries-1
                continue
            # Convert the list to a pandas DataFrame

# MovieDetailsIMDB().get_movie_details("0075669")