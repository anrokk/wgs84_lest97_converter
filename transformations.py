from pyproj import Transformer


def wgs84_to_lest97(lat, lon):
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3301", always_xy=True)
    y, x = transformer.transform(lon, lat)
    return x, y


def lest97_to_wgs84(x, y):
    transformer = Transformer.from_crs("EPSG:3301", "EPSG:4326", always_xy=True)
    lat, lon = transformer.transform(y, x)
    return lon, lat
