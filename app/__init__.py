from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from elasticsearch import Elasticsearch
import asyncio

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
es = Elasticsearch('http://elasticsearch:9200')
#es = Elasticsearch('http://localhost:9200')
loop = asyncio.new_event_loop()

from app import routes, models

#Coздание индекса
from app.models import Docs
from app.elastic import add_to_index

for post in Docs.query.all():
    add_to_index('docs', post)