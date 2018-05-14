#249, doesn't work because we need to download beautiful soup
import requests, sys, webbrowser, bs4
print('Googling...')
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.beautifulSoup(res.text)
linkElems = soup.select('.r a')
numOpen = min(f, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
    
