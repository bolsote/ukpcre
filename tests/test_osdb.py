import pytest

import pickle

from ukpcre import pattern


def pytest_generate_tests(metafunc):
    if pytest.config.getoption("osdb"):
        with open("tests/OSpostcodes.db", "rb") as f:
            metafunc.parametrize("postcode", pickle.load(f))
    else:
        metafunc.parametrize("postcode", pytest.skip([]))


def test_OS_postcodes(postcode):
    assert pattern.match(postcode)
