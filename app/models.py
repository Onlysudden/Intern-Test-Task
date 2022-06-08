from cgitb import text
from unicodedata import name
from app import db
from datetime import datetime

class Docs(db.Model):
    __searchable__ = ['text']
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime)
    rubrics = db.Column(db.Text())

    def __repr__(self):
        return '<Docs {} {} {} {}>'.format(self.id, self.rubrics, self.text, self.created_date)
