import pyproj

wgs84 = pyproj.CRS("EPSG:4326")
l_est97 = pyproj.CRS("EPSG:3301")


def wgs84_to_l_est97(lat, lon):
    transformer = pyproj.Transformer.from_crs(wgs84, l_est97, always_xy=True)
    x, y = transformer.transform(lon, lat)
    return x, y


def l_est97_to_wgs84(x, y):
    transformer = pyproj.Transformer.from_crs(l_est97, wgs84, always_xy=True)
    lon, lat = transformer.transform(x, y)
    return lat, lon
