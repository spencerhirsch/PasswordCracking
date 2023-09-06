def main():
   f = open('animals.txt', 'r')
   f2 = open('three_animals.txt', 'w')
   lines = f.readlines()
   # for line in f.readlines():
   for line in lines:
       start = line[0:3]
       for line2 in lines:
           new_string = ''
           end = line2[0:3]
           new_string = start + end
           print(new_string)
           f2.write(new_string + '\n')
main()
