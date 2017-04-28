from handler import Handler

class BlogHandler(Handler):

    def get(self):
        self.render("blog.html")

