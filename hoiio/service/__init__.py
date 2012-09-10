import requests
import datetime

from hoiio.exceptions import HoiioException


HOIIO_API_ENDPOINT = 'https://secure.hoiio.com/open/'


class Service:

    def __init__(self, app_id, access_token):
        setAuth(app_id, access_token)

    def set_auth(self, app_id, access_token):   
        self.app_id = app_id
        self.access_token = access_token

    def make_request(self, url, **kwargs):
        self.validate_auth()

        kwargs['app_id'] = self.app_id
        kwargs['access_token']  = self.access_token
        for key in kwargs:
            print '%s: %s' % (key, kwargs[key])

        r = requests.get(url, params=kwargs)
        # print 'Response: %s' % r.text
        
        return Response(r)

    def validate_auth(self):
        if not hasattr(self, 'app_id') or not hasattr(self, 'access_token') or (self.app_id == None) or (self.access_token == None):
            raise HoiioException('App ID and Access Token not init')


class Response:
    """
    A class to encapsulate the API response. It also contains the Response class
    from requests.

    response = Response(r)
    response.status
    """

    def __init__(self, response):
        """
        response is from Requests
        """
        self.response = response
        self.json = response.json
        self.text = response.text
        try:
            for key in response.json:
                value = response.json[key]
                # We do special handling for certain response keys
                if key == 'txn_refs':
                    txn_refs_list = value.split(',')
                    setattr(self, key, txn_refs_list)
                if key == 'date':
                    setattr(self, key, Response.date_from_str(value))
                elif key == 'entries':
                    # Turns each entry (a dict) into an object
                    i = 0
                    for entry in value:
                        obj = obj_dic(entry)
                        value[i] = obj
                        i += 1
                    setattr(self, key, value)
                    # Change date string to datetime
                    for entry in value:
                        entry.date = Response.date_from_str(entry.date)
                else:
                    setattr(self, key, value)
        except Exception, e:
            # It is possible that json is empty and throws: TypeError: 'NoneType' object is not iterable
            print 'Exception: %s' % e
            import traceback
            traceback.print_exc()
            raise HoiioException

    def is_success(self):
        if self.json['status'] == 'success_ok':
            return True
        return False

    @staticmethod
    def date_from_str(s):
        # Due to a bug from API, date might have micro sec (after .)
        if '.' in s:
            f = "%Y-%m-%d %H:%M:%S.%f"
        else:
            f = "%Y-%m-%d %H:%M:%S"
        return datetime.datetime.strptime(s, f)


def api_endpoint(*args):
    endpoint = HOIIO_API_ENDPOINT
    for arg in args:
        endpoint = endpoint + arg + '/'
    return endpoint[:-1]


# http://stackoverflow.com/questions/1305532/convert-python-dict-to-object
def obj_dic(d):
    top = type('new', (object,), d)
    seqs = tuple, list, set, frozenset
    for i, j in d.items():
        if isinstance(j, dict):
            setattr(top, i, obj_dic(j))
        elif isinstance(j, seqs):
            setattr(top, i, 
                    type(j)(obj_dic(sj) if isinstance(sj, dict) else sj for sj in j))
        else:
            setattr(top, i, j)
    return top