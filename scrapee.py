#https://en.wikipedia.org/wiki/States_and_union_territories_of_India
import urllib2
wiki = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"
page = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
print soup.prettify
soup.title
soup.title.string
all_links = soup.find_all("a")
for link in all_links:
    print link.get("href")
all_tables=soup.find_all('table')
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
df


 
