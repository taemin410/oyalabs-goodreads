import requests
import json
import xml.etree.ElementTree as ET
import xmltodict
import pandas as pd
from bs4 import BeautifulSoup

def getAuthorInfo(authorID):
    task = {'key': 'bstCFbTaNVLqw8aLyq3ikQ', 'id': authorID
            }

    keys=json.dumps(task)

    resp = requests.get('https://www.goodreads.com/author/list.xml', json=task)
    if resp.status_code != 200:
        # This means something went wrong.
        print (resp.status_code)

    #print (resp.text)
    # print (type(resp))

    xpars = xmltodict.parse(resp.text)
    jsons = json.dumps(xpars)
    print(jsons)


# tree = ET.fromstring(resp.text)
#
# for child in tree:
#     print(child.tag, child.attrib)
#
# for neighbor in tree.iter('book'):
#     print(neighbor.attrib)

# root = tree.getroot()
# for child in root:
#     print(child.tag, child.attrib)

# y = json.loads(resp)

def searchQueryByString(query):

    task = {'key': 'bstCFbTaNVLqw8aLyq3ikQ',
            'q': query

            }
    resp = requests.get("https://www.goodreads.com/search/index.xml", task )

    if resp.status_code != 200:
        # This means something went wrong.
        print (resp.status_code)

    #print(resp.text)

    contents = resp.text
    soup = BeautifulSoup(contents, 'xml')
    try:
        titles = soup.find_all('id')[1]
        for title in titles:
            print(title)
            return title
    except:
        return 404

searchQueryByString("Chicka Chicka Boom Boom (Paperback)")


def getBookByISBN(ISBN):

    #ISBN in string
    task = {'key': 'bstCFbTaNVLqw8aLyq3ikQ',
            'q': ISBN
            }
    keys=json.dumps(task)


    resp= requests.get("https://www.goodreads.com/search/index.xml", keys)
    if resp.status_code != 200:
        # This means something went wrong.
        print (resp.status_code)

    print(resp.text)

#
def searchByISBN(isbn):

    task = {'key': 'bstCFbTaNVLqw8aLyq3ikQ', 'format': 'xml' ,  'isbn' : isbn
            }

    resp= requests.get("https://www.goodreads.com/book/isbn/", params=task)
    if resp.status_code != 200:
        # This means something went wrong.
        print (resp.status_code)

    # print(resp.text)
    xpars = xmltodict.parse(resp.text)
    jsons = json.dumps(xpars, indent=4, sort_keys=True)
    print(jsons)

    a= pd.read_json(jsons)

    a.to_csv("test.csv")

def searchByGoodreadsID(bookid):

    task = {'key': 'bstCFbTaNVLqw8aLyq3ikQ', 'format': 'xml' ,  'id' : bookid
            }

    resp= requests.get("https://www.goodreads.com/book/show", params=task)
    if resp.status_code != 200:
        # This means something went wrong.
        print (resp.status_code)

    #print(resp.text)
    contents = resp.text
    soup = BeautifulSoup(contents, 'xml')
    isbn = soup.find_all('isbn')
    isbn13 = soup.find_all('isbn13')

    return isbn, isbn13


searchByGoodreadsID("24875389")
