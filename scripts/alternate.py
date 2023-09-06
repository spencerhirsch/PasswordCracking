def main():
   print('test')
   f = open('animals.txt', 'r')
   f2 = open('other_animals.txt', 'w')
   lines = f.readlines()
   # for line in f.readlines():
   for line in lines:
      # print(line)
      new_string = ''
      string = line.rstrip()
      for i in range(len(string)):
         if i % 2 == 0:
            new_string += string[i].upper()
         else:
            new_string += string[i]    
      f2.write(new_string + '\n')
main()
