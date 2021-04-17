import os
import pandas as pd

#url = 'https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html'

dirname = "C:\\Users\\oguzh\\Downloads\\" 
script_dir = os.path.dirname(dirname)
file_path = os.path.join(script_dir, 'Genel Koronavirüs Tablosu.html')
#tr-cities-utf8.json

html = open(file_path,'r',encoding='UTF-8')
source_code = html.read()
df = pd.read_html(source_code)
df = df[0].dropna(axis=0, thresh=4)
print(df)

#Run this to save it to a csv
#for i, table in enumerate(df):
    #df.to_csv('Covid-Turkey.csv','a')
