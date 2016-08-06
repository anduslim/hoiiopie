import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse

#from . import service
from .service import voice as hoiio_voice
from .service import sms as hoiio_sms
from .service import fax as hoiio_fax
from .service import ivr as hoiio_ivr
from .service import number as hoiio_number
from .service import account as hoiio_account

class Hoiio(object):

    # Services as class attributes
    voice = hoiio_voice.Voice()
    sms = hoiio_sms.Sms()
    number = hoiio_number.Number()
    fax = hoiio_fax.Fax()
    ivr = hoiio_ivr.Ivr()
    account = hoiio_account.Account()

    services = [voice, sms, number, fax, ivr, account]

    @staticmethod
    def init(app_id, access_token):
        for service in Hoiio.services:
            service.set_auth(app_id, access_token)
            service._Hoiio = Hoiio

    # Other configurations
    # Implicit phone number prefix
    prefix = '1'
    # Set debuglevel to 1 to print logs
    debuglevel = 0

class CallStatus:
    """ The Call Status"""
    ANSWERED = 'answered'
    UNANSWERED = 'unanswered'
    FAILED = 'failed'
    BUSY = 'busy'
    ONGOING = 'ongoing'

class SmsStatus:
    """ The SMS Status"""
    QUEUED = 'queued'
    DELIVERED = 'delivered'
    FAILED = 'failed'
    ERROR = 'error'
    RECEIVED = 'received'

class FaxStatus:
    """ The Fax Status"""
    ANSWERED = 'answered'
    UNANSWERED = 'unanswered'
    FAILED = 'failed'
    BUSY = 'busy'
    ONGOING = 'ongoing'


