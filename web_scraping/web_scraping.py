import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
print(response.text)
print(response.request.headers)
print(response.headers)

page = BeautifulSoup(response.text, 'html.parser')
print(page.title)
print(page.title.string)
print(page.find_all('h3'))

link_section = page.find('a', attrs={'name': 'links'})
section = []
for element in link_section.next_elements:
    if element.name == 'h3':
        break
    section.append(element.string or '')

print(section)
print(page.find_all(re.compile('^h(2|3)')))



