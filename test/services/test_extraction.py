#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest

from tile_data_extractor.services import TileDataExtractionService
from tile_data_extractor.repositories import InMemoryRepository

from ..test_helper import fixture_path

class TileDataExtractionServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.repository = InMemoryRepository()
        self.service = TileDataExtractionService(self.repository)

    def test_should_extract_data_from_previous_process_correctly(self):
        self.service.process(fixture_path('basemaps_processed_log.txt'))
        self.assertEqual(len(self.repository.get_all()), 3)
    
    def test_should_filter_data_with_bad_bbox(self):
        self.service.process(fixture_path('bad_bbox_log.txt'))
        self.assertEqual(len(self.repository.get_all()), 0)

    def test_should_extract_data_from_user_queries_correctly(self):
        self.service.process(fixture_path('userdb_processed_log.txt'))
        self.assertEqual(len(self.repository.get_all()), 2)