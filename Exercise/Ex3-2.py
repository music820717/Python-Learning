try:
  hr = eval(input("Enter Hours: "))
  rt = eval(input("Enter Rates: "))

  if hr < 40 and hr > 0 :
    wage = hr*rt
  else :
    wage = 40*rt + (hr-40)*1.5*rt

  print("Pay:",round(wage,1))

except:
  print("Error, please enter numeric input")
