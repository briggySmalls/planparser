import pytest

from planparser.planparser import ParseResult


_TEST_DATA = [
	("Total floor area 109.0 sq. m. (1,174 sq. ft.) approx", ["1,174 "], [1174.0], 1174.0)
]


@pytest.mark.parametrize("text,expected", map(lambda x: (x[0], x[1]), _TEST_DATA))
def test_text_match(text, expected):
	m = ParseResult(text).matches
	assert m == expected


@pytest.mark.parametrize("text,expected", map(lambda x: (x[0], x[2]), _TEST_DATA))
def test_numbers_match(text, expected):
	m = ParseResult(text).numbers
	assert m == expected


@pytest.mark.parametrize("text,expected", map(lambda x: (x[0], x[3]), _TEST_DATA))
def test_area_match(text, expected):
	m = ParseResult(text).area
	assert m == expected
