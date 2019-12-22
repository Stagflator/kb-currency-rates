import requests

from bs4 import BeautifulSoup
import pandas as pd

url = "https://kapitalbank.az/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
th_elems = soup.find_all("th")
td_elems = soup.find_all("td")

curr = [th.text for th in th_elems[0:4]]
columns = [td.text for td in td_elems[0:4]]
rowsusd = [td.text for td in td_elems[5:9]]
rowseur = [td.text for td in td_elems[9:13]]
rowsrub = [td.text for td in td_elems[13:18]]

data = {
    columns[0]: curr,
    columns[1]: [rowsusd[0], rowseur[0], rowsrub[0]],
    columns[2]: [rowsusd[1], rowseur[1], rowsrub[1]],
    columns[3]: [rowsusd[2], rowseur[2], rowsrub[2]]
}

data2 = pd.DataFrame(data)

