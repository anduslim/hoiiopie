import unittest
import requests
from hoiio import Hoiio 
from hoiio.exceptions import HoiioException
from hoiio.service import Response

class BasicTest(unittest.TestCase):

    def test_init(self):
        Hoiio.init('a', 'b')
        self.assertEqual(Hoiio.voice.app_id, 'a')
        self.assertEqual(Hoiio.voice.access_token, 'b')
        # self.assertTrue(Hoiio.access_token, 'b')

        # self.assertEqual(1 + 2, 3, "1 + 2 not equal to 3")
        # self.assertTrue(False)


    def test_without_auth(self):
        Hoiio.init(None, None)
        with self.assertRaises(HoiioException):
            Hoiio.voice.call('+6591378000', '+6566028066')


    def test_response(self):
        url = 'https://secure.hoiio.com/open/ivr/start/dial?dest=%2B6591378000&msg=Happy Valentine!&caller_id=private&access_token=sbvwYSx7jXf7HGYp&app_id=RzX40cGbJasuIt6B'
        r = requests.get(url)
        response = Response(r)
        self.assertTrue(response.is_success())


    def test_bad_response(self):
        url = 'https://google.com/api'
        r = requests.get(url)
        
        self.assertRaises(HoiioException, Response, r)


    def test_date_from_str(self):

        date = Response.date_from_str('2012-01-31 12:06:15.0')
        self.assertEqual(date.year, 2012)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 31)
        self.assertEqual(date.second, 15)

        date = Response.date_from_str('2002-01-31 12:06:40')
        self.assertEqual(date.year, 2002)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 31)
        self.assertEqual(date.second, 40)
        


