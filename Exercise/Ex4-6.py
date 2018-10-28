def computepay(hours,rate) :
  pay = 40*int(rate) + (int(hours)-40)*1.5*int(rate)
  return pay

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
print(computepay(hours,rate))


#---------answer(2)--------------

def computepay(hours,rate) :
  try:
    h = float(hours)
    r = float(rate)
  except:
    print('Please enter a numeric value')

  if h >= 40 :
    pay = 40*r + (h-40)*1.5*r
  else:
    pay = h*r
    
  return pay

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
print(computepay(hours,rate))
    
