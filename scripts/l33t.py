def main():
   f = open('l33t_og.txt', 'r')
   f2 = open('l33t.txt', 'w')
   lines = f.readlines()
   # for line in f.readlines():
   for line in lines:
      line_list = line.split('-')
      new_string = line_list[1][1::].strip()
      print(new_string)
      f2.write(new_string + '\n')
main()
