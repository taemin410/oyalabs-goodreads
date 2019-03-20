import urllib.request
import bs4


url = "https://www.naver.com/"

html = urllib.request.urlopen(url)

bsobj = bs4.BeautifulSoup(html, "html.parser")



# print (html.read())
# print (bsobj)
#

top_right = bsobj.find("div", {"class" : "area_links"})

find_a = top_right.find("a")

print (find_a.text)
