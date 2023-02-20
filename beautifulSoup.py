# # HTML is the language that is compiled by the browser

# # Parse -> Filter Out
import csv
import requests
from bs4 import BeautifulSoup

code = requests.get("https://www.worldometers.info/coronavirus/")
raw_code = code.text
url = BeautifulSoup(raw_code, "html.parser")

all_data = []
table_code = url.table
tags = table_code.find_all("tr")
final_data=[]
for i in tags:
    all_data.append(i.text.split("\n"))
for i in all_data:
    if i[1]!="":
        final_data.append(i[1:])
        
# print(all_data)

# file=open("covid_data_final.csv","w")
# x=csv.writer(file)
# x.writerows(final_data)
# file.close()

import pandas as pd
df=pd.read_csv("covid_data_final.csv",encoding="latin1", index_col="#")
# print(df)

x=list(df["Country,Other"])
y=list(df["TotalCases"])
ya= list(df["Total"])
y1=list(map(lambda y:int(y.replace(",","")),y))[1:20]
y2= list(map(lambda y:int(y.replace(",","")),ya))[1:20]
print(y2)
# import plotly.graph_objects as go
# fig= go.Figure([go.Bar(name="TotalCases",x=x,y=y1),
#                 go.Bar(name="TotalDeaths", x=x,y=y2)])
# fig.show()