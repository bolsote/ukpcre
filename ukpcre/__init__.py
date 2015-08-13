import re


_ukpcre = r"""
    ^(?P<postcode>
        (?P<girobank>gir\s*0aa) |                            # Girobank.
        (
            (?P<first>
                ((?![qvx])[a-z][a-hk-y]?[0-9][0-9]?) |       # First part: A1, AB1, A12, AB12.
                ((?![qvx])[a-z][0-9][a-hjkstuw]) |           # First part: A1B.
                ((?![qvx])[a-z][a-hk-y][0-9][abehmnprvwxy])  # First part: AB1C.
            )\s*(?P<second>[0-9](?![cikmov])[a-z]{2})?       # Second part.
        )
    )$
"""

pattern = re.compile(_ukpcre, re.IGNORECASE | re.VERBOSE)
