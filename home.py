from handler import Handler

class HomeHandler(Handler):

    def get(self):
        self.render("index.html")

