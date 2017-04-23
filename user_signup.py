import webapp2
import string
import jinja2
from handler import Handler


class UserSignup(Handler):
    def __init__(self):
        self.ctx = {"username": "","password": "","verify": ""}

    def get(self):
        self.render('user_signup.html', ctx=ctx)

    def post(self):
        self.ctx.username = self.request.get("username")
        self.ctx.password = self.request.get("password")
        self.ctx.verify = self.request.get("verify")
        self.render('user_signup.html', ctx=self.ctx)
