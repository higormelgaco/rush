from energy import energyCookie

def main():
      with open('./visual/logo/logo-rush.txt') as logo:
            print(logo.read())
      rush = energyCookie.EnergyCookie()
      try:
            user_input = str(input('\n[+] - Insert the page number bellow and Rush will bring the news:\n\t>> '))
            rush.show(user_input)
      except Exception:
            return 'Sorry! Try again later!'

if __name__ == '__main__':
      main()