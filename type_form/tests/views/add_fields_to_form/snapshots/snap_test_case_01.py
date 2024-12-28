# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddFieldsToFormAPITestCase.test_case body'] = [
    {
        'field_type': 'Text',
        'label': 'string',
        'place_holder': 'string'
    }
]

snapshots['TestCase01AddFieldsToFormAPITestCase.test_case status_code'] = '201'
