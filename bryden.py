import wsgiref.handlers
import os
import logging
import datetime, time, calendar
from google.appengine.ext import webapp
from google.appengine.api import mail


class MainPage(webapp.RequestHandler):
  def get(self):
#    self.response.headers['Content-Type'] = 'text/plain'
#    self.response.out.write('Hello, webapp World! - MainPage '+ os.environ['HTTP_HOST'])
    logging.debug('MainPage: ' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()) )

    self.response.out.write(
"""
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-5052616-1");
pageTracker._initData();
pageTracker._trackPageview();
</script>

"""
    )
    MailLog(self)
    pass


class OtherPage(webapp.RequestHandler):
  def get(self):
#    self.response.headers['Content-Type'] = 'text/plain'
#    self.response.out.write('Hello, webapp World! - OtherPage ' + os.environ['HTTP_HOST'] + os.environ['REMOTE_ADDR'] )
    logging.debug('OtherPage: ' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()) )
    self.response.out.write(
"""
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-5052616-1");
pageTracker._initData();
pageTracker._trackPageview();
</script>

"""
    )
    MailLog(self)


class PixelShim(webapp.RequestHandler):
  def get(self):
    logging.debug('PixelShim: ' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()) )
    self.response.out.write(
"""
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-5052616-1");
pageTracker._initData();
pageTracker._trackPageview();
</script>

"""
    )
    mail.send_mail(sender="chris.bryden@gmail.com",
              to="chris+pixelshim@bryden.net",
              subject='pixel shim ipaddress=' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()),
              body=time.asctime(time.localtime()) + ' ipaddress=' + os.environ['REMOTE_ADDR'] + \
                   '\n hostname=' + os.environ['HTTP_HOST'] + \
                   '\n servername=' + os.environ['SERVER_NAME'] + \
                   '\n serversoftware=' + os.environ['SERVER_SOFTWARE'] + \
                   '\n useremail=' + os.environ['USER_EMAIL'] + \
                   '\n authdomain=' + os.environ['AUTH_DOMAIN'] + \
                   '\n useragent=' + self.request.headers['User-Agent'])


def MailLog(self):

  try:
     remoteaddr = os.environ['REMOTE_ADDR'] 
     break
  except KeyError:
     remoteaddr = "robot?"
  else:
     remoteaddr = "other?"

  try:
     localtime = time.asctime(time.localtime()) 
     break
  except KeyError:
     localtime = "robot?"
  else:
     localtime = "other?"

  try:
     ipaddress = os.environ['REMOTE_ADDR'] 
     break
  except KeyError:
     ipaddress = "robot?"
  else:
     ipaddress = "other?"

  try:
     hostname = os.environ['HTTP_HOST'] 
     break
  except KeyError:
     hostname = "robot?"
  else:
     hostname = "other?"

  try:
     servername = os.environ['SERVER_NAME'] 
     break
  except KeyError:
     servername = "robot?"
  else:
     servername = "other?"

  try:
     serversoftware = os.environ['SERVER_SOFTWARE'] 
     break
  except KeyError:
     serversoftware = "robot?"
  else:
     serversoftware = "other?"

  try:
     usernmail = os.environ['USER_EMAIL'] 
     break
  except KeyError:
     usernmail = "robot?"
  else:
     usernamil = "other?"

  try:
     authdomain = os.environ['AUTH_DOMAIN'] 
     break
  except KeyError:
     authdomain = "robot?"
  else:
     authdomain = "other?"

  try:
     headerhost = self.request.headers['Host'] 
     break
  except KeyError:
     headerhost = "robot?"
  else:
     headerhost = "other?"

  try:
     headeraccept = self.request.headers['Accept'] 
     break
  except KeyError:
     headeraccept = "robot?"
  else:
     headeraccept = "other?"

  try:
     acceptcharset = self.request.headers['Accept-Charset'] 
     break
  except KeyError:
     acceptcharset = "robot?"
  else:
     acceptcharset = "other?"

  try:
     useragent = self.request.headers['User-Agent']
     break
  except KeyError:
     useragent = "robot?"
  else:
     useragent = "other?"

  mail.send_mail(sender="chris.bryden@gmail.com",
     to="chris@bryden.net",
     subject='appengine log - ipaddress=' + remoteaddr + ' ' + localtime,
     body= localtime + ' ipaddress=' + remoteaddr + \
        '\n hostname=' + hostname + \
        '\n servername=' + servername + \
        '\n serversoftware=' + serversoftware + \
        '\n useremail=' + usermail + \
        '\n authdomain=' + authdomain + \
        '\n headerhost=' + headerhost + \
        '\n accept=' + headeraccept + \
        '\n Acceptcharset=' + acceptcharset + \
        '\n useragent=' + useragent )


def makepage():
#   print "hello from "+__name__
   logging.debug('bryden makepage: ' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()) )

   application = webapp.WSGIApplication([('/', MainPage),
                                         ('/other', OtherPage),
                                         ('/pixelshim', PixelShim)
                                        ],
                                        debug=False)

   wsgiref.handlers.CGIHandler().run(application)


#
# this is a magical way to get makepage() to run only when localhost.py
# is run from the command line, this block is *not* run when you
# "import localhost" from another Python program. 
#
if __name__ == "__main__":
    makepage()

