from handler import Handler
from google.appengine.ext import db


class BlogPost(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class BlogPostHandler(Handler):
    def render_front(self, subject="", content="", error=""):
        self.render("postform.html", subject=subject, content=content, error=error)

    def get(self):
        self.render_front()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            a = BlogPost(subject=subject, content=content)
            o_id = a.put()
            o_id = a.key().id()
            self.redirect("/blog/" + str(o_id))
        else:
            error = "We need both subject and content"
            self.render_front(subject=subject, content=content, error=error)



