from hoiio.service import Service

from hoiio.service import api_endpoint


class Voice(Service):
	""" Voice service """
	
	def __init__(self):
		pass

	def call(self, dest1, dest2, **kwargs):
		"""
		This method will call 2 phone numbers and connect them up.

        :param dest1: Phone number 1. If ommited, the account registered mobile number will be used. 
        :param dest2: Phone number 2.
        :param caller_id: The caller ID to show to :data:`dest2`

        """
		print 'Calling %s to %s' % (dest1, dest2)
		kwargs['dest1'] = dest1
		kwargs['dest2'] = dest2
		return self.make_request(api_endpoint('voice', 'call'), **kwargs)
		

	def conference(self, *args, **kwargs):
		print 'Conference call to %s' % (args,)
		kwargs['dest'] = ','.join(args)
		return self.make_request(api_endpoint('voice', 'conference'), **kwargs)


	def hangup(self, txn_ref, **kwargs):
		print 'Hangup %s' % (txn_ref)
		kwargs['txn_ref'] = txn_ref
		return self.make_request(api_endpoint('voice', 'hangup'), **kwargs)


	def history(self, **kwargs):
		print 'Call history'
		return self.make_request(api_endpoint('voice', 'get_history'), **kwargs)


	def rate(self, dest1, dest2, **kwargs):
		print 'Calling %s to %s' % (dest1, dest2)
		kwargs['dest1'] = dest1
		kwargs['dest2'] = dest2
		return self.make_request(api_endpoint('voice', 'get_rate'), **kwargs)


	def status(self, txn_ref, **kwargs):
		print 'Status of %s' % (txn_ref)
		kwargs['txn_ref'] = txn_ref
		return self.make_request(api_endpoint('voice', 'query_status'), **kwargs)

