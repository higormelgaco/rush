import energyCookie

with open('./logo/logo-rush.txt', 'rb') as logo :
      print('\n')
      print(logo.read().decode('utf8'))
      print('\n\n')

try:
      user = int(input())
      energyCookie.show(user)


except:
      print('Invalid option.')

