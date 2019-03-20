from bs4 import BeautifulSoup
import requests
import pandas as pd
from goodreadsapi import *
import re

def getBookTitles0():
    textContent = []
    # isbnlist=[]
    # isbn13list=[]
    for j in range(1,26):
        pagelink = "https://www.goodreads.com/shelf/show/pre-k?page="+str(j)

        page_response = requests.get(pagelink, timeout=5)

        page_content = BeautifulSoup(page_response.content, "html.parser")
        paragraphs = page_content.find_all("a", attrs={"class": "bookTitle"})
        #print(paragraphs)
        print(j)

        for i in range(0, 50):

            try:
                title = paragraphs[i]
                #print(title.text)

                booktitle= re.sub(r" ?\([^)]+\)", "", title.text)
                # bookid = searchQueryByString(booktitle)
                # isbn, isbn13 = searchByGoodreadsID(bookid)

                booktitle = booktitle.strip("\n\r")
                textContent.append(booktitle)
                # isbnlist.append(isbn)
                # isbn13list.append(isbn13)
            except:
                print("error in list retrieve" + str(i) + "index of "+ str(j))

    df= pd.DataFrame(
        {'BookTitles': textContent
         # 'isbn': isbnlist,
         # 'isbn13': isbn13list
        })
    df.to_csv("tttt.csv")

getBookTitles0()

def getBookTitles1():
    textContent = []
    # isbnlist=[]
    # isbn13list=[]
    for j in range(1,45):
        pagelink = "https://www.goodreads.com/list/show/86.Best_Children_s_Books?page="+str(j)

        page_response = requests.get(pagelink, timeout=5)

        page_content = BeautifulSoup(page_response.content, "html.parser")
        paragraphs = page_content.find_all("a", attrs={"class": "bookTitle"})
        #print(paragraphs)
        for i in range(0, 100):

            try:
                title = paragraphs[i]
                #print(title.text)

                booktitle= re.sub(r" ?\([^)]+\)", "", title.text)
                # bookid = searchQueryByString(booktitle)
                # isbn, isbn13 = searchByGoodreadsID(bookid)

                booktitle = booktitle.strip("\n\r")
                textContent.append(booktitle)
                # isbnlist.append(isbn)
                # isbn13list.append(isbn13)
            except:
                print("error in list retrieve" + str(i) + "index of "+ str(j))

    df= pd.DataFrame(
        {'BookTitles': textContent
         # 'isbn': isbnlist,
         # 'isbn13': isbn13list
        })
    df.to_csv("Best_Children_s_Books.csv")

def getBookTitles2():
    textContent = []
    # isbnlist=[]
    # isbn13list=[]
    for j in range(1,26):
        pagelink = "https://www.goodreads.com/list/show/460.Best_Picture_Books?page="+str(j)

        page_response = requests.get(pagelink, timeout=5)

        page_content = BeautifulSoup(page_response.content, "html.parser")
        paragraphs = page_content.find_all("a", attrs={"class": "bookTitle"})
        #print(paragraphs)
        print(j)
        for i in range(0, 100):

            try:
                title = paragraphs[i]
                #print(title.text)

                booktitle= re.sub(r" ?\([^)]+\)", "", title.text)
                # bookid = searchQueryByString(booktitle)
                # isbn, isbn13 = searchByGoodreadsID(bookid)

                booktitle = booktitle.strip("\n\r")
                textContent.append(booktitle)
                # isbnlist.append(isbn)
                # isbn13list.append(isbn13)
            except:
                print("error in list retrieve" + str(i) + "index of "+ str(j))

    df= pd.DataFrame(
        {'BookTitles': textContent
         # 'isbn': isbnlist,
         # 'isbn13': isbn13list
        })
    df.to_csv("Best_Picture_Books.csv")

def getBookTitles3():
    textContent = []
    # isbnlist=[]
    # isbn13list=[]
    for j in range(1,16):
        pagelink = "https://www.goodreads.com/list/show/621.Best_children_s_books_EVER?page="+str(j)

        page_response = requests.get(pagelink, timeout=5)

        page_content = BeautifulSoup(page_response.content, "html.parser")
        paragraphs = page_content.find_all("a", attrs={"class": "bookTitle"})
        #print(paragraphs)
        print(j)
        for i in range(0, 100):

            try:
                title = paragraphs[i]
                #print(title.text)

                booktitle= re.sub(r" ?\([^)]+\)", "", title.text)
                # bookid = searchQueryByString(booktitle)
                # isbn, isbn13 = searchByGoodreadsID(bookid)

                booktitle = booktitle.strip("\n\r")
                textContent.append(booktitle)
                # isbnlist.append(isbn)
                # isbn13list.append(isbn13)
            except:
                print("error in list retrieve" + str(i) + "index of "+ str(j))

    df= pd.DataFrame(
        {'BookTitles': textContent
         # 'isbn': isbnlist,
         # 'isbn13': isbn13list
        })
    df.to_csv("Best_children_s_books_EVER.csv")


def getBookTitles4():
    textContent = []
    # isbnlist=[]
    # isbn13list=[]
    for j in range(1,7):
        pagelink = "https://www.goodreads.com/list/show/591.Voices_Sounds_Best_Read_Alouds_for_Young_Children?page="+str(j)

        page_response = requests.get(pagelink, timeout=5)

        page_content = BeautifulSoup(page_response.content, "html.parser")
        paragraphs = page_content.find_all("a", attrs={"class": "bookTitle"})
        #print(paragraphs)
        print(j)
        for i in range(0, 100):

            try:
                title = paragraphs[i]
                #print(title.text)

                booktitle= re.sub(r" ?\([^)]+\)", "", title.text)
                # bookid = searchQueryByString(booktitle)
                # isbn, isbn13 = searchByGoodreadsID(bookid)

                booktitle = booktitle.strip("\n\r")
                textContent.append(booktitle)
                # isbnlist.append(isbn)
                # isbn13list.append(isbn13)
            except:
                print("error in list retrieve" + str(i) + "index of "+ str(j))

    df= pd.DataFrame(
        {'BookTitles': textContent
         # 'isbn': isbnlist,
         # 'isbn13': isbn13list
        })
    df.to_csv("Voices_Sounds_Best_Read_Alouds_for_Young_Children.csv")



# isbnlist=[]
# isbn13list=[]
#
# df = pd.read_csv("books.csv")
# # bookid = searchQueryByString(booktitle)
# # isbn, isbn13 = searchByGoodreadsID(bookid)
# for index, row in df.iterrows():
#     #print(row["Popular Pre K Books title"])
#     booktitle = re.sub(r" ?\([^)]+\)", "", row["Popular Pre K Books title"])
#
#     bookid=searchQueryByString(booktitle)
#
#     print("BOOK ID IS : " + bookid)
#     if bookid == None or bookid == 404 :
#         print("Exception!!")
#         isbn, isbn13 = None, None
#     else:
#         isbn, isbn13 = searchByGoodreadsID(bookid)
#
#
#     isbnlist.append(isbn)
#     isbn13list.append(isbn13)
#
# df['isbn']=isbnlist
# df['isbn13']=isbn13list
#
# print(df.head())
#
#



# html_str = "<html><div> </div> </html>"
#
# bsObj = bs4.BeautifulSoup(html_str, "html.parser")

# print (type(bsObj))
# print (bsObj)
# print (bsObj.find("div"))


