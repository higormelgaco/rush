import energyCookie

def show(number):
      rush_cookies = {
            '1' : energyCookie.welivesecurity(),
            '2' : energyCookie.scmagazine(),
            '3' : energyCookie.thehackernews(),
            '4' : energyCookie.mentebinaria(),
            '5' : energyCookie.talosintelligence()

      }


      if number == '6':
            for sources in rush_cookies.values():
                  for news in range(len(sources)):
                        print()
                        print('\33[1;31m >> \33[1;0m{}'.format(sources[news][0]))
                        print(sources[news][1])
                        print(''.center(170, '_'))
                  print()
                  print('\33[1;31m'+''.center(170, '~'))
                  print()

      else:
            content = rush_cookies[number]
            print('Main News'.center(100, '-'))
            for news in range(len(content)):
                  print()
                  print('\33[1;31m >> \33[0;0m{}'.format(content[news][0]))
                  print(content[news][1])
                  print(''.center(1030,'_'))

user = str(input("What's the news source do you want Rush to show?\n"
      '[1] - welivesecurity;\n'
      '[2] - scmagazine;\n'
      '[3] - thehackernews;\n'
      '[4] - mente binaria;\n'
      '[5] - talos intelligence;\n'
      '[6] - all the sources;\n'
      'Please, insert the number of the energy cookie that you want : '))


print(show(user))