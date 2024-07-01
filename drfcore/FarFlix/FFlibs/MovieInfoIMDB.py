# local imports
import sys
sys.path.append(r"C:\SIMPLY_Official\\2024\\TechHome241\drfcore\\FarFlix")
import random, string
from imdb import IMDb,IMDbDataAccessError
import pandas as pd
from FFlibs.DbConnections import DbConnections
from FFlibs.Globster import *
pd.set_option('display.width',1200)
pd.set_option('display.max_columns',15)
pd.set_option('display.max_rows',30)
from django.conf import settings
from datetime import datetime
now = datetime.now() 
import time
from requests.exceptions import Timeout

class MovieInfoIMDB:
    def __init__(self):
        pass 
    
    def randomword(self,length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def divide_list(self,lst, n):
        avg = len(lst) // n
        remainder = len(lst) % n
        sublists = [lst[i * avg + min(i, remainder):(i + 1) * avg + min(i + 1, remainder)] for i in range(n)]
        return sublists

    def getMovieCodesListfromDB(self):
        Lst_Movie_Codes = []
        con = DbConnections().connectToDB()
        df = pd.read_sql_query("SELECT * FROM FarFlix_farflixmoviesmodel where ID > 3656 ORDER BY ID DESC;", con)
        Lst_Movie_Codes = df['movieCode_IMDB'].to_list()
        sublists = MovieInfoIMDB().divide_list(Lst_Movie_Codes, 5)
        return sublists
    
    def getFileName(self,number):
        FileNametoWrite = "Bollywood_FullLIST"+ MovieInfoIMDB().randomword(10)+ "_" +number + ".csv"
        return FileNametoWrite
    
    def saveInfo2Disk(self,dataFrame):
        try:
            Num_df = dataFrame.Title.count()
        except Exception as e:
            print("Error",e)
        try:
            dataFrame.to_csv(Globster().SaveMovieDetailsIMDB + MovieInfoIMDB().getFileName(str(Num_df)), encoding='utf-8',index=False)
            print("######Success######")
            print("Written on ",Globster().SaveMovieDetailsIMDB + MovieInfoIMDB().getFileName(str(Num_df)))
            print("##################")
        except Exception as e:
            print("Writing UnSuccess",e)
        return dataFrame
    
    
    def get_movie_details(self, movie_codes):
        ia = IMDb()
        movie_details = []
        Counter = 1
        ErroList = []

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
        print(len(movie_codes)) 

        # print(len(movie_codes))    
        for movie_code in movie_codes:
            retries = 3
            while retries > 0:
                try:
                    # Get the movie object using the movie code
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
                        # Add the movie details to the list
                        print(f"Count: {Counter}, {title}, {year}")
                        Counter +=1
                        movie_details.append([title, year, genres, directors, writers, cast, plot, runtime, country, language, awards, rating, movie_code])
                    else:
                        ErroList.append(movie_code)
                    break  # Break the loop if the operation was successful
                except IMDbDataAccessError as e:
                    if 'timed out' in str(e):
                        retries -= 1
                        print(f"Timeout occurred for movie code {movie_code}. Retrying... ({retries} retries left)")
                        time.sleep(5)  # Wait for 5 seconds before retrying
                    else:
                        ErroList.append(movie_code)
                        print(e)
                        break  # Break the loop and continue with the next movie code
                except Exception as e:
                    ErroList.append(movie_code)
                    print(e)
                    break  # Break the loop and continue with the next movie code

            # Convert the list to a pandas DataFrame
            df = pd.DataFrame(movie_details, columns=["Title", "Year", "Genres", "Directors", "Writers", "Cast", "Plot", "Runtime", "Country", "Language", "Awards", "Rating","MovieCode"])

        # Write the duplicates to a text file
        with open(os.path.join(Globster().SaveMovieDetailsIMDB, 'Errors.txt'), 'w') as f:
            for movie_code in ErroList:
                f.write(f'{movie_code}\n')
        return df
    
    def build_uploadMovieDetailsIMDB(self):
        MoviewithSubList = MovieInfoIMDB().getMovieCodesListfromDB()
        TotalLength_Sublist = len(MoviewithSubList)
        print(TotalLength_Sublist)
        Counter = 0
        
        for MovieList in MoviewithSubList:
            print(Counter)
            try:
                dataFrame = MovieInfoIMDB().get_movie_details(MovieList)
                MovieInfoIMDB().saveInfo2Disk(dataFrame)
                Counter += 1
            except Exception as e:
                continue
    
    # def buildCSVIMDBdetailsFile(self):
    #     # movieCodesList = ['5918074','1832382','1372681','149568','12631660','177496','80322','178185','178186','106204','306434','90577','13468976','154108','178203','178204','2203308','2321163','1570417','215466','403935','1396208','9783778','4559006','1849718','831840','4387040','88687','418460','1252596','14091818','278291','10184','112313','94625','5784860','476729','6139732','115491','0066763','118931','289992','1255951','946999','5615116','14167338','301179','72860','118957','337971','13129104','1934231','3447364','8751976','1327035','47990','363563','234000','255112','845448','13510660','4088588','4354740','23333666','1047459','10644708','1833673','422091']
    #     # movieCodesList =['1833673','6027478','6380520','60310','328998','6071752','1815775','328729','273535','3723864','0896934','7881542','67183','11027830','7335176','6512784','2309987','3619772','4865436','5325684','6535880','1887763','369516','411469','11460818','242519','242519','1259573','1949548','3142232','806088','6588966','119295','154591','3177316','5461944','11163028','1980986','7721946','1573072','14167390','286705','80901','378072','2034011','3678938','326576','11816092','2622130','10393870','4047112','156641','300051','290685','130803','8983228','348843','449994','278522','1077248','2621000','7598180','104561','8108196','5456546','5456546','13449624','2330927','3758172','187193','357819','7838252','5460276','2962230','8576200','79386','10235600','7881550','3038772','294662','156691','5980232','0234054','173102','1727535','12834962','1664809','62177','114231','7550816','1744641','98168','95955','405508','1239276','2821880','4909752','86837','19315924','110366','10895556','1708532','1245732','896968','299108','155106','9470628','816627','2830606','1787439','1434447','202470','7102426','3410408','105271','2077833','8178634','6296236','5165344','152256','6836936','299375','8239946','6791730','318956','1639426','4434004','83248','2392447','8291224','11385128','442855','220832','10806040','5178278','1185412','2317337','84866','120456','11964084','215338','494290','5755092','5638474','287111','1084972','59893','290331','96415','7430722','7430722','3138602','315642','72582','13381376','4218572','86597','232960','833561','0093578','0369746','1111869','9390026','43307','12361178','274944','4172430','2321493','2798920','2560140','28246045','947798','4937942','92400','7657566','11691684','445883','4912910','2095605','6904272','3181822','1345836','11804152','21919896','116756','115568','211934','106333','346723','5946128','126871','238936','164538','118983','112870','101732','1285241','461936','3495026','172519','222024','151150','449999','347304','113526','0347473','137100','1188996','119861','1562871','1182937','3405236','114231','148706','114726','420332','385351','120540','115042','9006564','25403492','96922','871510','6381764','2180339','10162384','210945','145681','10016180','368008','1196141','8749198','790636','1772288','985025','2387433','2387433','1878942','2103281','99371','2101341','1311699','989757','1321509','1241317','2461218','832266','2377322','2375585','1073105','1314655','1645170','92890','63384','1840309','1853728','1853728','1770672','1211837','120655','2978462','4160708','2270788','483607','8110640','1255953','1375666','3481634','1628841','3062096','28623600','5962210','2226417','1591095','2106361','758758','2180411','1634121','1634121','1634121','1634121','1057500','7779510','0057193','790724','1205537','1351685','3393786','3868150','20618056','143145','120347','10839808','381061','3582020','1131734','3289712','3289712','3289712','3289712','116695','3110960','1210166','8090564','2969522','5834426','1748122','1126618','3740778','1485749','1935179','408306','408306','1464763','100212','2024521','363771','642334','1821549','4438848','2495778','3531824','3531824','1023111','4790268','151738','12907294','2872718','2382320','1959490','2024469','1837613','125439','3110958','1670345','13345606','6472976','11871074','10366206','16900880','15255288','8649252','6794504','804516','1663662','14563970','21979910','446013','3733778','338337','1716777','6834034','409182','2397535','822847','473075','1196339','1392214','1446714','110912','465580','2691734','132477','2388715','151804','1238298','479968','1922679','5458448','1206543','6679794','3491962','758771','88461','1623205','1904996','1355644','995868','2788732','1981677','102685','3717490','1438534','830515','1082868','10594864','350028','462499','2231461','2304953','12848468','2873282','485985','2275946','253556','4154916','462504','105236','1753496','995863','8965324','1396523','365686','9470628','1034331','1446192','1318514','2386285','257044','215129','2929652','71042','3748528','6000478','2401842','2199571','1742334','1599348','1656190','2126355','2582576','5851014','2396438','120815','120070','2179936','7668870','111104','3501112','1214962','2140379','1247690','379786','114369','2301147','1956620','138097','9376612','365748','815236','15483276','1515091','13860098','1386691','1773764','1038915','822854','4633690','6494418','3397884','2053463','13698928','458481','3544112','1252289','7312940','8269322','15501376','22606046','1571243','882977','3774114','7660350','2062700','1537481','6449354','1656192','111257','2537176','1186370','1517489','1185266','2567712','473705','441796','2080374','1656186','1772264','420223','878804','1131729','1935902','42281','1911644','1790886','2517658','2326612','16476272','1366365','3065204','1457767','1457767','10323676','245844','1093357','319262','407887','458352','1825157','9382310','1863203','1650535','961728','10521092','2039393','1139328','847167','435651','279113','2034800','2980592','492044','408839','2404463']
    #     # movieCodesList = ['101284','0066763','0896934','0234054','0093578','0369746','0347473','0057193']
    #     dataFrame = MovieInfoIMDB().get_movie_details(movieCodesList)
    #     MovieInfoIMDB().saveInfo2Disk(dataFrame)
    #     print("Success")
        
# MovieInfoIMDB().get_movie_details([5956100,4434004,2178470])
#we were runningthis
# MovieInfoIMDB().build_uploadMovieDetailsIMDB()
# MovieInfoIMDB().buildCSVIMDBdetailsFile()