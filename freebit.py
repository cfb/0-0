import wsgiref.handlers
import os
from google.appengine.ext import webapp


class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, webapp World! - MainPage '+ os.environ['HTTP_HOST'])


class OtherPage(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, webapp World! - OtherPage ' + os.environ['HTTP_HOST'])


def makepage():
#   print "hello from "+__name__

   application = webapp.WSGIApplication([('/', MainPage),
                                         ('/other', OtherPage)
                                        ],
                                        debug=True)

   wsgiref.handlers.CGIHandler().run(application)

#
# this is a magical way to get makepage() to run only when localhost.py
# is run from the command line, this block is *not* run when you
# "import localhost" from another Python program.
#
if __name__ == "__main__":
    makepage()

