
SMS
==========

------------------
Send an SMS
------------------

Send a single SMS to a phone. What's better than a Hoiio World message. 

.. code-block:: python

    res = Hoiio.sms.send('Hoiio World', '+6511111111')

There are some optional parameters that you can use as documented in `Hoiio SMS API <http://developer.hoiio.com/docs/sms_send.html>`_. These parameters can be passed in as keyword arguments in all of the methods.

.. code-block:: python

    res = Hoiio.sms.send('Hoiio World', '+6511111111',
        sender_name = 'Citibank',
        tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )

One of the very useful feature is :data:`sender_name`. It should only be used if you have activated the `SMS Rebranding feature <http://developer.hoiio.com/docs/sms_send.html#senderid>`_. You can change to any alphanumeric eg. a company name or other phone numbers. 

The :data:`notify_url` should be your web server. Hoiio will post notification to this URL on the SMS delivery status. You need this to know if the SMS is "queued" of "delivered".

Hoiio API response can be accessed as fields of a :class:`Response` object.

.. code-block:: python

    res = Hoiio.sms.send('Hoiio World', '+6511111111')
    
    print res.txn_ref
    # 'AA-S-1234'
    
    print res.is_success()
    # True

The :data:`txn_ref` is a very important field - a transaction for the API. All chargeable API (eg. making a call back, sending an SMS) will return 1 or more txn_ref. 


-------------------------
Send bulk SMS
-------------------------

Bulk SMS API is a convenient extension to `Send an SMS`_. It sends up to 1,000 SMS in a single request. This is useful if you want to send the same message to multiple phone numbers.

The phone numbers are passed in as variable arguments to the method.

.. code-block:: python

    # SMS to 2 numbers (up to 1000 numbers)
    res = Hoiio.sms.bulk_send('Hoiio World', '+6511111111', '+652222222',
        notify_url = 'http://my.server.com/myscript'
    )
    
    # The bulk_txn_ref that encapsulate individual txn_ref
    print res.bulk_txn_ref
    # 'AA-B-1234'
    
It is recommended that you make use of :data:`notify_url` to track the status of the individual SMS. The :data:`txn_ref` of the individual SMS will be provided during the notification phase.



----------------------
Receive SMS
----------------------

Hoiio supports `receiving SMS <http://developer.hoiio.com/docs/sms_receive.html>`_. Developers need to purchase an SMS enabled number from Hoiio. At the point of writing (Sep 2012), the only country that has SMS enabled number is the US.

To get a notification from Hoiio whenever you receive an SMS at the number, you will need to go to Hoiio's developer portal and configure the Notify URL, or use the :doc:`Number API <number>` to configure.



----------------------
Retrieve SMS status
----------------------

You can find out the SMS status of a particular transaction.

There are many information you can get from a SMS status. Most of the fields are returned as string, int or float. For 'date', a python datetime is returned. Note the datetime is in GMT+8.

.. code-block:: python

    res = Hoiio.sms.status('TX-1234')
    
    print res.txn_ref
    # 'TX-1234'

    print res.sms_status
    # 'delivered'
    
    print res.dest
    # '+6511111111'
    
    print res.date
    # datetime.datetime(2012, 1, 31, 12, 6, 15)

    print res.tag
    # 'my-tag'

    print res.split_count
    # 2
    
    print res.currency
    # 'SGD'
    
    print res.rate
    # 0.032
    
    print res.debit
    # 0.064




---------------------
Retrieve SMS history
---------------------

Query for all the transactions. 

.. code-block:: python

    res = Hoiio.sms.history()

    print res.total_entries_count
    # 234

    print res.entries_count
    # 100

    for entry in res.entries:
        print entry.txn_ref
        print entry.date
        # etc ..

Each entry has similar fields to that of SMS Status (see `Retrieve SMS status`_).

The query history API will fetch the transationcs in batches of 100. To go to the next page:

.. code-block:: python

    res = Hoiio.voice.history(page=2)

You can also filter by dates. The date format is 'YYYY-MM-DD HH:MM:SS' (GMT+8).

.. code-block:: python

    res = Hoiio.voice.history(from='2012-01-01 08:00:00', to='2012-12-31 08:00:00')


------------------
Retrieve SMS rate
------------------

Find out how much an SMS will cost before you actually send it.

.. code-block:: python

    res = Hoiio.sms.rate('Hoiio World', '+6511111111')

    print res.currency
    # 'SGD'

    print res.rate
    # 0.032

    res.split_count
    # 2

    res.total_cost
    # 0.064

    res.is_unicode
    # False


You can also find out how much it cost to receive an SMS on your Hoiio number. Hoiio supports receiving SMS for `only a few countries <http://developer.hoiio.com/docs/sms_receive.html>`_. In the example below, you own the Hoiio number +6599999999.

.. code-block:: python

    res = Hoiio.sms.rate_in('+6599999999')

    print res.currency
    # 'SGD'

    print res.rate
    # 0.01

Note that Hoiio charges per incoming SMS, regardless of the message size or unicode. 

If you don't need to use API to find out the cost (it seldom change anyway), you could refer to `Hoiio Pricing Page <http://developer.hoiio.com/pricing>`_.


