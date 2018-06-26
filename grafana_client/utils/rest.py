import httplib
import json

import requests

from grafana_client.utils import url_parse


class RestManager(object):
    headers = {'Content-Type': 'application/json'}

    def __init__(self, conf, cli_options=None):
        self.conf = conf
        self.cli_options = cli_options
        self.session = requests.Session()
        try:
            self.base_url = conf.get('grafana_testapi', 'url')
        except:
            self.base_url = 'http://localhost:3000'

        try:
            self.authorization = conf.get('grafana', 'authorization')
        except:
            raise Exception('Grafana Authorization must be provided')

        if self.authorization:
            RestManager.headers.update({'Authorization': self.authorization})

    def get(self, url):
        return self._parse_response('Get',
                                    self._request('get', url,
                                                  headers=self.headers))

    def post(self, url, data):
        return self._parse_response('Create',
                                    self._request('post', url,
                                                  data=json.dumps(data),
                                                  headers=self.headers))

    def put(self, url, data):
        return self._parse_response('Update',
                                    self._request('put', url,
                                                  data=json.dumps(data),
                                                  headers=self.headers))

    def delete(self, url, *args):
        data = json.dumps(args[0]) if len(args) > 0 else None
        return self._parse_response('Delete',
                                    self._request('delete', url,
                                                  data=data,
                                                  headers=self.headers))

    def _request(self, method, url, *args, **kwargs):
        url = url_parse.path_join(self.base_url, url)

        return getattr(self.session, method)(url, *args, **kwargs)

    def _raise_failure(self, op, response):
        raise Exception('{} failed: {}'.format(op, response.reason))

    def _parse_response(self, op, response):
        if response.status_code == httplib.OK:
            if op != 'Delete' and response.text != '':
                return response.json()
            else:
                return None
        else:
            self._raise_failure(op, response)
