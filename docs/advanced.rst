



--------------------
Phone Number Format
--------------------

You would have noticed that all the phone numbers are in full international format eg. with + and country code and area code. However, you can can change the behaviour by setting the prefix and achieve the same.

.. code-block:: python

    Hoiio.set_prefix('65')
    Hoiio.voice.call('11111111', '22222222')
    # Equivalent to Hoiio.voice.call('+6511111111', '+6522222222')

    # You could mix
    Hoiio.voice.call('+8500000000', '22222222')


