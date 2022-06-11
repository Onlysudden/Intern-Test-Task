from app import app, es, db
from flask import render_template, request
from app.models import Docs
from app.search import query_index, query_index_by_id

@app.get('/search/')
def get_posts():
    text = request.args["text"]
    if text is None:
        return "Text is None"
    ids = query_index('docs', text)
    result = Docs.query.filter(Docs.id.in_(ids)).order_by(Docs.created_date.desc()).all()
    return {"result": [post.as_dict() for post in result]}

@app.delete('/delete/')
def delete_post():
    id = request.args["id"]
    if query_index_by_id('docs', id) is not None:
        elastic = es.delete(index='docs', id=id)
        sqlite = Docs.query.filter(Docs.id==id).delete()
        db.session.commit()
        return {'result':{'sqlite':str(sqlite),'elastic':str(elastic)}}
    return render_template('error.html')

