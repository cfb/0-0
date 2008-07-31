import os
import logging
import datetime, time, calendar
from google.appengine.ext import webapp

# personal dev stuff
#
import localhost, bryden, blog

# ideas worth exploring 
#
import freebit, lawn, aparto, paydial, dnrs, wpcr, pcsyardsale, ips
import wms, boatcode, tracker, fbo

# stuff for other people
#
import islandboat, bluewave, intrepid



def main():
  hostname = os.environ['HTTP_HOST']
  logging.debug('disptach: ' + hostname + ' ' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()) )

  if hostname == 'localhost:8080' or hostname == 'localhost:80' or hostname == 'localhost':
     localhost.makepage()
  elif hostname == 'bryden.net' or hostname == 'www.bryden.net':
     bryden.makepage()
  elif hostname == 'fbo.bryden.net':
     fbo.makepage()
  elif hostname == 'aparto.bryden.net':
     aparto.makepage()
  elif hostname == 'freebit.bryden.net':
     freebit.makepage()
  elif hostname == 'lawn.bryden.net':
     lawn.makepage()
  elif hostname == 'tracker.bryden.net':
     tracker.makepage()
  elif hostname == '0990.bryden.net':
     paydial.makepage()
  elif hostname == 'blog.bryden.net':
     blog.makepage()
  elif hostname == 'boatcode.bryden.net':
     boatcode.makepage()
  elif hostname == 'dnrs.bryden.net':
     dnrs.makepage()
  elif hostname == 'ips.bryden.net':
     ips.makepage()
  elif hostname == 'wms.bryden.net':
     wms.makepage()
  elif hostname == 'wpcr.bryden.net':
     wpcr.makepage()
  elif hostname == 'pcsyardsale.bryden.net':
     pcsyardsale.makepage()
  elif hostname == 'intrepid-seas.bryden.net':
     intrepid.makepage()
  elif hostname == 'islandboat.bryden.net':
     islandboat.makepage()
  elif hostname == 'bluewave.bryden.net':
     bluewave.makepage()
#  elif hostname == 'wms.bryden.net':
#     wms.makepage()
  else:
     logging.error('disptach: ' + hostname + ' ' + os.environ['REMOTE_ADDR'] + ' ' + time.asctime(time.localtime()) )
     print "no match on the project host"



if __name__ == "__main__":
  main()
