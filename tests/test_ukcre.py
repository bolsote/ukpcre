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
        ("N1P 4AA", "N1P 4AA", "N1P", "4AA",),
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
        ("N1P", "N1P", "N1P", None,),
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
        ("", None, None, None),
        ("A", None, None, None),
        ("1", None, None, None),
        ("-", None, None, None),
        ("ñ", None, None, None),
        ("W1", None, None, None),
        ("QA12", None, None, None,),
        ("AJ12", None, None, None,),
        ("Q1A", None, None, None,),
        ("A1V", None, None, None,),
        ("QA1N", None, None, None,),
        ("AZ1N", None, None, None,),
        ("AB1Z", None, None, None,),
        ("W1 A11", None, None, None,),
        ("W1 1A1", None, None, None,),
        ("W1 11A", None, None, None,),
        ("W1 AAA", None, None, None,),
        ("N1C A11", None, None, None,),
        ("N1C 1A1", None, None, None,),
        ("N1C 11A", None, None, None,),
        ("N1C AAA", None, None, None,),
        ("N17 A11", None, None, None,),
        ("N17 1A1", None, None, None,),
        ("N17 11A", None, None, None,),
        ("N17 AAA", None, None, None,),
        ("SW8 A11", None, None, None,),
        ("SW8 1A1", None, None, None,),
        ("SW8 11A", None, None, None,),
        ("SW8 AAA", None, None, None,),
        ("WC1N A11", None, None, None,),
        ("WC1N 1A1", None, None, None,),
        ("WC1N 11A", None, None, None,),
        ("WC1N AAA", None, None, None,),
        ("HU12 A11", None, None, None,),
        ("HU12 1A1", None, None, None,),
        ("HU12 11A", None, None, None,),
        ("HU12 AAA", None, None, None,),
    )

    def test_match(self, data, postcode, first, second):
        assert pattern.match(data) is None
