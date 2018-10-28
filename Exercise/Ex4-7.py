score = input('Enter score: ')

def computegrade(score) :
  try:
    score = float(score)
  except:
    print('Please enter valid scores')

  if score > 1 :
    print('Please enter valid scores')
  elif score > 0.9 and score <= 1 :
    print('A')
  elif score > 0.8 and score <=0.9 :
    print('B')
  elif score > 0.7 and score <=0.8 :
    print('C')
  elif score > 0.6 and score <= 0.7 :
    print('D')
  else :
    print('F')


computegrade(score)


#Unsolved!!!
