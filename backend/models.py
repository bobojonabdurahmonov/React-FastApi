from peewee import *

db = SqliteDatabase("blogs.db")

class Blogs(Model):
    title = CharField(max_length=255)
    description = TextField()

    class Meta:
        database = db

db.connect()

db.create_tables([Blogs])
    

Blogs(title="Tramp is helping to Russia", description="Tramp is helping to Russ Tramp is helping to Russ Tramp is helping to Russ Tramp is helping to Russ Tramp is helping to Russ").save()