
import PairfromColor, ColorfromPair ,definitions

def print_manual(major_color, minor_color):
  print ('REFERENCE MANUAL for 25-pair color code' + '\n'  + '---------------------------------------')
  print ('PAIR NUMBER : MAJOR COLOR : MINOR COLOR')

  for major_color in definitions.MAJOR_COLORS:
    for minor_color in definitions.MINOR_COLORS:
      pair_number = PairfromColor.get_pair_number_from_color(major_color,minor_color )
      major_color, minor_color = ColorfromPair.get_color_from_pair_number(pair_number)
      print(color_pair_to_string(pair_number, major_color, minor_color))

def color_pair_to_string(pair_number, major_color, minor_color):
  return f' {pair_number} : {major_color} : {minor_color}  '

