import bs4
import csv

page = open('scrapedpage2.html','r')
soup = bs4.BeautifulSoup(page, 'lxml')

headings = soup.find_all('h3')
counters = soup.find_all('p', attrs={'class' : 'payamntp'})
currents = soup.find_all('p', attrs={'class' : 'payamntr'})
# print(headings)


output1 = [] #for each heading
output2 = [] #for each counter price
output3 = [] #for each pay now price



for heading in headings:
    output1.append(heading.text)

for counter in counters:
    output2.append(counter.text)

for current in currents:
    output3.append(current.text)

# print(output2)

rows = [output1,output2,output3]

# with open('output.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(("output1", "output2"))
#     for row in rows:
#          writer.writerow(row)


with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(rows)


# for heading in headings:
#     output.append(heading.text)


# print(output1)
