from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())  # Indents so we see the nesting.

# This will print out an html file in the python folder location

####

""
match = soup.title.text  # using the ".text." ender you can read it normally without the html
print(match)  # Will show the title of the html file

####

match = soup.div
print(match)  # Shows everything for the first article

match = soup.find('div')
print(match)  # Fidn method allows to add in args

match = soup.find('div', class_='footer')
print(match)  # find the exact arg that you want
# class_ is a special arg in python
# grabs the clas with the div of footer

####

article = soup.find('div', class_='article')
print(article)
# finding a matched tag, or article

headline = article.h2.a.text
print(headline)
# h2 = headline (maybe)
# a = anchor
# text = the text (no html)

summary = article.p.text
print(summary)
# p = paragraph

####

for article in soup.find_all('div', class_='article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()  # blank line
# will get all articles, not just first - will give entire list

####

# parsing an entire website
from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify)

####

article = soup.find('article')
print(article.prettify())
# will print the first article header and paragraph in html format

#instead of print(article)
headline = article.h2.a.text
print(headline)
# to get just the headline text

summary = article.find('div', class_='entry-content').p.text
# .p = paragraph
print(summary)
# to get the paragraph <p> in the <div class="entry-content"

####

# parsing a yt video

vid_src = article.find('iframe',class_='youtube-player')['src']
# print(vid_src)
# finding the <iframe html to parse it
# ID comes after the /embed/
vid_id = vid_src.split('/')[4]  # finds the right index starts at 0
vid_id = vid_id.split('?')[0]
print(vid_id)  # splits all / into diff strings

####

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
# printing out the full yt link.
# {} is a placeholder
# f'' is an f-string (formatted)

####

# get the link, headline, and description for all videos on page
# put it all inside a for loop

for article in  soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    vid_src = article.find('iframe',class_='youtube-player')['src']

    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)

####

# putting the video grabber into a try/except block will take away the error
# if there is no video it will just print None

try:
    vid_src = article.find('iframe',class_='youtube-player')['src']

    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://youtube.com/watch?v={vid_id}'
except Exception as e:
    yt_link = None

print(yt_link)

print()

####
# Have to close out the csv file because of how we opened it

 print()

 csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
