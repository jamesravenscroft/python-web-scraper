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


pElems= exampleSoup.select('p')
str(pElems[0])
'<p>Download my <strong> Python</strong> book from <a href=:http//inventwithoython.com">my website</a></p>'
pElems[0[.getText()
         Download my Python book from my website.'
         str(pElems[1])
         <p class="slogan">L earn Python the easy way!</p>'
         pElems[1].getText()
         'Learn Python the easy way!'
         str(pElems[2])
         <p>By <span id =ahother> JR3</span></p>
         pElems[2].getText()
