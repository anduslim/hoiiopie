import unittest
import requests
from hoiio import Hoiio 
from hoiio.exceptions import HoiioException
from hoiio.service import Response
from hoiio.service import str_to_date, date_to_str

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
        


