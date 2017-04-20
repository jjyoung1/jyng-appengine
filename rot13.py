import os
import jinja2
import webapp2

from handler import Handler

class Rot13Handler(Handler):

    def get(self):
        self.render("rot13.html")

