# All middle/end blocks not tested..
# You need to change session on the fly.. (unlikely testable in this way)
session = 'S1234'

import unittest
import time
from credentials import *

from hoiio import Hoiio

class IvrTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)        


    def tearDown(self):
        # Take some time to pickup the call, before another test
        time.sleep(15)
        pass


    def test_dial_1(self):
        res = Hoiio.ivr.dial(MY_SG_MOBILE_NUMBER,
            msg = 'Hello. This is an automated message from Hoiio.',
            caller_id = HOIIO_NUMBER_1,
            max_duration = '10',
            tag = 'myapp',
            notify_url = 'http://google.com'
        )

        self.assertTrue(res.is_success())
        print 'Session: %s' % res.session
        print 'Txn ref: %s' % res.txn_ref
        session = res.session


    def test_dial_prefix_1(self):
        Hoiio.prefix = PHONE_NUMBER_PREFIX
        
        res = Hoiio.ivr.dial(PHONE_NUMBER_SHORT,
            msg = 'Hello. This is an automated message from Hoiio.',
            caller_id = HOIIO_NUMBER_1,
            max_duration = '10',
            tag = 'myapp',
            notify_url = 'http://google.com'
        )

        self.assertTrue(res.is_success())
        print 'Session: %s' % res.session
        print 'Txn ref: %s' % res.txn_ref
        session = res.session



    def test_play_1(self):
        res = Hoiio.ivr.play(session, 'Hello. This is an automated message from Hoiio.',
            tag = 'myapp',
            notify_url = 'http://google.com'
        )
        
        self.assertTrue(res.is_success())




