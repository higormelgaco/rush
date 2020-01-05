# -*- coding: utf-8 -*-

import requests
from datetime import date
from bs4 import BeautifulSoup

def welivesecurity():
    month, year = date.today().month, date.today().year
    pagina = requests.get("https://www.welivesecurity.com/br/{}/{}/".format(year, month))

    soup = BeautifulSoup(pagina.content, 'lxml')
    links, news = soup.select('h2 > a'), []

    for index in range(len(links)):
       news.append([links[index].attrs['title'], links[index].attrs['href']])

    return news

def scmagazine():
   page = requests.get('https://www.scmagazine.com/home/security-news/', headers={"User-Agent": "news"})
   soup = BeautifulSoup(page.content, 'lxml')
   articles = soup.select('h3 > a')

   all_content, unit_content = [],[]

   for index in articles:
      unit_content = str(index).strip('\t\t\t</a>').split('\n\t\t\t\t')
      link = index.attrs['href']
      all_content.append([unit_content[1], link])

   return all_content


def thehackernews():
    page = requests.get('https://thehackernews.com/', headers={"User-Agent": "news"})

    soup = BeautifulSoup(page.content, 'lxml')
    links, title, all_content = soup.select('.story-link'), soup.select('h2'), []

    for index in range(len(links)):
        all_content.append([str(title[index].getText()), links[index].attrs['href']])

    return all_content

def mentebinaria():
    page = requests.get('https://www.mentebinaria.com.br/noticias/', headers={"User-Agent": "news"})

    soup = BeautifulSoup(page.content, 'lxml')
    links, news = soup.select('span > a'), []

    for index in range(len(links)):
        news.append([str(links[index].getText()).strip(), links[index].attrs['href']])

    return news

def talosintelligence():
    year, month = date.today().year, date.today().month
    page = requests.get('https://blog.talosintelligence.com/{}/{}/'.format(year, month), headers={'User-Agent': 'news'})

    soup = BeautifulSoup(page.content, 'lxml')
    links, news = soup.select('h3 > a'), []

    for index in range(len(links)):
        news.append([str(links[index].getText()), links[index].attrs['href']])

    return news

def zdnet():
    page = requests.get('https://www.zdnet.com/topic/security/', headers={"User-Agent": "news"})

    soup = BeautifulSoup(page.content, 'lxml')
    links, news = soup.select('h3 > a'), []

    for index in range(len(links)):
        news.append([str(links[index].getText()).strip(), 'https://www.zdnet.com/topic/security{}'.format(links[index].attrs['href'])])

    return news

#show the reults to the users
def show(number):
      cookies_names, count, number = ['We Live Security', 'SC Magazine', 'The Hacker News', 'Mente Binária', 'Talos Intelligence'], 0, str(number)
      rush_cookies = {
            '1' : welivesecurity(),
            '2' : scmagazine(),
            '3' : thehackernews(),
            '4' : mentebinaria(),
            '5' : talosintelligence(),
            '6' : zdnet()
      }
      try :
            if number == '7':
                for sources in rush_cookies.values():
                    print('{}'.format(cookies_names[count]).center(120, ' '))
                    count += 1
                    for news in range(len(sources)):
                        print()
                        print('>> {}'.format(sources[news][0]))
                        print(sources[news][1] + '\n')
            else:
                  content = rush_cookies[number]
                  print('Main News'.center(120, ' '))
                  for news in range(len(content)):
                        print()
                        print('>> {}'.format(content[news][0]))
                        print(content[news][1])
                        print(''.center(120,' '))

      except:
            print("An error occurred at the capture process. Try again later or verify if the page searched it's up.")

      return
