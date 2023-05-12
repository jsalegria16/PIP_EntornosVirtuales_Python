import store

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/') # Respond some text, a list in this case
def get_list():
    return [1,2,3,4,5,65,67,8,9]

@app.get('/contact',response_class=HTMLResponse) # Respond with HTML
def get_list():
    return """
    <h1> Hello, this is from your own server </h1>
    <img src="https://www.w3schools.com/images/img_bootcamp_gold_160.png" alt="Italian Trulli">
    """


def run():
    store.GetCategories()
    

if __name__ == '__main__':
    run()