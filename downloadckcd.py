import requests, os, bs4
 url="http://xkcd.com"
 os.makedirs('xkcd', exist_ok=True)
while not url.endwith ('#')
#TODO: download the page
# TODO: download the image
# TODO: Save the img to /.xkcd
#TODO: Get the Prev button's url.

print('DOwnloading page %s... % url)
res= requests.get(url)
res.raise_for_status()
print ('Done')
