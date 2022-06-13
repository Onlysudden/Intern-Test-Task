from app import db
from app.elastic import delete_by_id, query_index_by_text, query_index_by_id

async def search(Model, text):
    if text is None:
        return "Text is None"
    try:
        ids = query_index_by_text('docs', text)
        result = Model.query.filter(Model.id.in_(ids)).order_by(Model.created_date.desc()).all()
        return {"result": [post.as_dict() for post in result]}
    except Exception as exc:
        return str(exc)

async def delete(Model, id):
    delete_item = query_index_by_id('docs', id)
    if delete_item is not None:
        elastic_result = delete_by_id('docs', id)
        if elastic_result is True:
            db_result = bool(Model.query.filter(Model.id==id).delete())
            db.session.commit()
            return db_result
        return elastic_result
    return False