# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetFormFieldsAPITestCase.test_case body'] = [
    {
        'field_id': 1,
        'field_type': 'Text',
        'label': 'string'
    }
]

snapshots['TestCase01GetFormFieldsAPITestCase.test_case status_code'] = '200'