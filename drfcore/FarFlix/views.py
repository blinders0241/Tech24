from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas as pd
import json,os
from FarFlix.models import FarFlixMoviesModel,FFMovieDetailsModel
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from FarFlix.FFlibs.DbConnections import DbConnections
from FarFlix.FFlibs.MovieDetailsIMDB import *
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from FarFlix.FFlibs.Youtube import youtube_downloader
# Create your views here.


def FarFlixhome(request):
    msg = "HELL"
    return JsonResponse({"result": msg})
@csrf_exempt
def FarFlixUpload(request):
    if request.method == 'POST' and request.FILES.get('csvFile'):
        
        uploaded_file = request.FILES['csvFile']
        df = pd.read_csv(uploaded_file)
        # print("Recived Dataframe goes like this \n",df.tail())
        for index, row in df.iterrows():
            if row['movieName_Disk'] == '':
                continue
            try:        # hdr = ['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'OPEN_INT', 'CHG_IN_OI', 'TIMESTAMP']
                obj = FarFlixMoviesModel.objects.create(
                FilePath= row['File Path'],
                movieName_Disk = row['movieName_Disk'],
                FileSize = row['Size (GB)'],
                FileType = row['File Type'],
                movieCode_IMDB = row['movieCode_IMDB'],
                Title_IMDB = row['Title_IMDB'],
                Year_IMDB = row['Year_IMDB'],
                Genres_IMDB = row['Genres_IMDB'],
                Classified = row['Classified'],
                )
                obj.save()
            except IntegrityError as e:
                print("Error occurred while saving row to db", row['Issue key'], e)

        response = {"result": "Saved to DB"}
        return JsonResponse(response)
    else:
        response = {'error': 'Invalid request'}
        return JsonResponse(response, status=400)

@csrf_exempt
def FFMovieDetailsUpload(request):
    if request.method == 'POST' and request.FILES.get('csvFile'):
        uploaded_file = request.FILES['csvFile']
        df = pd.read_csv(uploaded_file)
        # print("Received Dataframe goes like this \n",df.tail())
        
        # Initialize an empty list to store duplicates
        duplicates = []

        for index, row in df.iterrows():
            if row['Title'] == '':
                continue
            try:
                # Check if a movie with the same MovieCode already exists
                if not FFMovieDetailsModel.objects.filter(MovieCode_IMDB=row['MovieCode']).exists():
                    obj = FFMovieDetailsModel.objects.create(
                        Title_IMDB= row['Title'],
                        Year_IMDB = row['Year'],
                        Genres_IMDB = row['Genres'],
                        Directors_IMDB = row['Directors'],
                        Writers_IMDB = row['Writers'],
                        Cast_IMDB = row['Cast'],
                        Plot_IMDB = row['Plot'],
                        Runtime_IMDB = row['Runtime'],
                        Country_IMDB = row['Country'],
                        Language_IMDB = row['Language'],
                        Awards_IMDB = row['Awards'],
                        Rating_IMDB = row['Rating'],
                        MovieCode_IMDB = row['MovieCode'],
                    )
                    obj.save()
                else:
                    # If a duplicate is found, add it to the duplicates list
                    duplicates.append(row['MovieCode'])
            except IntegrityError as e:
                print("Error occurred while saving row to db", row['Title'], e)

        # Write the duplicates to a text file
        with open(os.path.join(settings.BASE_DIR, 'duplicates.txt'), 'w') as f:
            for movie_code in duplicates:
                f.write(f'{movie_code}\n')

        response = {"result": "Saved to DB"}
        return JsonResponse(response)
    else:
        response = {'error': 'Invalid request'}
        return JsonResponse(response, status=400)
 
    
def FarFlixIMDBDetails(request):
    con = DbConnections().connectToDB()
    # df = pd.read_sql_query("SELECT * FROM FarFlix_farflixmoviesmodel", con)
    df = pd.read_sql_query("SELECT * FROM FarFlix_ffmoviedetailsmodel", con)
    df_sorted = df.sort_values(by='id', ascending=False)
    data = json.loads(df.to_json(orient='records'))
    return JsonResponse(data, safe=False)

def FarFlixFileDetails(request):
    movieCode = request.GET.get('param1', '')
    print("# == Params received ============================================")
    print(f"params1: {movieCode}")
    con = DbConnections().connectToDB()
    df = pd.read_sql_query(f"SELECT * FROM FarFlix_farflixmoviesmodel WHERE movieCode_IMDB = '{movieCode}'", con)
    # print(df.head())
    data = json.loads(df.to_json(orient='records'))
    return JsonResponse(data, safe=False)

@csrf_exempt
def FF_FetchDetailsFromDB(request):
    con = DbConnections().connectToDB()
    df = pd.read_sql_query("SELECT * FROM FarFlix_farflixmoviesmodel ORDER BY id DESC LIMIT 61;", con)
    df_sorted = df.sort_values(by='id', ascending=False)
    data = json.loads(df_sorted.to_json(orient='split',index=False))
    return JsonResponse(data, safe=False)


