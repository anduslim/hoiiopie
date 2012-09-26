# IMPORTANT: Most of the methods are not tested as I didn't buy a Fax number (limited to SG)

import unittest
import time
from credentials import *

from hoiio import Hoiio
from hoiio import FaxStatus

FAX_FILENAME = '/'

class FaxTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)        


    def tearDown(self):
        pass

    # Not tested
    def test_send(self):
        res = Hoiio.fax.send(HOIIO_NUMBER_1, FAX_FILENAME)
        print 'Txn ref: %s' % res.txn_ref

        self.assertTrue(res.is_success())



class QueryTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)    
        

    def tearDown(self):
        pass

    
    def test_rate(self):
        res = Hoiio.fax.rate(HOIIO_NUMBER_1)

        print res.response.text
        print 'Currency: %s' % res.currency
        print 'Rate: %s' % res.rate
        
        self.assertTrue(res.is_success())        
        self.assertEqual(res.currency, 'SGD')
        self.assertTrue(isinstance(res.rate, float))
            

    def test_rate_in(self):
        res = Hoiio.fax.rate_in(HOIIO_NUMBER_1)

        print res.response.text
        print 'Currency: %s' % res.currency
        print 'Rate: %s' % res.rate

        self.assertTrue(res.is_success())        
        self.assertEqual(res.currency, 'SGD')
        self.assertTrue(isinstance(res.rate, float))
                


    def test_history(self):
        res = Hoiio.fax.history()
        self.assertTrue(res.is_success())        
        print 'Total entries count: %s' % res.total_entries_count
        print 'Entries count: %s' % res.entries_count

        self.assertEqual(res.entries_count, len(res.entries))
        
        for entry in res.entries:
            print '-' *40
            print 'txn_ref:\t %s' % entry.txn_ref 
            print 'fax_status:\t %s' % entry.fax_status 
            print 'src:\t %s' % entry.src
            print 'dest:\t %s' % entry.dest
            print 'date:\t %s' % entry.date 
            print 'fax_pages:\t %s' % entry.fax_pages 
            print 'fax_url:\t %s' % entry.fax_url 
            print 'tag:\t %s' % entry.tag 
            print 'currency:\t %s' % entry.currency 
            print 'rate:\t %s' % entry.rate 
            print 'debit:\t %s' % entry.debit 


            if entry.src == None:
                print '>> Outgoing Fax'
                if entry.fax_status == FaxStatus.ANSWERED:
                    print '>> The Fax was sent!'
                elif entry.fax_status == FaxStatus.ONGOING:
                    print '>> The Fax is being sent now'
            else:
                print '>> Incoming Fax'

        self.assertTrue(res.is_success())        
        



