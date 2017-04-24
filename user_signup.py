import re

from handler import Handler

class UserSignupHandler(Handler):
    USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
    PASSWORD_RE = re.compile("^.{3,20}$")
    EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")

    def get(self):
        self.render('user_signup.html')

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        valid_username = self._validate_user(username)
        valid_password = self._validate_password(password)
        valid_verify = self._validate_verify(password, verify)
        valid_email = self._validate_email(email)

        # Check if all inputs are valid
        if (valid_username and valid_password and valid_verify and valid_email):
            url = '/welcome?username='+valid_username
            self.redirect(url)

        else:
            username_error = ""
            password_error = ""
            verify_error = ""
            email_error = ""

            if not valid_username:
                username_error = "Invalid Username"
            if not valid_password:
                password_error = "Invalid Password"
            if not valid_verify:
                verify_error = "Passwords do not match"
            if not valid_email:
                email_error = "Email address is invalid"

            self.response.status_int = 400

            self.render('user_signup.html',
                        username=username,
                        password=password,
                        verify=verify,
                        email=email,
                        username_error=username_error,
                        password_error=password_error,
                        verify_error=verify_error,
                        email_error=email_error
                        )

    def _validate_user(self, username):
        if UserSignupHandler.USER_RE.match(username):
            return username
        else:
            return None

    def _validate_password(self, password):
        if UserSignupHandler.PASSWORD_RE.match(password):
            return password
        else:
            return None

    def _validate_verify(self, password, verify):
        if UserSignupHandler.PASSWORD_RE.match(verify) and verify==password:
            return verify
        else:
            return None

    def _validate_email(self, email):
        return email


class WelcomeHandler(Handler):
    def get(self):
        username = self.request.get("username")
        self.render('welcome.html', username=username)