@csrf_exempt
def FF_FetchEditDetailsTODB(request):
        """
        Movie Details Update
        Step1 : Receive the details to be updated alongside ID from table FarFlix_farflixmoviesmodel
        Step2 : Fetch the ID of FarFlix_ffmoviedetailsmodel first before updating the tables
        step3 : Fetch the details from IMDB to be updated in FarFlix_ffmoviedetailsmodel
        step4 : Update both the tables accordingly:
            table 1 : update from the fields from the page
            table FarFlix_ffmoviedetailsmodel : update from IMDB 
        
        """
        if request.method == 'POST':
            try:
                #Received Data
                data = json.loads(request.body)
                
                movie = FarFlixMoviesModel.objects.get(id=data['id'])
                con = DbConnections().connectToDB()
                cur = con.cursor()
                
                ID = movie.id
                received_movieCode_IMDB = data['movieCode_IMDB']
                print("####")
                print(movie.movieCode_IMDB)
                # received_Title_IMDB = data['Title_IMDB']
                # received_Year_IMDB = data['Year_IMDB']
                cur.execute("SELECT id \
                            FROM FarFlix_ffmoviedetailsmodel \
                            WHERE CAST(movieCode_IMDB AS INTEGER) IN (\
                                SELECT CAST(movieCode_IMDB AS INTEGER) \
                                FROM FarFlix_farflixmoviesmodel \
                                WHERE ID = '%s')" % ID)
                movideDetailsID = cur.fetchone()
                id_FarFlix_ffmoviedetails = movideDetailsID[0]
                print("ID to update in FarFlix_ffmoviedetailsmodel Table",id_FarFlix_ffmoviedetails )
                print("Data received from the Page/Form",data)
                #Fetch the details from IMDB Site 
                dataframefromIMDB = MovieDetailsIMDB().get_movie_details(received_movieCode_IMDB)
                movie.movieCode_IMDB = data.get('movieCode_IMDB', movie.movieCode_IMDB)
                movie.Year_IMDB = data.get('Year_IMDB', movie.Year_IMDB)
                movie.Title_IMDB = data.get('Title_IMDB', movie.Title_IMDB)
                movie.save()
                row = dataframefromIMDB.iloc[0]  # Get the first row of the dataframe
                # Prepare the SQL UPDATE statement
                sql = """
                UPDATE FarFlix_ffmoviedetailsmodel
                SET Title_IMDB = ?, Year_IMDB = ?, Genres_IMDB = ?, Directors_IMDB = ?, Writers_IMDB = ?, Cast_IMDB = ?, Plot_IMDB = ?, Runtime_IMDB = ?, Country_IMDB = ?, Language_IMDB = ?, Awards_IMDB = ?, Rating_IMDB = ?, MovieCode_IMDB = ?
                WHERE id = ?
                """
                # If Runtime is a list of a single value
                row['Runtime'] = row['Runtime'][0] if isinstance(row['Runtime'], list) and len(row['Runtime']) > 0 else row['Runtime']
                # If Awards is None, replace it with an empty string or some default value
                row['Awards'] = row['Awards'] if row['Awards'] is not None else ''
                # Prepare the data
                data = (row['Title'], movie.Year_IMDB, row['Genres'], row['Directors'], row['Writers'], row['Cast'], row['Plot'], row['Runtime'], row['Country'], row['Language'], row['Awards'], row['Rating'], row['MovieCode'], id_FarFlix_ffmoviedetails)

                # Execute the SQL statement
                cur.execute(sql, data)
                con.commit()
                
                return JsonResponse({'message': 'Movie updated successfully'}, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Movie not found'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def FF_DeleteMoviebyID(request):
    lst_deletedMovieID= []
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ID = (data['id'])
            movie = FarFlixMoviesModel.objects.get(id=ID)
            movie.delete()
            
            return JsonResponse({'message': 'Movie deleted with ID :'+str(ID)}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Movie not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def FF_Youtube(request):
    YoutubeUrl = request.GET.get('videoId', '')
    print("# == Params received ============================================")
    print(f"params1: {YoutubeUrl}")
    # links = youtube_downloader.input_links(YoutubeUrl)
    YoutubeUrl = YoutubeUrl.split('\n')
    print(type(YoutubeUrl))
    links = YoutubeUrl.pop()
    print(links)

    try:
        youtube_downloader.merge_Audio_Video(links)
        print("Download finished!")

    except Exception as e:
        print("Error occurred while downloading the video", e)
        return JsonResponse({"error": "Error occurred while downloading the video"}, status=500)

    response = {"result": "Saved to DB"}
    return JsonResponse(response)
    # return JsonResponse({"result": YoutubeUrl}, safe=False)

    