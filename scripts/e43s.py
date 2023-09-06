def main():
   f = open('animals.txt', 'r')
   f2 = open('E43.txt', 'w')
   lines = f.readlines()
   # for line in f.readlines():
   for line in lines:
      if 'e' in line.lower():
         lowercase = line.lower().replace('e', '3').strip()
         new_string = lowercase.capitalize()
      else:
         new_string = line.strip()
      f2.write(new_string + '\n')
main()
