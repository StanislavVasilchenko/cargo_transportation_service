from geopy import distance


def get_distance(lat1, lon1, lat2, lon2):
    pick_up = (lat1, lon1)
    delivery = (lat2, lon2)
    _distance = distance.distance(pick_up, delivery).miles
    return _distance
