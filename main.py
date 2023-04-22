from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] | None = None
    title: str
    overview: str
    year: int
    rating: float
    category: str


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

@app.get('/movies/', tags = ['movies'])
def get_movies_by_category(category: str):
    res = list(filter(lambda x: x['category'] == category, movies))
    return res if len(res) > 0 else "No hay nada que ver"

@app.post('/movies', tags = ['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    for index, item in enumerate(movies):
        if item["id"] == id:
            movies[index].update(movie)
            movies[index]["id"] = id
            return movies[index]

@app.delete('/movies/{id}', tags = ['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
    return movies