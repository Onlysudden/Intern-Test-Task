from cgitb import text
from app import db
from datetime import datetime

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.Text())
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Docs {}>'.format(self.rubrics)
