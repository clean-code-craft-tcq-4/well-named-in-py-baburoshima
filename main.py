import testfile,Colordefinitions
import ReferenceManual

if __name__ == '__main__':
  testfile.test_number_to_pair(4, 'White', 'Brown')
  testfile.test_number_to_pair(5, 'White', 'Slate')
  testfile.test_pair_to_number('Black', 'Orange', 12)
  testfile.test_pair_to_number('Violet', 'Slate', 25)
  testfile.test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
  ReferenceManual.print_manual(Colordefinitions.MAJOR_COLORS, Colordefinitions.MINOR_COLORS)
