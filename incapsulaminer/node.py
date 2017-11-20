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
        self.url = 'https://my.incapsula.com/api/integration/v1/ips'

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
        rkwargs = dict(
            stream=False,
            verify=self.verify_cert,
            timeout=self.polling_timeout,
            data=[('resp_format','json'),]
        )

        r = requests.post(
            self.url,
            **rkwargs
        )

        try:
            r.raise_for_status()
        except:
            LOG.debug('%s - exception in request: %s %s',
                      self.name, r.status_code, r.content)
            raise

        # parse the results into a list
        return iter(json.loads(r.text)['ipRanges'])

class IPv6(BasePollerFT):
    def configure(self):
        super(IPv6, self).configure()

        self.polling_timeout = self.config.get('polling_timeout', 20)
        self.verify_cert = self.config.get('verify_cert', False)
        self.url = 'https://my.incapsula.com/api/integration/v1/ips'

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
        rkwargs = dict(
            stream=False,
            verify=self.verify_cert,
            timeout=self.polling_timeout,
            data=[('resp_format','json'),]
        )

        r = requests.post(
            self.url,
            **rkwargs
        )

        try:
            r.raise_for_status()
        except:
            LOG.debug('%s - exception in request: %s %s',
                      self.name, r.status_code, r.content)
            raise

        # parse the results into a list
        return iter(json.loads(r.text)['ipv6Ranges'])
