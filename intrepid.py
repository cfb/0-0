# Really Critical Google Stuff
#
import wsgiref.handlers
from google.appengine.ext import webapp

# Addon Google Stuff
#
import os
import logging
import datetime, time, calendar


class MainPage(webapp.RequestHandler):
  def get(self):
    logging.debug('intrepid MainPage: ' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()) )
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, webapp World! - MainPage '+ os.environ['HTTP_HOST'] + __name__)


class OtherPage(webapp.RequestHandler):
  def get(self):
    logging.debug('intrepid OtherPage: ' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()) )
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, webapp World! - OtherPage ' + os.environ['HTTP_HOST'])


def makepage():
#   print "hello from "+__name__
   logging.debug('intrepid ' + __name__  + ': ' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()) )

   application = webapp.WSGIApplication([('/', MainPage),
                                         ('/other', OtherPage)
                                        ],
                                        debug=True)

   wsgiref.handlers.CGIHandler().run(application)

#
# this is a magical way to get makepage() to run only when intrepid.py
# is run from the command line, this block is *not* run when you
# "import intrepid" from another Python program. 
#
if __name__ == "__main__":
    makepage()

