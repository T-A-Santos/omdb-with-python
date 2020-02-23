import requests as req


API_KEY = 'Your_api_key_here'

def search_by_title(movie_title):
    url = "http://www.omdbapi.com/?apikey={}&t={}".format(API_KEY, movie_title)
    retorno = req.get(url).json()
    d = {}

    if retorno['Response'] == 'True':

        d['year'] = retorno['Year']
        d['title'] = retorno['Title']
        d['director'] = retorno['Director']
        d['genre'] = retorno['Genre']
        d['poster'] = retorno['Poster']
        d['actors'] = retorno['Actors']

        if retorno['Ratings'][0]['Value'] == "N/A":
            d['internet_movie_database'] = None

        else:
            d['internet_movie_database'] = retorno['Ratings'][0]['Value']
        
        if retorno['Ratings'][1]['Value'] == "N/A":
            d['rotte_tomatoes'] = None

        else:
            d['rotten_tomatoes'] = retorno['Ratings'][1]['Value']

        if retorno['Ratings'][2]['Value'] == "N/A":
            d['metacritic'] = None
        
        else:
            d['metacritic'] = retorno['Ratings'][2]['Value']

    return d
