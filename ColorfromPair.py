import Colordefinitions

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(Colordefinitions.MINOR_COLORS)
  if major_index >= len(Colordefinitions.MAJOR_COLORS):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(Colordefinitions.MINOR_COLORS)
  if minor_index >= len(Colordefinitions.MINOR_COLORS):
    raise Exception('Minor index out of range')
  return Colordefinitions.MAJOR_COLORS[major_index], Colordefinitions.MINOR_COLORS[minor_index]
