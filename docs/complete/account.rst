
Account
============

The Account API retrieves your user profile and credits balance.

------------------------------------
Retrieve credit balance
------------------------------------

Hoiio credit balance is made up of:

1. Main Points (aka `points`)

2. Bonus Points (aka `bonus`)

The only difference is that bonus cannot be transferred to another account. When Hoiio debits, it will take from bonus first.

.. code-block:: python

    res = Hoiio.account.balance()

    print 'Balance [%s]: %f (%f + %f)' % (res.currency, res.balance, res.points, res.bonus)
    # 'Balance [USD]: 12.40 (10 + 2.40)'

------------------------------------
Retrieve account info
------------------------------------

This retrieves the general information about your account.

.. code-block:: python

    res = Hoiio.account.info()

    print res.uid
    # 'AA-1234'

    print res.name
    # 'John Appleton'

    print res.mobile_number
    # '+16001234567'

    print res.email
    # 'John Appleton'

    print res.country
    # 'SG'

    print res.currency
    # 'SGD'

    print res.prefix
    # '1'
