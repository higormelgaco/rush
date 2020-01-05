import energyCookie

with open('logo-rush.txt', 'r') as logo :
      print('\n')
      print(logo.read())
      print('\n\n')

try:
      user = int(input("What's the news source do you want Rush to show?\n"
            '[1] - welivesecurity;\n'
            '[2] - scmagazine;\n'
            '[3] - thehackernews;\n'
            '[4] - mente binaria;\n'
            '[5] - talos intelligence;\n'
            '[6] - zdnet;\n'
            '[7] - all the sources;\n'
            'Please, insert the number of the energy cookie that you want : \n'))


      energyCookie.show(user)

except:
      print('Invalid option.')

