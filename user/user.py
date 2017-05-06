import random
import string
import hashlib
from google.appengine.ext import ndb


def make_salt():
    return ''.join(random.choice(string.letters) for x in range(0, 5))


# Implement the function valid_pw() that returns True if a user's password
# matches its hash. You will need to modify make_pw_hash.

def make_pw_hash(name, pw, salt=''):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)


def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)


# h = make_pw_hash('spez', 'hunter2')
# print valid_pw('spez', 'hunter2', h)

class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    password_hash = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)


class UserManagement(object):
    # Class Helper Function
    @classmethod
    def _query_user(username):
        return ndb.GqlQuery("SELECT * FROM BlogPost WHERE username=%s" % username)

    def __init__(self, username=''):
        if username:
            self.user = self._query_user(username)
        else:
            self.user = None

    def get_user(self, username):
        # Get an existing user from the database
        if not self.user:
            self.user = self._query_user(username)
        return self.user

    def create_user(self, username, password):
        if not (username and password):
            # A non-empty password is required
            raise ValueError('Username and Password are required')
        password_hash = make_pw_hash(self.user.username, password)
        user = User(username, password_hash)
        return user.put()

    def validate_user(self, name, password_hash):

        ''' Retrieve user from data'''
        pass

    def get_password_hash(self):
        return

if __name__ == '__main__':

    h = make_pw_hash('joel', 'foo')
    print (valid_pw('joel', 'foo', h))
    print (valid_pw('joell', 'foo', h))
