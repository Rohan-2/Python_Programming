# Tesla

def checkDriver_age():
  age = input('What is your age: ')
  if (int(age) < 18):
    print('Sorry you are not of age, Turnning off!')
  elif (int(age) == 18):
    print('Congratulations on your first year of driving, Enjoy the ride!')
  else:
    print('Powering on, Enjoy the ride!')  
  
checkDriver_age()