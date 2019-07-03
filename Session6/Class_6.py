import requests
import bs4

response = requests.get('https://dantri.com.vn/suc-khoe.htm')
# print(response.content.decode())
soup = bs4.BeautifulSoup(response.content.decode(),'html.parser')

# print(soup.title)
all_div = soup.find_all('div',{'data-boxtype':'timelineposition'})
result = []
for v in all_div:
    # first = all_div[0]
    title = v.div.h2.a.string
    link = v.a.img.attrs['src']
    result.append({'title':title, 'link':link})
print(result)
# with open('dantri.html','wt',encoding='utf-8') as f:
#     f.write(response.content.decode())
