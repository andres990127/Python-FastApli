from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } ,
    {
        'id': 2,
        'title': 'Avatar2',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get('/', tags = ['home'])
def message():
    return HTMLResponse('<h1>Hello World</h2>')

@app.get('/movies', tags = ['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags = ['movies'])
def get_movie(id: int):
    movie = list(filter(lambda x: x['id'] == id, movies))
    return movie if len(movie) > 0 else "No hay nada que ver"