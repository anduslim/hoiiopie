import unittest
from datetime import datetime
from credentials import *

from hoiio import Hoiio

class NumberTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)        
        

    def tearDown(self):
        pass


    def test_available_countries(self):
        res = Hoiio.number.available_countries()

        self.assertTrue(res.is_success())
        self.assertEqual(res.entries_count, len(res.entries))
        self.assertTrue(isinstance(res.entries_count, int))

        for country in res.entries:
            self.assertTrue(isinstance(country.code, str))
            self.assertTrue(isinstance(country.name, str))
            self.assertTrue(isinstance(country.prefix, str))
            print('%s [%s] with number prefix %s' % (country.name, country.code, country.prefix))

            if country.states:
                for state in country.states:
                    self.assertTrue(isinstance(state.code, str))
                    self.assertTrue(isinstance(state.name, str))
                    print('  %s [%s]' % (state.name, state.code))


    def test_available_numbers(self):
        res = Hoiio.number.available_numbers('US', 'AL')
        print(res.response.text)
        self.assertTrue(res.is_success())
        self.assertEqual(res.entries_count, len(res.entries))
        self.assertTrue(isinstance(res.entries_count, int))
        self.assertTrue(isinstance(res.total_entries_count, int))

        for entry in res.entries:
            print('%s %s' % (entry.number, entry.capability))
            self.assertTrue(isinstance(entry.number, str))


    def test_available_numbers_page2(self):
        res = Hoiio.number.available_numbers('US', 'AL', page=2)
        print(res.response.text)
        self.assertTrue(res.is_success())
        self.assertEqual(res.entries_count, len(res.entries))
        self.assertTrue(isinstance(res.entries_count, int))
        self.assertTrue(isinstance(res.total_entries_count, int))

        for entry in res.entries:
            print(entry.number)
            self.assertTrue(isinstance(entry.number, str))


    def test_available_numbers_page_sg_all(self):
        page = 1
        while True:
            res = Hoiio.number.available_numbers('SG', page=page)
            print(res.response.text)

            if page ==1:
                print('Total:', res.total_entries_count)

            # No more pages
            if res.entries_count == 0:
                break;

            self.assertTrue(res.is_success())
            self.assertEqual(res.entries_count, len(res.entries))
            self.assertTrue(isinstance(res.entries_count, int))
            self.assertTrue(isinstance(res.total_entries_count, int))

            for entry in res.entries:
                print(entry.number)
                print('Support Voice:', True if 'VOICE' in entry.capability else False)
                print('Support Fax:', True if 'FAX' in entry.capability else False)
                print('Support SMS:', True if 'SMS' in entry.capability else False)
                self.assertTrue(isinstance(entry.capability, list))
                self.assertTrue(isinstance(entry.number, str))

            page += 1


    def test_number_cost(self):
        res = Hoiio.number.rate('US')
        
        self.assertTrue(res.is_success())
        self.assertEqual(res.currency, 'SGD')
        
        for entry in res.entries:
            print('%d %s for %s month' % (entry.rate, res.currency, entry.duration))
            self.assertTrue(isinstance(entry.rate, float))
            self.assertTrue(isinstance(entry.duration, int))


    def test_number_cost_sg(self):
        res = Hoiio.number.rate('SG')
        
        self.assertTrue(res.is_success())
        self.assertEqual(res.currency, 'SGD')
        
        for entry in res.entries:
            print('%d %s for %s month' % (entry.rate, res.currency, entry.duration))
            self.assertTrue(isinstance(entry.rate, float))
            self.assertTrue(isinstance(entry.duration, int))

                        
    def test_number_subscribe_1_mth(self):
        # Cannot test on production
        res = Hoiio.number.subscribe(HOIIO_NUMBER_1, 1)
        print(res.response.text)
        self.assertFalse(res.is_success())
        # self.assertTrue(res.is_success())
        # self.assertEqual(res.currency, 'SGD')
        # self.assertTrue(isinstance(res.debit, float))


    def test_number_subscribe(self):
        # Cannot test on production
        res = Hoiio.number.subscribe(HOIIO_NUMBER_1, 'auto_extend')
        self.assertFalse(res.is_success())
        # self.assertTrue(res.is_success())
        # self.assertEqual(res.currency, 'SGD')
        # self.assertTrue(isinstance(res.debit, float))


    def test_configure_voice(self):
        res = Hoiio.number.configure(HOIIO_NUMBER_1, 
            forward_to='http://google.com/')
        self.assertTrue(res.is_success())

    def test_configure_sms(self):
        res = Hoiio.number.configure(HOIIO_NUMBER_1, 
            forward_sms_to='http://google.com/')
        self.assertTrue(res.is_success())
     
    def test_configure_voice_sms(self):
        res = Hoiio.number.configure(HOIIO_NUMBER_1, 
            forward_to='http://google.com/', 
            forward_sms_to='http://google.com/')
        self.assertTrue(res.is_success())
     
    def test_configure_fax_sms(self):
        res = Hoiio.number.configure(HOIIO_NUMBER_1, 
            forward_to='http://google.com/', 
            forward_sms_to='http://google.com/',
            mode='fax')
        self.assertTrue(res.is_success())
     
    def test_active_numbers(self):
        res = Hoiio.number.subscribed_numbers()
        print(res.response.text)
        self.assertTrue(res.is_success())
        self.assertEqual(res.entries_count, len(res.entries))
        self.assertTrue(isinstance(res.entries_count, int))
        
        for number in res.entries:
            self.assertTrue(isinstance(number.number, str))
            self.assertTrue(isinstance(number.forward_to, str))
            self.assertTrue(isinstance(number.expiry, datetime))
            self.assertTrue(isinstance(number.auto_extend_status, bool))
            print(number)
            print('Number:', number.number)
            print('Fwd to:', number.forward_to)
            print('Fwd to sms:', number.forward_sms_to)
            print('Expiry:', number.expiry)
            print('Auto Extend:', number.auto_extend_status)
            # missing mode
            print('Country:', number.country)
            print('State:', number.state)


