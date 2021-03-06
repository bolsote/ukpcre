# ukpcre
[![Build Status](https://travis-ci.org/bolsote/ukpcre.svg?branch=master)](https://travis-ci.org/bolsote/ukpcre)
[![Code Climate](https://codeclimate.com/github/bolsote/ukpcre/badges/gpa.svg)](https://codeclimate.com/github/bolsote/ukpcre)

Flexible regular expression to detect full or partial UK postcodes.


## Structure.
The regular expression is based both on [official versions](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/413338/Bulk_Data_Transfer_-_additional_validation_valid_from_March_2015.pdf) and [variatons thereof](http://stackoverflow.com/q/164979/). It looks like this (adding spacing and indentation to make it easier to read):

```
^(?P<postcode>
	(?P<girobank>gir\s*0aa) |                            # Girobank.
	(
		(?P<first>
			((?![qvx])[a-z][a-hk-y]?[0-9][0-9]?) |       # First part: A1, AB1, A12, AB12.
			((?![qvx])[a-z][0-9][a-hjkpstuw]) |          # First part: A1B.
			((?![qvx])[a-z][a-hk-y][0-9][abehmnprvwxy])  # First part: AB1C.
		)\s*(?P<second>[0-9](?![cikmov])[a-z]{2})?       # Second part.
	)
)$
```

It can be divided into three distinct blocks. In all cases, both uppercase and lowercase letters are accepted, and spaces are optional where relevant.

### Girobank postcode.
The first group matches the Girobank postcode (GIR 0AA).

### First section.
The first part of a postcode is covered by two distinct cases:

1. It's followed by the second part, with or without one (or more) whitespace(s).
2. It's the only part of the postcode provided.

Three possibilities are covered via sub-expressions:

1. Postcodes in the form A1, AB1, A12 or AB12: `(?![qvx])[a-z][a-hk-y]?[0-9][0-9]?`.
2. Postcodes in the form A1B: `(?![qvx])[a-z][0-9][a-hjkpstuw]`.
3. Postcodes in the form AB1C: `(?![qvx])[a-z][a-hk-y][0-9][abehmnprvwxy]`.

In all cases, the corresponding alphabetic character classes include the appropriate exclusions, as defined in the relevant [Wikipedia article](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation).

### Second section.
The final section of the full postcode sub-expression, `([0-9](?![cikmov])[a-z]{2})`, matches the second half of a postcode, with or without leading whitespaces (`\s*`). It starts by a number, followed by two letters, excluding the characters `[cikmov]`.


## Testing.
A test suite is provided, with cases to match all of the cases mentioned, including character exclusions. It can be run using [py.test](http://pytest.org).

For every failure a line is generated in a file called `failures.list`, including the affected postcode. This way, it's fairly easy to see a list of the offending postcodes.

### Testing against OS database.
A script and a test generator is provided for testing against the Ordnance Survey Code-Point Open postcode database. This database can't be provided with the code, though, but can be obtained through the [official channels](https://www.ordnancesurvey.co.uk/opendatadownload/products.html).

Once the database has been obtained, the ZIP file can be decompressed under the `tests/data/` directory, and the script `tests/prepare_os_data.py` will generate the postcode database for you. If the test suite is run using the `--osdb` command line switch it will use it. Beware, though: it generates one test for every postcode, and it will take a while.


## Invoke tasks.
A `tasks.py` file is included, which uses the facilities provided by [Invoke](http://www.pyinvoke.org/) in order to provide a cross-platform Makefile-like system. The following tasks are included:

* `test`: Run the test suite. Accepts two arguments:
  * `--osdb`: Run tests against the Ordnance Survey dataset.
  * `--report`: Generate a JUnit-like XML report.
* `genosdb`: Generate the postcode database file necessary to run the test suite against the Ordnance Survey dataset.
* `lint`: Run the `flake8` linter.
* `clean`: Clean up temporary files.


## Notes.
You can also [analyse this regex](https://regex101.com/r/yD1lU1/).
