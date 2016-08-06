import unittest
import requests
from credentials import *

from hoiio import Hoiio 
from hoiio.exceptions import HoiioException
from hoiio.service import Response
from hoiio.service import str_to_date, date_to_str

class BasicTest(unittest.TestCase):

    def test_init(self):
        Hoiio.init('a', 'b')
        self.assertEqual(Hoiio.voice.app_id, 'a')
        self.assertEqual(Hoiio.voice.access_token, 'b')


    def test_without_auth(self):
        Hoiio.init(None, None)
        with self.assertRaises(HoiioException):
            Hoiio.voice.call(PHONE_NUMBER_1, PHONE_NUMBER_2)


    def test_bad_response(self):
        url = 'https://google.com/api'
        r = requests.get(url)
        
        self.assertRaises(HoiioException, Response, r)


    def test_str_to_date(self):
        date = str_to_date('2012-01-31 12:06:15.0')
        self.assertEqual(date.year, 2012)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 31)
        self.assertEqual(date.second, 15)

        date = str_to_date('2002-01-31 12:06:40')
        self.assertEqual(date.year, 2002)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 31)
        self.assertEqual(date.second, 40)
        

    def test_date_to_str(self):
        date = str_to_date('2012-01-31 12:06:15')
        s = date_to_str(date)
        self.assertEqual(s, '2012-01-31 12:06:15')

        date = str_to_date('2002-01-31 12:06:40')
        s = date_to_str(date)
        self.assertEqual(s, '2002-01-31 12:06:40')
        

    def test_prefix(self):
        print('Prefix:', Hoiio.prefix)
        self.assertEqual(Hoiio.prefix, '1')

        Hoiio.prefix = '65'
        print('Prefix:', Hoiio.prefix)
        self.assertEqual(Hoiio.prefix, '65')
        
        Hoiio.prefix = ''
        print('Prefix:', Hoiio.prefix)
        self.assertEqual(Hoiio.prefix, '')

        # Should remove the +
        Hoiio.prefix = '+86'
        print('Prefix:', Hoiio.prefix)
        self.assertEqual(Hoiio.prefix, '86')
        

