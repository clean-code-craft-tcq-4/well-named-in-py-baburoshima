import definitions

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = definitions.MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = definitions.MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(definitions.MINOR_COLORS) + minor_index + 1

