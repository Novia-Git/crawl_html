import requests
from bs4 import BeautifulSoup
import pandas as pd
res = requests.get("http://www.freebookspot.es/topten.aspx?Category_ID=163")
soup = BeautifulSoup(res.text,'html.parser')
soup.select('b')

books = pd.Series()
for book in soup.select("b"):
    books = books.append(pd.Series([book.text])).reset_index(drop=True)

books = books[11:]

bkn = pd.Series()
for i in range(1,len(books),2):
    bkn = bkn.append(pd.Series([books.values[i]])).reset_index(drop=True)
print(bkn)




