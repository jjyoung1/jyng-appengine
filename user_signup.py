import re

from handler import Handler


class UserSignupHandler(Handler):
    def get(self):
        self.render('user_signup.html')

    # TODO: Cleanup context passing to template
    def post(self):
        # get posted parameters
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        # Initialize context for response
        # We don't want the password fields repopulated in case of error
        ctx = dict(username=username,
                   email=email)

        # Initialize verification error status to false
        error = False

        # If invalid username setup error and message
        if not _valid_user(username):
            ctx['username_error'] = 'Invalid Username'
            error = True

        if not _valid_password(password):
            ctx['password_error'] = 'Invalid Password'
            error = True

        if not _valid_password(verify) or password != verify:
            ctx['verify_error'] = "Passwords don't match"
            error = True

        # Check if all inputs are valid
        if not error:
            url = '/welcome?username=' + username
            self.redirect(url)

        else:
            # set error response code
            self.response.status_int = 400
            self.render('user_signup.html', **ctx)


#
# Utility functions used for parameter verification
#
USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")


def _valid_user(username):
    return username and USER_RE.match(username)


PASSWORD_RE = re.compile("^.{3,20}$")


def _valid_password(password):
    return password and PASSWORD_RE.match(password)


EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")


def _valid_email(self, email):
    return not email or EMAIL_RE.match(email)


class WelcomeHandler(Handler):
    def get(self):
        username = self.request.get("username")
        self.render('welcome.html', username=username)
