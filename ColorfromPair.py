import definitions

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(definitions.MINOR_COLORS)
  if major_index >= len(definitions.MAJOR_COLORS):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(definitions.MINOR_COLORS)
  if minor_index >= len(definitions.MINOR_COLORS):
    raise Exception('Minor index out of range')
  return definitions.MAJOR_COLORS[major_index], definitions.MINOR_COLORS[minor_index]
