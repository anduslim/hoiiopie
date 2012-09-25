#!/usr/bin/env python
# -*- coding: utf8 -*- 

import unittest
import time
from credentials import *

from hoiio import Hoiio
from hoiio import SmsStatus

class SmsTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)        


    def tearDown(self):
        pass


    def test_send(self):
        res = Hoiio.sms.send('Hello how are you?\n\nGood stuff', MY_SG_MOBILE_NUMBER)
        print 'Txn ref: %s' % res.txn_ref

        self.assertTrue(res.is_success())


    def test_bulk_send_1(self):
        res = Hoiio.sms.bulk_send('1 yeah !@#$%^&*()_+~', MY_SG_MOBILE_NUMBER)
        print res.response.text
        # Due to a bug on Hoiio, the bulk_txn_ref is txn_ref instead
        # print 'Bulk txn ref: %s' % res.bulk_txn_ref
        print 'Bulk txn ref: %s' % res.txn_ref

        self.assertTrue(res.is_success())


    def test_bulk_send_2(self):
        res = Hoiio.sms.bulk_send('2 yeah !@#$%^&*()_+~', MY_SG_MOBILE_NUMBER, MY_US_MOBILE_NUMBER)
        print res.response.text
        # Due to a bug on Hoiio, the bulk_txn_ref is txn_ref instead
        # print 'Bulk txn ref: %s' % res.bulk_txn_ref
        print 'Bulk txn ref: %s' % res.txn_ref

        self.assertTrue(res.is_success())




class QueryTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)
        

    def tearDown(self):
        pass

    
    def test_rate(self):
        res = Hoiio.sms.rate('Hoiio World', MY_SG_MOBILE_NUMBER)

        print res.response.text
        print 'Currency: %s' % res.currency
        print 'Is Unicode?: %s' % res.is_unicode
        print 'Rate: %s' % res.rate
        print 'Split count: %s' % res.split_count
        print 'Total Cost: %s' % res.total_cost

        self.assertTrue(res.is_success())        
        self.assertEqual(res.currency, 'SGD')
        self.assertEqual(res.is_unicode, False)
        self.assertEqual(res.split_count, 1)

        self.assertTrue(isinstance(res.total_cost, float))
        self.assertTrue(isinstance(res.rate, float))
        self.assertTrue(isinstance(res.split_count, int))
        self.assertTrue(isinstance(res.currency, unicode))
            

    def test_rate_in(self):
        res = Hoiio.sms.rate_in(HOIIO_NUMBER_1)

        print res.response.text
        print 'Currency: %s' % res.currency
        print 'Is Unicode?: %s' % res.is_unicode
        print 'Rate: %s' % res.rate
        print 'Split count: %s' % res.split_count
        print 'Total Cost: %s' % res.total_cost

        self.assertTrue(res.is_success())        
        self.assertEqual(res.currency, 'USD')
        self.assertEqual(res.is_unicode, False)
        self.assertEqual(res.split_count, 1)

        self.assertTrue(isinstance(res.total_cost, float))
        self.assertTrue(isinstance(res.rate, float))
        self.assertTrue(isinstance(res.split_count, int))
        self.assertTrue(isinstance(res.currency, unicode))
        

    def test_rate_long(self):
        res = Hoiio.sms.rate('Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World Hoiio World ', '+6590000000')
        
        print res.response.text        
        self.assertTrue(res.is_success())        
        self.assertEqual(res.split_count, 2)


    def test_rate_unicode(self):
        res = Hoiio.sms.rate('你好', MY_US_MOBILE_NUMBER)
        
        print res.response.text        
        self.assertTrue(res.is_success())        
        self.assertEqual(res.is_unicode, True)
    

    def test_history(self):
        res = Hoiio.sms.history()
        self.assertTrue(res.is_success())        
        print 'Total entries count: %s' % res.total_entries_count
        print 'Entries count: %s' % res.entries_count

        self.assertEqual(res.entries_count, len(res.entries))
        
        for entry in res.entries:
            print '-' *40
            print 'txn_ref:\t %s' % entry.txn_ref 
            print 'sms_status:\t %s' % entry.sms_status 
            print 'dest:\t %s' % entry.dest
            print 'date (year):\t %s' % entry.date.year 
            print 'tag:\t %s' % entry.tag 
            print 'split_count:\t %s' % entry.split_count
            print 'src:\t %s' % entry.src
            print 'currency:\t %s' % entry.currency 
            print 'rate:\t %s' % entry.rate 
            print 'debit:\t %s' % entry.debit 

            if entry.sms_status == SmsStatus.DELIVERED:
                print '>> The SMS was delivered!'
            elif entry.sms_status == SmsStatus.QUEUED:
                print '>> The SMS is queuing to be sent'

            if entry.src != None:
                print '>> Outgoing SMS'

        self.assertTrue(res.is_success())        
        

    def test_status(self):
        res = Hoiio.sms.status(SMS_STATUS_TX)

        print res.response.text

        self.assertTrue(res.is_success())        
        self.assertEqual(SMS_STATUS_TX, res.txn_ref)
        self.assertEqual(2012, res.date.year)
        self.assertEqual(9, res.date.month)
        self.assertEqual(10, res.date.day)
        self.assertEqual(17, res.date.hour)
        self.assertEqual(58, res.date.minute)
        self.assertEqual(49, res.date.second)
        
        print 'txn_ref:\t %s' % res.txn_ref 
        print 'sms_status:\t %s' % res.sms_status 
        print 'dest:\t %s' % res.dest
        print 'date (GMT+8):\t %s' % res.date 
        print 'split_count:\t %s' % res.split_count 
        # Bug: Should have src
        # print 'src:\t %s' % res.src
        print 'tag:\t %s' % res.tag 
        print 'currency:\t %s' % res.currency 
        print 'rate:\t %s' % res.rate 
        print 'debit:\t %s' % res.debit 


