#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from blog.blog import BlogHandler, PostHandler
from blog.blog_post import BlogPostHandler
from home import HomeHandler
from rot13 import Rot13Handler
from user_signup import UserSignupHandler, WelcomeHandler, UserLogoutHandler

app = webapp2.WSGIApplication([
    (r'/', HomeHandler),
    (r'/rot13', Rot13Handler),
    (r'/blog/welcome', WelcomeHandler),
    (r'/blog', BlogHandler),
    (r'/blog/signup', UserSignupHandler),
    (r'/blog/logout', UserLogoutHandler),
    (r'/blog/newpost', BlogPostHandler),
    webapp2.Route(r'/blog/<o_id:\d+>', PostHandler)
], debug=True)

