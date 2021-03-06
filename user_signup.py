import re
import random
import string
import hmac

from handler import Handler

secret = "NUIOPlkkjO*-{n-98BUiopb56&*)(b;olBy79i8b"

def make_salt():
    return ''.join(random.choice(string.letters) for x in range(0, 5))


# Implement the function valid_pw() that returns True if a user's password
# matches its hash. You will need to modify make_pw_hash.

def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())


def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return 1

class UserSignupHandler(Handler):
    def get(self):
        self.render('user_signup.html')

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
            url = '/blog/welcome'
            salt = make_salt()
            c = make_secure_val(username)

            self.response.headers.add_header('set-cookie', str('user=%s; Path=/' % c))
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
        username = self.request.cookies.get("user")
        (username, c) = username.split('|')
        self.render('welcome.html', username=username)


if __name__ == '__main__':
    salt = make_salt()
    print(salt)
    c = make_secure_val('joel')
    print(c)
    print("User cookie is " + str(check_secure_val(c)))


class UserLogoutHandler(Handler):
    def _logout(self):
        self.response.delete_cookie('user', path='/')
        self.redirect('/blog/signup')

    def get(self):
        self._logout()

    def post(self):
        self._logout()
