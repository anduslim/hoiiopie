

Basics
==========

------------
Setting Up
------------

Before you begin, make sure you have already installed the SDK. Refer to :doc:`/quickstart` if you have not. Basically you do a `pip install hoiiopie`.

To use the package, you import :class:`Hoiio` from :mod:`hoiiopie`. 

Then initialize the service with your Hoiio credentials (a pair of App ID and Access Token). You can create an app and get the Hoiio credentials by logging in at http://developer.hoiio.com. We use a singleton pattern [1]_ to init the credentials, so you only need to call `init(...)` once.

.. code-block:: python

    from hoiio import Hoiio
    
    Hoiio.init('MY_APP_ID', 'MY_ACCESS_TOKEN')

.. note:: Obviously, you need to replace MY_APP_ID and MY_ACCESS_TOKEN with YOUR Hoiio credentials. Obtain them from http://developer.hoiio.com.

.. note:: We use a singleton pattern because most of the time, you are using the same set of credentials for your application. However, if you need to use different credentials simultaneously, then you can always override this behaviour by providing the keys `app_id` and `access_token` in the payload.



---------------
Requests
---------------

Hoiio Pie is designed to simplify your development.

It is designed to be as simple as possible, but no simpler [2]_.

Hence, it has minimal number of classes which you need to know. The most important is :class:`Hoiio`, which you can use to make various API requests, such as:

* Hoiio.voice.call(...)
* Hoiio.sms.send(...)
* Hoiio.fax.send(...)
* Hoiio.ivr.dial(...)
* Hoiio.ivr.gather(...)

As you can see, the services are categorized as voice, sms, fax, ivr, number and account. This correspond to what `Hoiio API <http://developer.hoiio.com/docs/>` provides.

The **required parameters** are passed in as positional arguments to the methods.

The **optional parameters** are passed in as keyword arguments after the positional arguments.

.. code-block:: python

    res = Hoiio.CATEGORY.REQUEST(REQUIRED_1, REQUIRED_2, key1=OPTIONAL_1)

You will see many of the APIs are in the same pattern.


---------------
Response
---------------
    
After you make a service request, a :class:`Response` object will be returned.

You can access the fields of the response object. It corresponds to the response parameters in `Hoiio API <http://developer.hoiio.com/docs/>`.

.. code-block:: python

    print res.txn_ref
    # 'TX-1234'


You can also access additional fields

.. code-block:: python

    # The exact http response body
    print res.text
    # '{"txn_ref": "AA-C-3070102","status": "success_ok"}'

    # The http response body in JSON
    print res.json
    # {'txn_ref': 'AA-C-3070102', 'status': 'success_ok'}

Lastly, the SDK uses `Requests <http://docs.python-requests.org>`_, a HTTP python package for Humans. You can access the `Response class <http://docs.python-requests.org/en/latest/user/advanced/#request-and-response-objects>`_, which gives you access to fields like the HTTP headers and status code.

.. code-block:: python

    print res.response.headers
    # {'content-length': '56170', 'x-content-type-options': 'nosniff', 'x-cache':
    'HIT from cp1006.eqiad.wmnet, MISS from cp1010.eqiad.wmnet', 'content-encoding':
    'gzip', 'age': '3080', 'content-language': 'en', 'vary': 'Accept-Encoding,Cookie',
    'server': 'Apache', 'last-modified': 'Wed, 13 Jun 2012 01:33:50 GMT',
    'connection': 'close', 'cache-control': 'private, s-maxage=0, max-age=0,
    must-revalidate', 'date': 'Thu, 14 Jun 2012 12:59:39 GMT', 'content-type':
    'text/html; charset=UTF-8', 'x-cache-lookup': 'HIT from cp1006.eqiad.wmnet:3128,
    MISS from cp1010.eqiad.wmnet:80'}

You can even access the request headers, if you need it.

.. code-block:: python

    print res.response.request.headers
    # {'Accept-Encoding': 'identity, deflate, compress, gzip',
    'Accept': '*/*', 'User-Agent': 'python-requests/0.13.1'}

.. [1] http://en.wikipedia.org/wiki/Singleton_pattern
.. [2] http://en.wikiquote.org/wiki/Albert_Einstein
