from bs4 import BeautifulSoup
import requests
import openpyxl as op

URL ='http://books.toscrape.com/catalogue/page-'

wb = op.Workbook()
sheet = wb.active
sheet.title = 'Popular books'
sheet.append(['Book Name','Book Price','Book Availability'])

for page in range(1,51):
    path = URL + str(page) + '.html'
    print(path)

    source = requests.get(URL + str(page) + '.html')


    # source = requests.get('http://books.toscrape.com').text
    soup = BeautifulSoup(source.text, 'html.parser')


    books = soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})


    for book in books:
        b = []
        name = book.h3.a['title']
        price= book.findAll("p", {"class": "price_color"})[0].text
        stock_avail=book.findAll("p", {"class": "instock availability"})[0].text.strip()

        print(name)
        print(price)
        print(stock_avail)
        b.append(name)
        b.append(price)
        b.append(stock_avail)

        sheet.append(b)
        print()

    wb.save('Book Info.xlsx')





