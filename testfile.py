#contains test functions for get_color_from_pair_number and get_pair_number_from_color
import ColorfromPair , PairfromColor

def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = ColorfromPair.get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = PairfromColor.get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)
