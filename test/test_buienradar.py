from buienradar import Buienradar


def test_get_rain():
    data = Buienradar().get_precipitation_text()
    assert len(data) == 24


def test_next_rain():
    data = Buienradar().get_next_rain_moment()
