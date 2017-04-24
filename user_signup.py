from handler import Handler


class UserSignupHandler(Handler):
    def _init_ctx(self):
        ctx = {"username": "","password": "","verify": ""}
        return ctx

    def get(self):
        ctx = self._init_ctx();
        self.render('user_signup.html', ctx=ctx)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        self.render('user_signup.html', ctx={"username": username,
                                             "password": password,
                                             "verify": verify})
