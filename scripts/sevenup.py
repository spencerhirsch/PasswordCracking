def main():
   f = open('animals.txt', 'r')
   f2 = open('sevenup.txt', 'w')
   lines = f.readlines()
   # for line in f.readlines():
   for line in lines:
      if len(line.strip()) > 7:
         new = line.strip()
         for i in range(100):
            if i < 10:
               new_string = new + '0' + str(i)
            else:
               new_string = new + str(i)
            f2.write(new_string + '\n')
main()
