#----------算有幾個--------
list = [1,3,5,7,9,11,13,15,17,19]
count = 0
for i in list:
  count = count + 1
  print('number of list:',count)
  
#功能和下面一樣

print(len(list))

#------------加總-----------
count = 0
for i in list:
  count = count + i
  print('addup: ',count)

#功能和下面一樣

print(sum(list))
