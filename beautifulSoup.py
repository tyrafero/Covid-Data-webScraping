# # HTML is the language that is compiled by the browser

# # Parse -> Filter Out
# import requests

# from bs4 import BeautifulSoup
# url= BeautifulSoup("https://www.worldometers.info/coronavirus/","html.parser")
# code=requests.get(url)
# raw_code= code.text
# raw_code=BeautifulSoup(raw_code,"lxml")
# # print(type(raw_code))

# all_data=[]
# table_code= raw_code.table
# tags= table_code.find_all("tr")
# for i in tags:
#     all_data.append(i.text.split("\n"))
# print(all_data)

# import csv
# import requests
# from bs4 import BeautifulSoup

# code = requests.get("https://www.worldometers.info/coronavirus/")
# raw_code = code.text
# url = BeautifulSoup(raw_code, "html.parser")

# all_data = []
# table_code = url.table
# tags = table_code.find_all("tr")
# final_data=[]
# for i in tags:
#     all_data.append(i.text.split("\n"))
# for i in all_data:
#     if i[1]!="":
#         final_data.append(i[1:])
        
# print(all_data)

# file=open("covid_data_final.csv","w")
# x=csv.writer(file)
# x.writerows(final_data)
# file.close()

import pandas as pd
df=pd.read_csv("covid_data_final.csv",encoding="latin1")
print(df)