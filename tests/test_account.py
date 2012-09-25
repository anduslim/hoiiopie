import unittest
import time
from credentials import *

from hoiio import Hoiio

class AccountTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)
     

    def tearDown(self):
        pass


    def test_balance(self):
        res = Hoiio.account.balance()
        print 'Balance [%s]: %f (%f + %f)' % (res.currency, res.balance, res.points, res.bonus)
        
        self.assertTrue(res.is_success())
        self.assertTrue(isinstance(res.currency, unicode))
        self.assertTrue(isinstance(res.balance, float))
        self.assertTrue(isinstance(res.points, float))
        self.assertTrue(isinstance(res.bonus, float))


    def test_info(self):
        res = Hoiio.account.info()
        print res.uid
        print res.name
        print res.mobile_number
        print res.email
        print res.country
        print res.currency
        print res.prefix

        self.assertTrue(res.is_success())
        self.assertTrue(isinstance(res.uid, unicode))
        self.assertTrue(isinstance(res.name, unicode))
        self.assertTrue(isinstance(res.mobile_number, unicode))
        self.assertTrue(isinstance(res.email, unicode))
        self.assertTrue(isinstance(res.country, unicode))
        self.assertTrue(isinstance(res.currency, unicode))
        self.assertTrue(isinstance(res.prefix, unicode))
        