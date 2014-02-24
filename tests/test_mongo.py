#!/usr/bin/env python
# coding=utf8

from uuid import uuid4 as uuid

import pytest
pymongo = pytest.importorskip('pymongo')

from simplekv.db.mongo import MongoStore
from basic_store import BasicStore


class TestMongoDB(BasicStore):
    @pytest.fixture
    def db_name(self):
        return '_simplekv_test_{}'.format(uuid())

    @pytest.yield_fixture
    def store(self, db_name):
        conn = pymongo.MongoClient()
        yield MongoStore(conn[db_name])
        conn.drop_database(self.db_name)
