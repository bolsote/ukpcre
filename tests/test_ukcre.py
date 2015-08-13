from ukpcre import pattern


class ValidPostcodeTests:
    def test_match(self, data, postcode, first, second):
        assert pattern.match(data)

    def test_groups(self, data, postcode, first, second):
        assert pattern.match(data).group('postcode') == postcode
        assert pattern.match(data).group('first') == first
        assert pattern.match(data).group('second') == second


class TestGirobankPostcodes(ValidPostcodeTests):
    postcodes = (
        ("GIR 0AA", "GIR 0AA", None, None,),
    )

    def test_groups(self, data, postcode, first, second):
        super().test_groups(data, postcode, first, second)

        assert pattern.match(data).group('girobank') == postcode


class TestFullPostcodes(ValidPostcodeTests):
    postcodes = (
        ("W1 6LS", "W1 6LS", "W1", "6LS",),
        ("N1C 4UQ", "N1C 4UQ", "N1C", "4UQ",),
        ("N17 6LA", "N17 6LA", "N17", "6LA",),
        ("SW8 1UQ", "SW8 1UQ", "SW8", "1UQ",),
        ("CW3 9SS", "CW3 9SS", "CW3", "9SS",),
        ("SE5 0EG", "SE5 0EG", "SE5", "0EG",),
        ("WC2H 7LT", "WC2H 7LT", "WC2H", "7LT",),
        ("WC1N 2PL", "WC1N 2PL", "WC1N", "2PL",),
        ("HU12 0AR", "HU12 0AR", "HU12", "0AR"),
    )


class TestPartialPostcodes(ValidPostcodeTests):
    postcodes = (
        ("W1", "W1", "W1", None,),
        ("N1C", "N1C", "N1C", None,),
        ("N17", "N17", "N17", None,),
        ("SW8", "SW8", "SW8", None,),
        ("CW3", "CW3", "CW3", None,),
        ("SE5", "SE5", "SE5", None,),
        ("WC2H", "WC2H", "WC2H", None,),
        ("WC1N", "WC1N", "WC1N", None,),
        ("HU12", "HU12", "HU12", None,),
    )


class TestInvalidPostcode:
    postcodes = (
        ("QA12", None, None, None,),
        ("AJ12", None, None, None,),
        ("Q1A", None, None, None,),
        ("A1V", None, None, None,),
        ("QA1N", None, None, None,),
        ("AZ1N", None, None, None,),
        ("AB1Z", None, None, None,),
    )

    def test_match(self, data, postcode, first, second):
        assert pattern.match(data) is None
