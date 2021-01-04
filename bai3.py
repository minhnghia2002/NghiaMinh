n = int(input('Enter n: '))

for i in range(0, n + 1):
  if i == 0:
    print(' ' * (n - 1) + '💩', end= '')
  elif i == n:
    print(' ' * (n - 1) + '|', end= '')
#Từ đoạn trên là em hiểu còn từ đoạn này trở xuống em không hiểu
  else:
    for j in range(0, n + i):
      if j < n - i - 1:
        print(' ', end= '')
      else:
        print('*', end= '')
  print('')