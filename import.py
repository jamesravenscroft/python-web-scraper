 import bs4
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
<span id="author">JR3</span>'
spanElem.get('id')
'author'
spanElem.get('some_nonexistent_addr')== None
True
spanElem.attrs
{'id': 'author'}
