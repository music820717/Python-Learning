def computegrade(score):
  try:
    score = float(score)

    if score > 1:
      print('Please enter valid score')
    elif score > 0.9 and score <= 1:
      print('A')
    elif score > 0.8 and score <= 0.9:
      print('B')
    elif score > 0.7 and score <= 0.8:
      print('C')
    elif score > 0.6 and score <= 0.7:
      print('D')
    else:
      print('F')
  
  except:
    print('Please enter valid score')

score = input('Enter score: ')
computegrade(score)
