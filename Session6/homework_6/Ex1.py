import requests
import bs4
import pyexcel as p
from youtube_dl import YoutubeDL

response = requests.get('https://www.apple.com/itunes/charts/songs/')
soup = bs4.BeautifulSoup(response.content.decode(),'html.parser')

all_h3 = soup.find('div',{'id':'main'}).section.ul.find_all('h3')
all_h4 = soup.find('div',{'id':'main'}).section.ul.find_all('h4')

result = []
for i in range(len(all_h3)):
    names = all_h3[i].string
    artists = all_h4[i].string
    result.append({'name':names,'artists':artists})

# p.save_as(records=result,dest_file_name="topusuk.xls")

#chỉ download audio thôi không thì nặng quá

option = {
    'default_search':'ytsearch',
    'max_download':1,
    'format':'bestaudio/audio'
}

dl = YoutubeDL(option)
ls = []
for v in result:
    a = v['name']+" "+v['artists']
    ls.append(a)

dl.download(ls)
