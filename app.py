import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

productname = []
price = []
Reviews = []
Description = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


for i in range(1,11):  # page 1 se 4
    url = f"https://www.flipkart.com/search?q=mobiles+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_19_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_19_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=mobiles+under+50000%7CMobiles&requestId=81e90208-d48d-474b-a3e0-f49ce0b68a36&as-searchtext=mobiles+under+50000&page={i}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    box = soup.find("div",class_ ="QSCKDh dLgFEE")
    names = box.find_all("div",class_="RG5Slk")
    for n in names:
                name = n.text
                productname.append(name)
                
    print(len(productname))
    prices = box.find_all("div",class_="hZ3P6w DeU9vF")
    for n in prices:
                name = n.text
                
                price.append(name)
                
    print(len(price))

    reviews = box.find_all("div",class_="MKiFS6")
    for n in reviews:
                name = n.text
               
                Reviews.append(name)
                
    print(len(Reviews))

    description = box.find_all("ul",class_="HwRTzP")
    for n in description:
                name = n.text
                Description.append(name)
                
    print(len(Description))
    time.sleep(2)

df = pd.DataFrame({'Product_Name':productname,'Product_Price':price,'Product_Desc':Description,'Product_Reviews':Reviews})
print(df)




   

    