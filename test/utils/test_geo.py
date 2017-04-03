#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
import math

from tile_data_extractor.utils import GeoUtils

class LogParserTestCase(unittest.TestCase):

    TILE_11_BY_ZOOM_FIXTURE = {
        1: [0,20037508.3427892,20037508.3427892,0],
        2: [-10018754.1713946,0,0,10018754.1713946],
        3: [-15028131.2570919,10018754.1713946,-10018754.1713946,15028131.2570919],
        4: [-17532819.7999406,15028131.2570919,-15028131.2570919,17532819.7999406],
        5: [-18785164.0713649,17532819.7999406,-17532819.7999406,18785164.0713649],
        6: [-19411336.2070771,18785164.0713649,-18785164.0713649,19411336.2070771],
        7: [-19724422.2749332,19411336.2070771,-19411336.2070771,19724422.2749332],
        8: [-19880965.3088612,19724422.2749332,-19724422.2749332,19880965.3088612],
        9: [-19959236.8258252,19880965.3088612,-19880965.3088612,19959236.8258252],
        10: [-19998372.5843072,19959236.8258252,-19959236.8258252,19998372.5843072],
        11: [-20017940.4635482,19998372.5843072,-19998372.5843072,20017940.4635482],
        12: [-20027724.4031687,20017940.4635482,-20017940.4635482,20027724.4031687],
        13: [-20032616.372979,20027724.4031687,-20027724.4031687,20032616.372979],
        14: [-20035062.3578841,20032616.372979,-20032616.372979,20035062.3578841],
        15: [-20036285.3503367,20035062.3578841,-20035062.3578841,20036285.3503367],
        16: [-20036896.846563,20036285.3503367,-20036285.3503367,20036896.846563],
        17: [-20037202.5946761, 20036896.846563,-20036896.846563,20037202.5946761],
        18: [-20037355.4687327,20037202.5946761,-20037202.5946761,20037355.4687327]
    }

    LAST_TILE_BY_ZOOM_FIXTURE = {
        1 : [0,-20037508.3427892,20037508.3427892,0],
        2 : [10018754.1713946,-20037508.3427892,20037508.3427892,-10018754.1713946],
        3 : [15028131.2570919,-20037508.3427892,20037508.3427892,-15028131.2570919],
        4 : [17532819.7999406,-20037508.3427892,20037508.3427892,-17532819.7999406],
        5 : [18785164.0713649,-20037508.3427892,20037508.3427892,-18785164.0713649],
        6 : [19411336.2070771,-20037508.3427892,20037508.3427892,-19411336.2070771],
        7 : [19724422.2749332,-20037508.3427892,20037508.3427892,-19724422.2749332],
        8 : [19880965.3088612,-20037508.3427892,20037508.3427892,-19880965.3088612],
        9 : [19959236.8258252,-20037508.3427892,20037508.3427892,-19959236.8258252],
        10 : [19998372.5843072,-20037508.3427892,20037508.3427892,-19998372.5843072],
        11 : [20017940.4635482,-20037508.3427892,20037508.3427892,-20017940.4635482],
        12 : [20027724.4031687,-20037508.3427892,20037508.3427892,-20027724.4031687],
        13 : [20032616.372979,-20037508.3427892,20037508.3427892,-20032616.372979],
        14 : [20035062.3578841,-20037508.3427892,20037508.3427892,-20035062.3578841],
        15 : [20036285.3503367,-20037508.3427892,20037508.3427892,-20036285.3503367],
        16 : [20036896.846563,-20037508.3427892,20037508.3427892,-20036896.846563],
        17 : [20037202.5946761,-20037508.3427892,20037508.3427892,-20037202.5946761],
        18 : [20037355.4687327,-20037508.3427892,20037508.3427892,-20037355.4687327]
    }

    def test_should_return_zoom_18_for_metatile_bbox(self):
        xyz = GeoUtils.get_xyz_from_bbox(109419.6059902292,
                                         5489974.901040357,
                                         109801.7911316548,
                                         5490357.086181782,
                                         metatile=2, buffer_size=0)
        self.assertEqual(xyz['z'], 18)

    def test_should_return_zoom_18_for_tile_bbox(self):
        xyz = GeoUtils.get_xyz_from_bbox(109457.824504372,
                                         5490165.99361107,
                                         109610.698560942,
                                         5490318.86766764,
                                         buffer_size=0)
        self.assertEqual(xyz['z'], 18)
        self.assertEqual(xyz['x'], 131788)
        self.assertEqual(xyz['y'], 95158)

    def test_should_return_tile_11_for_all_zoom_levels_from_bbox(self):
        for zoom,bbox in self.TILE_11_BY_ZOOM_FIXTURE.iteritems():
            xyz = GeoUtils.get_xyz_from_bbox(bbox[0],
                                             bbox[1],
                                             bbox[2],
                                             bbox[3],
                                             buffer_size=0)
            self.assertEqual(xyz['z'], zoom, "Bad zoom level for {}".format(zoom))
            self.assertEqual(xyz['x'], 1, "Bad x value for {} zoom level".format(zoom))
            self.assertEqual(xyz['y'], 1, "Bad y value for {} zoom level".format(zoom))

    def test_should_return_last_tile_for_all_zoom_levels_from_bbox(self):
        for zoom,bbox in self.LAST_TILE_BY_ZOOM_FIXTURE.iteritems():
            xyz = GeoUtils.get_xyz_from_bbox(bbox[0],
                                             bbox[1],
                                             bbox[2],
                                             bbox[3],
                                             buffer_size=0)
            self.assertEqual(xyz['z'], zoom, "Bad zoom level for {}".format(zoom))
            self.assertEqual(xyz['x'], math.pow(2,zoom)-1, "Bad x value for {} zoom level".format(zoom))
            self.assertEqual(xyz['y'], math.pow(2,zoom)-1, "Bad y value for {} zoom level".format(zoom))

    def test_should_return_tile_00_and_zoom_2_with_metatile_bbox(self):
        xyz = GeoUtils.get_xyz_from_bbox(-20037508.3,
                                         -2504688.542848656,
                                         2504688.542848656,
                                         20037508.3,
                                         metatile=2, buffer_size=0)
        self.assertEqual(xyz['z'], 2)
        self.assertEqual(xyz['x'], 0)
        self.assertEqual(xyz['y'], 0)

    def test_should_return_tile_20_20_and_zoom_8_with_buffer_256(self):
        xyz = GeoUtils.get_xyz_from_bbox(-17063190.69815647,16593561.59637235,
                                         -16593561.59637235,17063190.69815647,
                                         buffer_size=256)
        self.assertEqual(xyz['z'], 8)
        self.assertEqual(xyz['x'], 20)
        self.assertEqual(xyz['y'], 20)

    def test_should_return_tile_20_20_and_zoom_8_with_buffer_128(self):
        xyz = GeoUtils.get_xyz_from_bbox(-16984919.18119245,16671833.11333637,
                                         -16671833.11333637,16984919.18119245,
                                         buffer_size=128)
        self.assertEqual(xyz['z'], 8)
        self.assertEqual(xyz['x'], 20)
        self.assertEqual(xyz['y'], 20)



    def test_should_return_tile_20_20_and_zoom_8_with_buffer_64(self):
        xyz = GeoUtils.get_xyz_from_bbox(-16945783.42271044,16710968.87181837,
                                         -16710968.87181837,16945783.42271044,
                                         buffer_size=64)
        self.assertEqual(xyz['z'], 8)
        self.assertEqual(xyz['x'], 20)
        self.assertEqual(xyz['y'], 20)

    def test_should_return_tile_20_20_and_zoom_8_with_buffer_32(self):
        xyz = GeoUtils.get_xyz_from_bbox(-16926215.54346943,16730536.75105938,
                                         -16730536.75105938,16926215.54346943,
                                         buffer_size=32)
        self.assertEqual(xyz['z'], 8)
        self.assertEqual(xyz['x'], 20)
        self.assertEqual(xyz['y'], 20)

    def test_should_return_tile_20_20_and_zoom_8_with_buffer_16(self):
        xyz = GeoUtils.get_xyz_from_bbox(-16916431.60384893,16740320.69067988,
                                         -16740320.69067988,16916431.60384893,
                                         buffer_size=16)
        self.assertEqual(xyz['z'], 8)
        self.assertEqual(xyz['x'], 20)
        self.assertEqual(xyz['y'], 20)

    def test_should_return_tile_20_20_and_zoom_8_with_buffer_8(self):
        xyz = GeoUtils.get_xyz_from_bbox(-16911539.63403868,16745212.66049013,
                                         -16745212.66049013,16911539.63403868,
                                         buffer_size=8)
        self.assertEqual(xyz['z'], 8)
        self.assertEqual(xyz['x'], 20)
        self.assertEqual(xyz['y'], 20)

    def test_should_return_tile_20_20_and_zoom_8_with_buffer_0(self):
        xyz = GeoUtils.get_xyz_from_bbox(-16906647.66422842,16750104.63030039,
                                         -16750104.63030039,16906647.66422842,
                                         buffer_size=0)
        self.assertEqual(xyz['z'], 8)
        self.assertEqual(xyz['x'], 20)
        self.assertEqual(xyz['y'], 20)