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


