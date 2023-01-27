from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Aplicacion de Prueba"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    }, 
    {
        'id': 2,
        'title': 'Avata',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2001',
        'rating': 7.8,
        'category': 'suspenso'    
    } 
]

@app.get("/")
def message():
    return HTMLResponse('<h1> Hello world </h1>')

# todas las peliculas
@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

# Filtrado de peliculas por id
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id:int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

# filtrado de peliculas por categoria
@app.get('/movies/', tags=['movies'])
def get_movie_by_Category(category: str, year:int):
   return [item 
   for item in movies 
        if (item['category']==category and int(item['year'])==year)]
        
    