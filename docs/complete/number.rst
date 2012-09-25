
Number
==========

The Number API is useful for developers to buy and manage numbers on the fly. If you need only 1 or a few numbers, you could choose to buy and manage from `Hoiio developer portal <http://developer.hoiio.com/>`_. 

------------------------------------
Retrieve available countries
------------------------------------

Retrieve the countries and states that have available Hoiio numbers. The country code and state code are needed later for `Retrieve available numbers`_.

.. code-block:: python

    res = Hoiio.number.available_countries()

    for country in res.entries:
        print '%s [%s] with number prefix %s' % (country.name, country.code, country.prefix)
        # 'USA [US] with number prefix 1'

        # For countries with states
        for state in country.states:
            print '  %s [%s]' % (state.name, state.code)
            # '  Alabama [AL]'

It is not necessary to use this method if the countries you support is pre-determined. You can simply use the country code in ISO 3166-1 alpha-2 format, and state code in ISO 3166-2 format. 

This method is more useful if you want to support new countries dynamically as Hoiio supports them.



------------------------------------
Retrieve available numbers
------------------------------------

Retrieve the numbers availabe for purchasing.

.. code-block:: python

    res = Hoiio.number.available_numbers('US', 'AL')

    for entry in res.entries:
        print entry.number
        # '+16001234567'

For countries without states, the state argument can be omitted.

.. code-block:: python

    res = Hoiio.number.available_numbers('SG')

------------------------------------
Retrieve number cost
------------------------------------

Retrieve how much a number subscription will cost for a country. eg. $4 per month

.. code-block:: python

    res = Hoiio.number.rate('US')

    print res.currency
    # 'USD'

    for entry in res.entries:
        print '%d month: %f %s' % (entry.duration, entry.rate, res.currency)
        # '1 month: 4 USD'


------------------------------------
Subscribe a number
------------------------------------

Subscribe a number for *x* months. 

.. code-block:: python

    # To subscribe for 1 month
    res = Hoiio.number.subscribe('+16001234567', 1)

    print 'Subscribed for %f %s' % (res.debit, res.currency)
    print 'Expires on %s' % res.expiry

You can also subscribe with auto extension. That way, the number will automatically renew every month.

.. code-block:: python

    res = Hoiio.number.subscribe('+16001234567', 'auto_extend')

.. note::

    Make sure you have already added your credit card in Hoiio developer portal.

------------------------------------
Configure a number
------------------------------------

After subscribing to a number, you can configure the number to notify your server when a call/fax/sms is received on the number. 

Number capabilities varies across country; they support a mix of voice, fax and SMS, or none. Voice and fax are mutually exlusive, it's either one or the other. 

As of Sept 2012:

- US numbers supports voice + SMS
- Singapore numbers supports voice/fax
- Hong Kong numbers supports voice
- Vietnam numbers supports voice
- Australia numbers supports voice
- New Zealand numbers supports voice

.. code-block:: python

    # Configure for voice only
    res = Hoiio.number.configure('+16001234567', 
        foward_to = 'http://my.server.com/myscript'
    )

    # Configure for SMS only
    res = Hoiio.number.configure('+16001234567', 
        foward_to_sms = 'http://my.server.com/myscript'
    )

    # Configure for voice + SMS
    res = Hoiio.number.configure('+16001234567', 
        foward_to = 'http://my.server.com/myscript',
        foward_to_sms = 'http://my.server.com/myscript',
    )

    # Configure for fax + SMS
    res = Hoiio.number.configure('+16001234567', 
        foward_to = 'http://my.server.com/myscript',
        foward_to_sms = 'http://my.server.com/myscript',
        mode = 'fax'
    )



------------------------------------
Retrieve subscribed numbers
------------------------------------

Retrieve details of all your subscribed numbers.

.. code-block:: python

    res = Hoiio.number.subscribed_numbers()

    for number in res.entries:
        print number.number
        # '+16001234567'

        print number.forward_to
        # 'http://my.server.com/myscript'

        print number.forward_sms_to
        # 'http://my.server.com/myscript'

        print number.expiry
        # 2012-12-31

        print number.auto_extend_status
        # 'enabled'

        print number.country
        # 'US'

        print number.state
        # 'AL'




