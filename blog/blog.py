from google.appengine.ext import db

from handler import Handler
from blog_post import BlogPost

class BlogHandler(Handler):

    def get(self):
        posts = db.GqlQuery("SELECT * FROM BlogPost "
                                 "ORDER BY created DESC")
        self.render("blog.html", posts=posts)

class PostHandler(Handler):
    def get(self, o_id):
        key = db.Key.from_path("BlogPost", int(o_id))
        post = db.get(key)
        if not post:
            self.error(404)
            return
        else:
            self.render("post.html", post=post)