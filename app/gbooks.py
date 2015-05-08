import requests

def bookinfo(isbn):
    try:

        res = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn)
        res = res.json()
      
        title = res['items'][0]['volumeInfo']['title']
        cover= "http://www.librarything.com/devkey/KEY/large/isbn/"+isbn
            #image =res['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']
        author = res['items'][0]['volumeInfo']['authors'][0]
        return (title,cover,author)
    except:
        return None
            


