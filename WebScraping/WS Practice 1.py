# Import Necessary libraries
from bs4 import BeautifulSoup as bs
import requests

# Load the Webpage
r = requests.get('https://en.wikipedia.org/wiki/Toy_Story_4')

# convert to a beautiful soup object
soup = bs(r.content)

# Print out the HTML
contents = soup.prettify()
#print(contents)

# Print the info box on wiki
info_box = soup.find(class_='infobox vevent')
#print(info_box.prettify())

# find the title and the tablerows
info_rows = info_box.find_all('tr')
for row in info_rows:
    print(row.prettify())
