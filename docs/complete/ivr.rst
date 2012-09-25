IVR
==========

The IVR APIs are grouped into :

1. Start blocks: Answer, Dial

2. Middle blocks: Play, Gather, Record, Monitor

3. End blocks: Hangup, Transfer

In a call flow, you must start with a Start block, followed by any number of Middle blocks, and lastly end with an End block. For more details, refer to `Hoiio IVR Documentation <http://developer.hoiio.com/docs/ivr.html>`_.



------------------------------------
Answer
------------------------------------

When a call is received on your Hoiio number, your server will receive a notification from Hoiio, and Hoiio expect if you want to answer the call, or ignore. 

Answer is a pseudo API. You don't need to explicitly call it. To answer the call, just use a Middle or End block eg. Play a message or Transfer to another number.

The notification from Hoiio includes a `session`, which is an important data needed for you to make subsequent requests to affect that call session.



------------------------------------
Dial
------------------------------------

Make an outgoing to a number.

.. code-block:: python

    res = Hoiio.ivr.dial('+6511111111')

    print res.session
    # 'S4643'

    print res.txn_ref
    # 'TX-1234'    

An advanced use which call a number with a caller ID, plays a message, and set the max duration for the call.

.. code-block:: python

    res = Hoiio.ivr.dial('+6511111111',
    	msg = 'Hello. This is an automated message from Hoiio.',
    	caller_id = '+6500000000',
    	max_duration = '60',
    	tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )



------------------------------------
Play
------------------------------------

Play a message over the phone

.. code-block:: python

	session = 'S1234'
    res = Hoiio.ivr.play(session, 'Hello. This is an automated message from Hoiio.',
		tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )

    print res.is_success()
    # True



------------------------------------
Gather
------------------------------------

Gather a keypad response over the phone. The following code will ask the user to press 1 for yes or press 2 for no. The system will expect only 1 digit, and it will attempt (and repeats) 3 times if the user does not respond. It will also timeout (hangup) if there is no response in 60 seconds.

.. code-block:: python

	session = 'S1234'
    res = Hoiio.ivr.gather(session, 
    	msg = 'Hello. Press 1 for yes, press 2 for no.',
    	max_digits = 1,
    	timeout = 60,
    	attempts = 3,
		tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )

    print res.is_success()
    # True



------------------------------------
Record
------------------------------------

Record a voice message.

.. code-block:: python

	session = 'S1234'
    res = Hoiio.ivr.record(session, 
    	msg = 'Hello. We are recording your voice message now.',
    	max_duration = 60,
		tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )

    print res.is_success()
    # True



------------------------------------
Monitor
------------------------------------

Monitor a phone conversation, that is record the whole phone conversation from the point that Monitor API is called. 

.. code-block:: python

	session = 'S1234'
    res = Hoiio.ivr.monitor(session, 
    	msg = 'Hello. Note that this phone conversation is recorded.',
		tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )

    print res.is_success()
    # True



------------------------------------
Transfer
------------------------------------

Transfer to a phone number or a conference room.

.. code-block:: python

	session = 'S1234'
    res = Hoiio.ivr.transfer(session, '+6522222222'
    	msg = 'Hello. We will be transferring this call.',
    	caller_id = '+6500000000',
    	tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )

    print res.is_success()
    # True

In the example code above, the call will end no matter if the transfer is successful or not. There are cases where you would want to handle the call if the transfer did not go through eg. `dest` is busy.

You could revert the Transfer operation by setting `on_failure` to 'continue'. This way, you will receive a notification when the transfer did not go through, and you can call subsequent Middle or End blocks. eg. Gather or even another Transfer.

.. code-block:: python

	session = 'S1234'
    res = Hoiio.ivr.transfer(session, '+6522222222'
    	msg = 'Hello. We will be transferring this call.',
    	caller_id = '+6500000000',
    	on_failure = 'continue'
		tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )



------------------------------------
Hangup
------------------------------------

Hangup a call.

.. code-block:: python

	session = 'S1234'
    res = Hoiio.ivr.monitor(session,
    	msg = 'Hello. We will be hanging up now. Bye!',
    	tag = 'myapp',
        notify_url = 'http://my.server.com/myscript'
    )

    print res.is_success()
    # True

You can call this API at any point of time when a call is in progress. You do not need to wait for a notification before calling this API. However, if hangup is used in this way, the `msg` parameter will not be played to the user and the call will hangup immediately.


