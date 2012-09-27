
Fax
==========

The Fax API can send and receive fax easily.

------------------------------------
Send Fax
------------------------------------

Send a PDF file to a fax number

.. code-block:: python

    res = Hoiio.fax.send('+6511111111', '/path/to/file.pdf')

    print res.txn_ref
    # 'TX-1234'

A more advanced use. The `filename` parameter is used to change the filename that resides at Hoiio.

.. code-block:: python

    res = Hoiio.fax.send('+6511111111', '/path/to/file.pdf',
    	filename = 'awesome-file.pdf',
    	caller_id = '+6500000000',
    	tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )


------------------------------------
Receive Fax
------------------------------------

To receive fax, you need to purchase a Hoiio number that supports receiving fax. Currently (as of Sep 2012), only Singapore numbers are capable of receiving fax.

To get a notification from Hoiio whenever you receive a fax at the number, you will need to go to Hoiio's developer portal and configure the Notify URL, or use :doc:`number` to configure.



------------------------------------
Retrieve Fax status
------------------------------------

Find out the status of a Fax (supports both sent or received) with its `txn_ref`.

.. code-block:: python

    res = Hoiio.fax.status('TX-1234')

    print res.txn_ref
    # 'TX-1234'

    print res.fax_status
    # 'answered'
    
    print res.src
    # '+6500000000'

    print res.dest
    # '+6511111111'
    
    print res.date
    # datetime.datetime(2012, 1, 31, 12, 6, 15)

    print res.fax_pages
    # 3

    print res.fax_url
    # 'http://some.server.com/file.pdf'

    print res.tag
    # 'my-tag'

    print res.currency
    # 'SGD'
    
    print res.rate
    # 0.032
    
    print res.debit
    # 0.064


------------------------------------
Retrieve Fax history
------------------------------------

Query for all fax transactions. Each of `entry` has similar fields as the response in `Retrieve Fax status`_.

.. code-block:: python

    res = Hoiio.fax.history()

    print res.total_entries_count
    # 234

    print res.entries_count
    # 100

    for entry in res.entries:
        print entry.txn_ref
        print entry.fax_status
        # etc ..

You can also filter the fax history by date and type (incoming, outgoing or all).

.. code-block:: python

    res = Hoiio.fax.history(
    	from = '2010-01-01 00:00:00',
    	to = '2012-01-01 00:00:00',
    	page = 3,
    	type = 'incoming'
    )



------------------
Retrieve Fax rate
------------------

Find out how much a fax will cost before you actually send it.

.. code-block:: python

    res = Hoiio.fax.rate('+6511111111')

    print res.currency
    # 'SGD'

    print res.rate
    # 0.032

You also check how much it cost to receive a fax.

.. code-block:: python

    res = Hoiio.fax.rate_in('+6500000000')

    print res.currency
    # 'SGD'

    print res.rate
    # 0.01






