from sqlalchemy.testing import db


class ToDo(db.Model):
    id = db.Colomn(db.integer, primary_key=True)
    title = db.Colomn(db.String(255))
    complete = db.Colomn(db.Boolean)
