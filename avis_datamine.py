import bs4
import csv

page = open('scrapedpage.html','r')
soup = bs4.BeautifulSoup(page, 'lxml')

headings = soup.find_all('h3')
counters = soup.find_all('p', attrs={'class' : 'payamntp'})
# print(headings)


output1 = [] #for each heading
output2 = [] #for each counter price
output3 = [] #for each pay now price



for heading in headings:
    output1.append(heading.text)

for counter in counters:
    output2.append(counter.text)

# print(output2)

rows = zip(output1,output2,output3)

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
         writer.writerow(row)


# for heading in headings:
#     output.append(heading.text)


# print(output1)
