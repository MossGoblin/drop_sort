import pytest
from drop_sort import drop_sort as ds
from drop_sort import __version__
import toolbox as tb


def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def bucket():
    return [2, 1, 4, 5, 8, 7, 5, 6, 3, 1, 4, 8, 9, 6, 3, 2, 1]


def test_sort_preset_bucket(bucket):
    result = ds.sort(bucket)
    assert result == [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9]


def test_sort_presorted(bucket):
    bucket.sort()
    result = ds.sort(bucket)
    assert result == [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9]


def test_sort_presorted_reversed(bucket):
    bucket.sort(reverse=True)
    result = ds.sort(bucket)
    assert result == [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9]


def test_sort_equinumerous():
    bucket = [0]*3
    result = ds.sort(bucket)
    assert result == [0, 0, 0]


def test_randomized_bucket_10():
    bucket = tb.get_rand_set(0, 10, 10)
    result = ds.sort(bucket)
    bucket.sort()
    assert result == bucket
