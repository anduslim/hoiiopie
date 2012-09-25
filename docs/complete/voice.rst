
Voice
==========

------------------
Make call back
------------------

Makes a voice call back between 2 phone numbers.

.. code-block:: python

    res = Hoiio.voice.call('+6511111111', '+6522222222')

There are some optional parameters that you can use as documented in `Hoiio Voice API <http://developer.hoiio.com/docs/voice_call.html>`_. These parameters can be passed in as keyword arguments.

.. code-block:: python

    res = Hoiio.voice.call('+6511111111', '+6522222222', 
        caller_id = 'private',
        max_duration = 600,
        tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )

The example above will call with a private caller ID (shown only to dest2), the call will be cut off in 10 minutes (600 sec), tagged with 'myapp' for the application reference, and the server's script will be notified on the call status.

We have shown how you can make an API request. But what about handling the response?

Hoiio API response can be accessed as fields of a Response object.

.. code-block:: python

    res = Hoiio.voice.call('+6511111111', '+6522222222')
    
    print res.txn_ref
    # 'AA-S-141147'
    
    print res.is_success()
    # True

One of the most important field is `txn_ref` - a transaction for the API. All chargeable API (eg. making a call back, sending an SMS) will return 1 or more `txn_ref`. 

It is also possible for the API to return unsuccessful. The response status will then return the error code eg. `error_invalid_http_method`, `error_insufficient_credit`, `error_rate_limit_exceeded`, etc. If `is_success()` returns `False`, then there is an error, and you might want to log the error.

.. code-block:: python

    res = Hoiio.voice.call('+6511111111', '+6522222222')

    if res.is_success():
        print 'The txn ref:', res.txn_ref
    else:
        # The API failed. Print the error code.
        print 'Error:', res.status


-----------------------
Make conference call
-----------------------

Voice call back connects only 2 phone numbers. As an extension, voice conference can connect multiple phone numbers (currently limited to 8 per room).

.. code-block:: python

    # Call 3 phones and put them in a conference
    res = Hoiio.voice.conference('+6511111111', '+6522222222', '+6533333333')
    
    # Find out the room id
    print res.room
    # 'MY-ROOM'
    
    # The transaction reference ID correspond to each of the phone number
    print res.txn_refs
    # ['TX-1', 'TX-2', 'TX-3']


It is not neccessary that you supply all the phone numbers in 1 API request. You could at some point in time add another participant into an existing conference room.

.. code-block:: python

    # Add another participant into the conference room
    res = Hoiio.voice.conference('+6544444444', room='MY-ROOM')
    
    print res.txn_refs
    # ['TX-4']

-------------
Hangup call
-------------

You may also at any point in time hangup any of the participant eg. kick him out of the conference room. In the example below, 'TX-4' refers to the `txn_ref` of +6544444444.

.. code-block:: python

    # Hangup one of the phone. 
    res = Hoiio.voice.hangup('TX-4')

Hangup is applicable to both conference call and call back. The difference is that a call back is considered 1 transaction, so hangup will disconnect both the phones, whereas a conference call is made up of multiple participants (each with their own transaction), so hangup will disconnect the participants individually.


----------------------
Retrieve call status
----------------------

You can find out the call status of a particular transaction.

.. code-block:: python

    res = Hoiio.voice.status('TX-1234')
    
    print res.txn_ref
    # 'TX-1234'

    print res.tag
    # 'my-tag'

    print res.date
    # datetime.datetime(2012, 1, 31, 12, 6, 15)

    print res.dest1
    # '+6511111111'

    print res.dest2
    # '+6522222222'
    
    print res.call_status_dest1
    # 'answered'
    
    print res.call_status_dest2
    # 'answered'
    
    print res.duration
    # 2
    
    print res.currency
    # 'SGD'
    
    print res.rate
    # 0.018
    
    print res.debit
    # 0.036
    

There are many information you can get from a call status. Most of the fields are returned as string or int or float. For 'date', a python datetime is returned. 

.. note::

    All datetime is in GMT+8.

The Call Status can also be used to query for the live status of a call eg. is it still ongoing?

.. code-block:: python

    res = Hoiio.voice.status('TX-1234')
    
    print res.call_status_dest1
    # 'ongoing'


---------------------
Retrieve call history
---------------------

Query for all the transactions. 

.. code-block:: python

    res = Hoiio.voice.history()

    print res.total_entries_count
    # 234

    print res.entries_count
    # 100

    for entry in res.entries:
        print entry.txn_ref
        print entry.date
        # etc ..

Each entry has similar fields to that of Call Status.

The query history API will fetch the transationcs in batches of 100. To go to the next page:

.. code-block:: python

    res = Hoiio.voice.history(page=2)


------------------
Retrieve call rate
------------------

You could find out how much the call back will cost before you actually make the call.

.. code-block:: python

    res = Hoiio.voice.rate('+6511111111', '+6522222222')
    
    print res.currency
    # 'SGD'

    print  res.rate
    # 0.036

    print res.talktime
    # 2352

The about call will cost $0.036 (Singapore Dollars), and with the account credit balance, the call can last 2352 minutes.

If you don't want to use API to find out the cost, you could refer to the `Pricing Page <http://developer.hoiio.com/pricing>`_.


