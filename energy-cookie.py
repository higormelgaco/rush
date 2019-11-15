# -*- coding: utf-8 -*-

import requests
from datetime import date
from bs4 import BeautifulSoup


def welivesecurity():

    #slice current date and build list
    day, month, year = date.today().day, date.today().month, date.today().year
    #download content
    pagina = requests.get("https://www.welivesecurity.com/br/{}/{}/{}/".format(year, month, day))

    src = pagina.content
    soup = BeautifulSoup(src, 'lxml')

    #penetration within 'a' tag
    links = soup.find_all('a')

    news, date_key = {}, '{}/{}/{}'.format(day,month,year)

    #links dentro da tag 'href' que conterem o paremetro fornecido, serao mostrados
    for link in links:
        if ("/br/{}/{}/{}".format(year,month,day) in link.attrs['href']) and (len(link.attrs['href']) > len('https://www.welivesecurity.com/br/{}/{}/{}/'.format(year,month,day))):
            news[date_key] = link.attrs['href']

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



