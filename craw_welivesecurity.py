# -*- coding: utf-8 -*-

'''
Search the news articles in welivesecurity
'''

import requests
from datetime import date
from bs4 import BeautifulSoup


def craw_welivesecurity_daily():

    #slice current date and build list
    atual_date = str(date.today()).split('-')
    #slice_date = atual_date.split('-')

    year = atual_date[0]
    month = atual_date[1]
    day = atual_date[2]


    #download content
    pagina = requests.get("https://www.welivesecurity.com/br/{}/{}/{}/".format(year, month, day))


    src = pagina.content
    soup = BeautifulSoup(src, 'lxml')

    #penetration within 'a' tag
    links = soup.find_all('a')

    news = {}
    date_key = '{}/{}/{}'.format(day,month,year)

    #links dentro da tag 'href' que conterem o paremetro fornecido, serao mostrados
    for link in links:
        if ("/br/{}/{}/{}".format(year,month,day) in link.attrs['href']) and (len(link.attrs['href']) > len('https://www.welivesecurity.com/br/{}/{}/{}/'.format(year,month,day))):
            news[date_key] = link.attrs['href']

    return news

print(craw_welivesecurity_daily())





