from app import app
from flask import render_template
from app.models import Docs

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/get_id/<id>')
def get_id(id=None):
    result = Docs.query.filter_by(id=id).first_or_404()
    return render_template('id.html', result=result)
