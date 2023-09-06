def main():
   f = open('shadow-fall23.txt', 'r')
   lines = f.readlines()
   # for line in f.readlines():
   count = 0
   for line in lines:
      count += 1
   print(count)
main()
