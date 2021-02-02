from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


html_text =requests.get('https://covid.gov.pk/').text
soup =BeautifulSoup(html_text, 'lxml')

status =soup.find('ul', class_='top-statistics block-separator without-activecases print-in-dashboard')

totalStatusInPK=status.find_all('li')

totalList=[]
titleList=[]


for index, tags in enumerate(totalStatusInPK):

    total =int(status.find_all('li')[index].span.text.replace(',',''))
    title =status.find_all('label')
    title =title[index].text

    totalList.append(total)
    titleList.append(title)



data =[]
for i in range(0,20):
    data.append(totalList)




df =pd.DataFrame(data,columns=['Confirmed_Cases', 'Deaths', 'Recovered', 'Total_Tests', 'Critical_Cases'] )
df.to_csv('Data/C19.csv')
print(df)





# with open('Data/newCovidData.csv', mode='a') as csv_file:
#
#     header=titleList
#     csv_writer =csv.writer(csv_file)
#
#     # csv_writer.writerow(header)
#     csv_writer.writerow(totalList)
