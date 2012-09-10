__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = 'Junda Ong'
__author_email__ = 'junda@hoiio.com'

import urllib
import urllib2

import service.voice
import service.sms
import service.fax
import service.ivr
import service.number
import service.user

class Hoiio(object):

    # Services as class attributes
    voice = service.voice.Voice()
    # sms = service.sms.Sms()
    # fax = service.fax.Fax()
    # ivr = service.ivr.Ivr()
    # number = service.number.Number()
    # user = service.user.User()

    @staticmethod
    def init(app_id, access_token):
        Hoiio.voice.set_auth(app_id, access_token)


# url = 'http://www.acme.com/users/details'
# params = urllib.urlencode({
#   'firstName': 'John',
#   'lastName': 'Doe'
# })
# response = urllib2.urlopen(url, params).read()




class CallStatus:
    """ The Call Status"""
    ANSWERED = 'answered'
    UNANSWERED = 'unanswered'
    FAILED = 'failed'
    BUSY = 'busy'
    ONGOING = 'ongoing'



