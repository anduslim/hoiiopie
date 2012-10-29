import unittest
import time
from datetime import datetime
from credentials import *

from hoiio import Hoiio
from hoiio import CallStatus

class CallBackTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)
     


    def tearDown(self):
        # Take some time to pickup the call, before another test
        time.sleep(15)
        pass


    def test_callback(self):
        res = Hoiio.voice.call(dest1=PHONE_NUMBER_1, dest2=PHONE_NUMBER_2)
        print 'Txn ref: %s' % res.txn_ref

        self.assertTrue(res.is_success())

    
    def test_callback_with_optionals(self):
        res = Hoiio.voice.call(PHONE_NUMBER_1, PHONE_NUMBER_2,
            caller_id = 'private',
            max_duration = 600,
            tag = 'myapp',
            notify_url = 'http://api.appspot.com/myscript'
            )

        self.assertTrue(res.is_success())


    def test_callback_invalid_num(self):
        res = Hoiio.voice.call(dest1='1234', dest2=PHONE_NUMBER_2)
        
        self.assertFalse(res.is_success())

        if not res.is_success():
            print 'Error:', res.status

    def test_callback_then_hangup(self):
        res = Hoiio.voice.call(dest1=PHONE_NUMBER_1, dest2=PHONE_NUMBER_2)
        print 'Txn ref: %s' % res.txn_ref
        self.assertTrue(res.is_success())
 
        time.sleep(15)

        # Hangup the call
        print 'Hangup up the calls..'
        txn_ref = res.txn_ref
        res = Hoiio.voice.hangup(txn_ref)
        self.assertTrue(res.is_success())




class ConferenceTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)        


    def tearDown(self):
        # Take some time to pickup the call, before another test
        time.sleep(15)
        pass


    def test_conference(self):
        res = Hoiio.voice.conference(PHONE_NUMBER_1, PHONE_NUMBER_2)
        print 'Txn refs: %s' % res.txn_refs
        print 'Room: %s' % res.room

        for txn_ref in res.txn_refs:
            print 'Txn ref: %s' % txn_ref

        self.assertEqual(len(res.txn_refs), 2)
        self.assertTrue(res.is_success())


    def test_conference_with_room(self):
        room_name = 'my.123.abc_room'
        res = Hoiio.voice.conference(PHONE_NUMBER_1, PHONE_NUMBER_2, room=room_name)
        print 'Txn refs: %s' % res.txn_refs
        print 'Room: %s' % res.room

        for txn_ref in res.txn_refs:
            print 'Txn ref: %s' % txn_ref

        self.assertEqual(res.room, room_name)
        self.assertEqual(len(res.txn_refs), 2)
        self.assertTrue(res.is_success())


    def test_conference_then_hangup_1(self):
        # 1) Make the conference call
        res = Hoiio.voice.conference(PHONE_NUMBER_1, PHONE_NUMBER_2)
        self.assertTrue(res.is_success())
        txn1 = res.txn_refs[0]
        txn2 = res.txn_refs[1]
        time.sleep(15)

        # 2) Hangup the call
        print 'Hangup up call 1..'
        res = Hoiio.voice.hangup(txn1)
        self.assertTrue(res.is_success())


    def test_conference_then_hangup_2(self):
        # 1) Make the conference call
        res = Hoiio.voice.conference(PHONE_NUMBER_1, PHONE_NUMBER_2)
        self.assertTrue(res.is_success())
        txn1 = res.txn_refs[0]
        txn2 = res.txn_refs[1]
        time.sleep(15)

        # 2) Hangup the call
        print 'Hangup up call 2..'
        res = Hoiio.voice.hangup(txn2)
        self.assertTrue(res.is_success())
    




class QueryTest(unittest.TestCase):

    def setUp(self):
        # Setup Hoiio credentials
        Hoiio.init(APP_ID, ACCESS_TOKEN)


    def tearDown(self):
        pass

    
    def test_rate(self):
        res = Hoiio.voice.rate(dest1=PHONE_NUMBER_1, dest2=PHONE_NUMBER_2)
        print 'Currency: %s' % res.currency
        print 'Rate: %s' % res.rate
        print 'Talktime: %s' % res.talktime

        self.assertTrue(res.is_success())        
        self.assertEqual(res.currency, 'SGD')
        
        self.assertTrue(isinstance(res.currency, unicode))
        self.assertTrue(isinstance(res.rate, float))
        self.assertTrue(isinstance(res.talktime, int))


    def test_history(self):
        res = Hoiio.voice.history()
        print res.response.text
        
        self.assertTrue(res.is_success())        
        self.assertEqual(res.entries_count, len(res.entries))
        self.assertTrue(isinstance(res.total_entries_count, int))
        self.assertTrue(isinstance(res.entries_count, int))

        print 'Total entries count: %s' % res.total_entries_count
        print 'Entries count: %s' % res.entries_count
        
        for entry in res.entries:
            print '-' *40
            print 'txn_ref:\t %s' % entry.txn_ref 
            print 'tag:\t %s' % entry.tag 
            print 'date:\t %s' % entry.date
            print 'dest1:\t %s' % entry.dest1 
            print 'dest2:\t %s' % entry.dest2
            if hasattr(entry, 'number'):
                print 'hoiio#:\t %s' % entry.number
            print 'call_status_dest1:\t %s' % entry.call_status_dest1 
            print 'call_status_dest2:\t %s' % entry.call_status_dest2
            print 'duration:\t %s' % entry.duration
            print 'currency:\t %s' % entry.currency 
            print 'rate:\t %s' % entry.rate 
            print 'debit:\t %s' % entry.debit 

            if entry.call_status_dest1 == CallStatus.ANSWERED:
                print '>> The call was answered!'

            self.assertTrue(isinstance(entry.date, datetime))
            self.assertTrue(isinstance(entry.rate, float))
            self.assertTrue(isinstance(entry.debit, float))
            self.assertTrue(isinstance(entry.duration, int))
            self.assertTrue(isinstance(entry.txn_ref, unicode))
            

    def test_status(self):
        res = Hoiio.voice.status(VOICE_STATUS_TX)
        print res.response.text
        
        self.assertTrue(res.is_success())        
        self.assertEqual(VOICE_STATUS_TX, res.txn_ref)
        
        print 'txn_ref:\t %s' % res.txn_ref 
        print 'tag:\t %s' % res.tag 
        print 'date (GMT+8):\t %s' % res.date 
        print 'dest1:\t %s' % res.dest1 
        print 'dest2:\t %s' % res.dest2
        print 'call_status_dest1:\t %s' % res.call_status_dest1 
        print 'call_status_dest2:\t %s' % res.call_status_dest2
        print 'duration:\t %s' % res.duration
        print 'currency:\t %s' % res.currency 
        print 'rate:\t %s' % res.rate 
        print 'debit:\t %s' % res.debit 

        self.assertTrue(isinstance(res.date, datetime))
        self.assertTrue(isinstance(res.duration, int))
        self.assertTrue(isinstance(res.rate, float))
        self.assertTrue(isinstance(res.debit, float))
        self.assertTrue(isinstance(res.currency, unicode))



