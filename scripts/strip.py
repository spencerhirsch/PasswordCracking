def main():
   f = open('done.txt', 'r')
   f2 = open('stripped.txt', 'w')
   lines = f.readlines()
   # for line in f.readlines():
   for line in lines:
      line = line.strip()
      broken_line = line.split(':')
      print(broken_line)
      # new_string = broken_line[1]
      f2.write(broken_line[0] + ': ' + broken_line[1] +'\n')
main()
