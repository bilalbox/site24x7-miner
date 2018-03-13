from __future__ import absolute_import

import logging
import requests
import json
from minemeld.ft.basepoller import BasePollerFT

LOG = logging.getLogger(__name__)


class IPv4(BasePollerFT):
    def configure(self):
        super(IPv4, self).configure()

        self.polling_timeout = self.config.get('polling_timeout', 20)
        self.verify_cert = self.config.get('verify_cert', False)
        self.url = 'https://creatorexport.zoho.com/site24x7/location-manager/json/IP_Address_View/C80EnP71mW2fDd60GaDgnPbVwMS8AGmP85vrN27EZ1CnCjPwnm0zPB5EX4Ct4q9n3rUnUgYwgwX0BW3KFtxnBqHt60Sz1Pgntgru/'

    def _process_item(self, item):
        # called on each item returned by _build_iterator
        # it should return a list of (indicator, value) pairs
        if item is None:
            LOG.error('%s - no IP information found', self.name)
            return []

        else:
            value = {
                'type': 'IPv4',
                'confidence': 100
            }

        return [[item, value]]

    def _build_iterator(self, now):
        # called at every polling interval
        # here you should retrieve and return the list of items
        r = requests.get(self.url)

        try:
            r.raise_for_status()
        except:
            LOG.debug('%s - exception in request: %s %s',
                      self.name, r.status_code, r.content)
            raise

        # parse the results into a list
        j = json.loads(r.text)['LocationDetails']
        return iter(loc['external_ip'] for loc in j)

class IPv6(BasePollerFT):
    def configure(self):
        super(IPv6, self).configure()

        self.polling_timeout = self.config.get('polling_timeout', 20)
        self.verify_cert = self.config.get('verify_cert', False)
        self.url = 'https://creatorexport.zoho.com/site24x7/location-manager/json/IP_Address_View/C80EnP71mW2fDd60GaDgnPbVwMS8AGmP85vrN27EZ1CnCjPwnm0zPB5EX4Ct4q9n3rUnUgYwgwX0BW3KFtxnBqHt60Sz1Pgntgru/'

    def _process_item(self, item):
        # called on each item returned by _build_iterator
        # it should return a list of (indicator, value) pairs
        if item is None:
            LOG.error('%s - no IP information found', self.name)
            return []

        else:
            value = {
                'type': 'IPv6',
                'confidence': 100
            }

        return [[item, value]]

    def _build_iterator(self, now):
        # called at every polling interval
        # here you should retrieve and return the list of items
        r = requests.get(self.url)

        try:
            r.raise_for_status()
        except:
            LOG.debug('%s - exception in request: %s %s',
                      self.name, r.status_code, r.content)
            raise

        # parse the results into a list
        j = json.loads(r.text)['LocationDetails']
        return iter(loc['IPv6_Address_External'] for loc in j)
