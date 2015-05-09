import requests

def bookinfo():
    lis = []
    isbns = [9781405882613, 9780593072493,9780679444817,9780553275728,9780521397346,9781573928335]
    for isbn in isbns:
        res = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+str(isbn))
        res = res.json()     
        title = res['items'][0]['volumeInfo']['title']
        #cover= "http://www.librarything.com/devkey/KEY/large/isbn/"+str(isbn)
        cover =res['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        author = res['items'][0]['volumeInfo']['authors'][0]
        category = res['items'][0]['volumeInfo']['categories'][0]
        lis.append((title,cover,author,category))
    return lis
        
            


