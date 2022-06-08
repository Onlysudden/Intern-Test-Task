from app import app
from flask import render_template, request
from app.models import Docs
from app.search import query_index

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/get_id/<n>')
def get_id(n=None):
    result = Docs.query.filter(Docs.id>n).limit(20).all()
    return render_template('id.html', result=result)

@app.route('/test/', methods=["GET"])
def get_posts():
    text = request.args["text"]
    ids = query_index('posts', text)
    result = []
    for id in ids:
       result.append(Docs.query.filter(Docs.id==id).all())
    return render_template('idtest2.html', result=result)

