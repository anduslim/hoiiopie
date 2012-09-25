
-----------------
Quick Start
-----------------

Install Hoiio Pie from Python Cheeseshop.

.. code-block:: bash

	sudo pip install hoiiopie

Hoiio Pie will be installed, together with it's dependencies. There is only 1 dependency:

- `Requests <http://docs.python-requests.org>`_

You do NOT need to install the dependencies since they will be automatically installed with `pip install`. 


Start by initializing the service with your Hoiio credentials (a pair of App ID and Access Token). If you have not, register a developer account from `Hoiio <http://developer.hoiio.com>`_ and create an app from the portal. Then make Hoiio API requests!

.. code-block:: python

	from hoiio import Hoiio

	Hoiio.init('MY_APP_ID', 'MY_ACCESS_TOKEN')

	# Makes a voice call back
	Hoiio.voice.call('+6511111111', '+6522222222')

	# Send an SMS
	Hoiio.sms.send('+6511111111', 'Hoiio World~')

	# Fax a document
	Hoiio.fax.send('+6511111111', '/path/to/my/file.pdf')

	# IVR sequence
	Hoiio.ivr.dial('+6511111111')
	# After the call is picked up..
	Hoiio.ivr.gather(session, msg = 'For sales enquiry, please press 1. For technical support, please press 2.')
	# Finally, hangup the call
	Hoiio.ivr.hangup(session)

	
This is *merely* a quick start guide.

Refer to :doc:`/complete_guide` for more usage. 
