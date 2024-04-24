from fastapi import FastAPI

# creating instace of fastapi
app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Taiyab Ansari'}}


@app.get('/about')
def about_page():
    return {'data': 'about page'}