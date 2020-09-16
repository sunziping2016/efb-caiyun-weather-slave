import sys


def test_example():
    assert 1 + 1 == 2


def test_import():
    print(sys.path)
    import efb_caiyun_weather_slave.__version__
