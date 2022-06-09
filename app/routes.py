from app import app, es, db
from flask import render_template, request
from app.models import Docs
from app.search import query_index, query_index_by_id, remove_from_index

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/get_id/<n>')
def get_id(n=None):
    result = Docs.query.filter(Docs.id==n).all()
    return render_template('id.html', result=result)

@app.route('/search/', methods=["GET"])
def get_posts():
    text = request.args["text"]
    if text is None:
        pass
    ids = query_index('posts', text)
    result = Docs.query.filter(Docs.id.in_(ids)).order_by(Docs.created_date.desc()).all()
    return render_template('search.html', result=result)

@app.route('/delete/')
def delete_post():
    id = request.args["id"]
    if query_index_by_id('posts', id) is not None:
        elastic = es.delete(index='posts', id=id)
        sqlite = Docs.query.filter(Docs.id==id).delete()
        db.session.commit()
        return render_template('delete.html', elastic=elastic, sqlite=sqlite)
    return render_template('error.html')

