import requests
import bs4
import pyexcel as p 


# arr = [{'title':'title1','content':'content1'},
#         {'title':'title2','content':'content2'}]

# p.save_as(records=arr, dest_file_name="result.xls")

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
    result.append([title, link])

p.save_as(array=result,dest_file_name="dantri.xls")
