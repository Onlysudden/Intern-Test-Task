from app import es

def add_to_index(index, model):
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    es.index(index=index, id=model.id, body=payload)

def remove_from_index(index, model):
    es.delete(index=index, id=model.id)

def query_index(index, text):
    search = es.search(
        index=index,
        size=20,
        query = {'multi_match': {'query': text, 'fields': ['*']}})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids

def query_index_by_id(index, id):
    result = es.search(index=index, body={
        "size": 1,
        "query": {
            "match": {
                'id': id
            }
        }
    })["hits"]["hits"]
    return result



# from app import app
# from app.models import Docs
# from app.search import add_to_index, remove_from_index, query_index
# for post in Docs.query.all():\ 
#     add_to_index('posts', post)

# query_index('posts', 'one two three four five')