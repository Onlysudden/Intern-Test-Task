from app import app, loop
from flask import request
from app.models import Docs
from app.tasks import search, delete

@app.get('/search/')
def get_posts():
    text = request.args["text"]
    result = loop.run_until_complete(search(Docs, text))
    #result = search(Docs, text)
    return result

@app.delete('/delete/')
def delete_post():
    id = request.args["id"]
    result = loop.run_until_complete(delete(Docs, id))
    #result = delete(Docs, id)
    return {'result': result}

