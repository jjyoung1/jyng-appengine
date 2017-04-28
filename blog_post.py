from handler import Handler

class BlogPostHandler(Handler):
    def get(self):
        self.render("post.html")

    def post(self):
        pass