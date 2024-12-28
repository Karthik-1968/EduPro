# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01LoginUserAPITestCase.test_case body'] = {
    'access_token': 'string',
    'expires_in': 1
}

snapshots['TestCase01LoginUserAPITestCase.test_case status_code'] = '200'
