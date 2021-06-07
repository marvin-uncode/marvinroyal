from bs4 import BeautifulSoup
import requests
import re
import csv
import sys

url = "https://www.nationalblackguide.com/black-directory/alabama"

page = requests.get(url)  # sets url to variable html

# good : titles
title_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
titles = bsObj.find_all('a', {"class": "summary-title"})
for title in titles:
    title_list.append(title.text)

# good : items
item_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
items = bsObj.find_all('a', {"class": "summary-categories-item"})
for item in items:
    item_list.append(item.text)

# good : phone
phone_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
phones = bsObj.find_all('a', {"class": "summary-phone"})
for phone in phones:
    phone_list.append(phone.text)

# good : locations
address_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
addresses = bsObj.find_all('div', {"class": "summary-address"})
for address in addresses:
    line = address.text
    line = line.strip()
    line = re.split('\n', line)
    address_list.append(line[0])

# good : websites
website_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
websites = bsObj.find_all('a', {'class': 'visit-website summary-actions-item'})
for website in websites:
    website_url = website.get('href')
    if website_url not in website_list:
        website_list.append(website_url)

# standardize all list length
targets = [title_list, item_list, address_list, phone_list, website_list]
max_length = max([len(i) for i in targets])
for target in targets:
    count = 0
    diff = max_length - len(target)
    if diff > 0:
        while count != diff:
            target.append("None")
            count += 1
    else:
        continue


# rough execution, data is paired to one row and semi-correlates, would need reorganizing
with open('national_black_guide.csv', 'w') as national_black_guide:
    file_writer = csv.writer(national_black_guide, delimiter=',')

    # The First row for categories
    categories = ['Titles', "Items", "Address", 'Websites']
    file_writer.writerow(categories)

    count = 0
    while count < len(title_list):
        targets = [title_list[count], item_list[count], address_list[count], website_list[count]]
        file_writer.writerow(targets)
        count = count + 1

# Testing -------------------------------------------------------------------------------------

# print(len(title_list), " title length")
# print(len(item_list), " items length")
# print(len(phone_list), " phone length")
# print(len(address_list), " address length")
# print(len(website_list), " website length")

