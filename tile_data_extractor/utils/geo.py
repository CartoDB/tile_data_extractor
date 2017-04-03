import math
from decimal import Decimal

class GeoUtils(object):

    EARTH_RADIUS = 6378137
    EARTH_DIAMETER = EARTH_RADIUS * 2
    EARTH_CIRCUMFERENCE = EARTH_DIAMETER * math.pi
    TILE_SIZE_PIXEL = 256.0

    @classmethod
    def get_xyz_from_bbox(cls, xmin, ymin, xmax, ymax, metatile=1, buffer_size=0):
        initial_res = (cls.EARTH_CIRCUMFERENCE)/cls.TILE_SIZE_PIXEL
        origin_shift = (initial_res * cls.TILE_SIZE_PIXEL) / 2.0
        if metatile > 1:
            zoom = GeoUtils.get_zoom_from_metatile_bbox(xmin, ymin, xmax, ymax, metatile)
        elif buffer_size >= 64:
            zoom = GeoUtils.get_zoom_from_metatile_bbox(xmin, ymin, xmax, ymax, 2)
        else:
            zoom = GeoUtils.get_zoom_from_tile_bbox(xmin, ymin, xmax, ymax)
        if buffer_size > 0:
            xmin, ymin, xmax, ymax, zoom = cls.__substract_buffer(
                xmin, ymin, xmax, ymax, zoom, buffer_size)
        tile_geo_size = cls.TILE_SIZE_PIXEL * (initial_res / (math.pow(2, zoom)))
        x = round(Decimal((xmin + origin_shift)/tile_geo_size))
        y = round(Decimal(-((ymax - origin_shift)/tile_geo_size)))
        return {'x': x, 'y': y, 'z': zoom}

    @classmethod
    def __substract_buffer(cls, xmin, ymin, xmax, ymax, zoom, buffer_size):
        # If buffer size is greater or equal to 128 we have to adjust the zoom level
        # because for example a buffer size of 128 adds 128 pixels to each side
        # so at the end we have a metatile
        if buffer_size >= 128:
            zoom += (buffer_size / 128) - 1
        res = cls.EARTH_CIRCUMFERENCE/math.pow(2, zoom)/cls.TILE_SIZE_PIXEL
        buffered_xmin = xmin + (buffer_size * res)
        buffered_xmax = xmax - (buffer_size * res)
        buffered_ymin = ymin + (buffer_size * res)
        buffered_ymax = ymax - (buffer_size * res)
        return buffered_xmin, buffered_ymin, buffered_xmax, buffered_ymax, zoom

    @classmethod
    def get_zoom_from_metatile_bbox(cls, minx, miny, maxx, maxy, metatile):
        diff = maxx - minx
        return round(Decimal(math.log((cls.EARTH_CIRCUMFERENCE/(diff/metatile)), 2)))

    @classmethod
    def get_zoom_from_tile_bbox(cls, minx, miny, maxx, maxy):
        diff = maxx - minx
        return round(Decimal(math.log((cls.EARTH_CIRCUMFERENCE/diff), 2)))
