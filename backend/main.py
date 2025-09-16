from fastapi import FastAPI
from models import Blogs

app = FastAPI()

@app.get("/api/")
async def homepage():
    return {"Status": "success"}

@app.get("/api/blogs/")
async def get_blogs():
    bloglar = Blogs.select()
    return {
        "allblogs": [{
            "id": blog.id, 
            "title": blog.title,
            "description": blog.description
        } for blog in bloglar]
    }

@app.get("/api/blogs/add/{title}/{desc}")
async def blog_add(title: str, desc: str):
    Blogs.create(title=title, description=desc)
    return {"Status": "Blog added"}

@app.get("/api/blogs/delete/{title}")
async def blog_del(title: str):
    deleted = Blogs.delete().where(Blogs.title == title).execute()
    if deleted:
        return {"Status": "Deleted"}
    else:
        return {"Status": "Not found"}

@app.get("/api/blogs/edit/{id}/{title}/{desc}")
async def blog_update(id: int, title: str, desc: str):
    blog = Blogs.get_or_none(Blogs.id == id)
    if blog:
        blog.title = title
        blog.description = desc
        blog.save()
        return {"Status": "Updated"}
    return {"Status": "Not found"}
