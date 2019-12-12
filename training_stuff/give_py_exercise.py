# Parsing w3resource site with python exercises and outputing random exercise
# Requests - HTTP request lib
# bs4 - HTML parser lib
# 1. get content from each exercise section left navbox <ul class="nav nav-list">
# 2. From there, get a nav-header -> get <a href> link
# 3. From each link get a <p> which has <strong>, which is header of exercise , do n+1
# 4. From same <p> Else is text of this exercise
# 5. create nested 2D list i,j
# 6. header of exercise goes to i, rest is j
# 7. after done with scraping(how do I know if it's done?), create random number x
# 8. random number x is in range of 0:n, n - number of exercises
# 9. Print list(x) and contents of it

import requests
from bs4 import BeautifulSoup, Tag

reqs = requests.get('https://www.w3resource.com/python-exercises/')

# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#print(reqs)
# https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
#print(reqs.headers)
# Store page content.
src = reqs.content
# Start with bs4 parser
# Create BeautifulSoup object based on src
soup = BeautifulSoup(src, 'lxml')

# find_all method to find all <ul> elements on the page with class "nav_list"
navbox_list = soup.find_all("a")
#print(navbox_list)

urls = []
exr_urls = []
for a_tag in navbox_list:
    urls.append(a_tag.attrs['href'])

for url in urls:
    if "/python-exercises/" in url:
        if "https://www.w3resource.com" not in url:
            exr_urls.append("https://www.w3resource.com" + url)
        else:
            exr_urls.append(url)

exercises = []
for url_soup in exr_urls:
    soup_ex = BeautifulSoup(requests.get(url_soup).content, 'lxml')
    div_ex = soup_ex.find("div", class_="mdl-cell mdl-card mdl-shadow--2dp through mdl-shadow--6dp mdl-cell--7-col")
    #пропустить 1 p
    #пробежаться по подряд идущим p пока они не закончатся тэги p
    #paragraph = new Tag()
    #paragraph
    p_tag = Tag(Tag(Tag(div_ex).find("p")).nextSibling())
    for paragraph in div_ex:
        paragraph = Tag(paragraph)
        if paragraph.name != 'p' break
            #содержимое ориджинал контента
            paragraph.ne

    # нечётный p - задание чётный - со ссылкой на ответ, вынимать её
    #p_ex = div_ex.findAll('p')
    exercises.append(x)
#class="mdl-cell mdl-card mdl-shadow--2dp through mdl-shadow--6dp mdl-cell--7-col"
#надо выбрать <p> в нужном <div> брать все подряд нрн
#пока подряд идущие <p> не закончатся


print(exr_urls)
print(len(exr_urls))
print(len(exercises))
print(exercises)
print('END')


