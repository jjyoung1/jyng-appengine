from handler import Handler


class UserSignupHandler(Handler):

    def get(self):
        self.render('user_signup.html')

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        self.render('user_signup.html',
                    username=username,
                    password=password,
                    verify=verify)
