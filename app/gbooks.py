import requests

def bookinfo(books):
    lis = []
    for book in books:
        res = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+book.isbn)
        res = res.json()
        title = res['items'][0]['volumeInfo']['title']
        image = "http://www.librarything.com/devkey/KEY/large/isbn/"+book.isbn
        #image =res['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']
        author = res['items'][0]['volumeInfo']['authors'][0]
        lis.append((title,image,author))
    return lis



