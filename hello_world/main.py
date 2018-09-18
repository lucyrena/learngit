# Copyright 2016 Google Inc.
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

import webapp2
import jinja2
import os
import re
from string import letters
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

# build template
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
 #   def write_form(self, text=""):
  #      self.response.write(form % {"text": text})
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'
       items = self.request.get_all("food")
       self.render('shopping_list.html', items = items)

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

class Task1(Handler):
 #   def write_form(self, text=""):
  #      self.response.write(form % {"text": text})
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'

       self.render('Task1.html')

class Task1_questions(Handler):
 #   def write_form(self, text=""):
  #      self.response.write(form % {"text": text})
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'

       self.render('Task1_questions.html')

class Task2(Handler):
 #   def write_form(self, text=""):
  #      self.response.write(form % {"text": text})
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'

       self.render('Task2.html')
    # def post(self):
    #     text = self.request.get('text')
    #
    #     self.response.write(form % ''.join(a))
        # user_month = valid_month(self.request.get('month'))
        # user_day = valid_day(self.request.get('day'))
        # user_year = valid_year(self.request.get('year'))
        #
        # if (user_year and user_day and user_month) is None:
        #     self.write_form("That doesn't look valid to me, friend!")
        # else:
        #     self.redirect("/thanks")

# class BlogHandler(webapp2.RequestHandler):
#     def write(self, *a, **kw):
#         self.response.out.write(*a, **kw)
#         #q=self.request.get("q")
#         #self.response.write(q+"try again!")
#     def render_str(self, template, **params):
#         t = jinja_env.get_template(template)
#         return t.render(params)
#     def render(self, template, **kw):
#         self.write(self.render_str(template, **kw))
#         #self.response.headers['Content-Type'] = 'text/plain'
#         #self.response.write(self.request)
#
# def blog_key(name = 'default'):
#     return db.Key.from_path('blogs',name)
#
# class Post(db.Model):
#     subject = db.StringProperty(required = True)
#     content = db.TextProperty(required = True)
#     created = db.DateTimeProperty(auto_now_add = True)
#     last_modified = db.DateTimeProperty(auto_now = True)
#
#     def render(self):
#         self._render_text = self.content.replace('\n','<br>')
#         return render_str("post.html", p = self)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/Task1.html', Task1),
    ('/Task1_questions.html', Task1_questions),
    ('/Task2.html', Task2),
    #('/thanks', ThanksHandler)
], debug=True)
