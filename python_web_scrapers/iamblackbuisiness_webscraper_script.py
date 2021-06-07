from bs4 import BeautifulSoup
import requests
import re
import csv

url = "https://iamblackbusiness.com/businesses.php?filter=state%7CAL&sort="

page = requests.get(url)  # sets url to variable html

# good : titles
title_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
titles = bsObj.find_all('h3', {"class": "property-title"})
for title in titles:
    line = title.text
    line = line.strip()
    line = re.sub('\n', '', line)
    title_list.append(line)

# good : locations
location_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
locations = bsObj.find_all('div', {"class": "location"})
for location in locations:
    line = location.text
    line = line.strip()
    line = re.sub('\n\t', '', line)
    location_list.append(line)

# good : descriptions
description_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
descriptions = bsObj.find_all('div', {"class": "description"})
for description in descriptions:
    line = description.text
    line = line.strip()
    line = re.sub('\n\t', '', line)
    description_list.append(line)

# good : phone
phone_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
phones = bsObj.find_all('div', {"class": "iabb-reset-pull-right social pull-right"})
for phone in phones:
    line = phone.text
    line = line.strip()
    line = re.sub('\n\t', '', line)
    phone_list.append(line)

# good : website
website_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
websites = bsObj.find_all('a', {'title': 'Website'})
for website in websites:
    website_url = website.get('href')
    if website_url not in website_list:
        website_list.append(website_url)

# good : email
email_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
emails = bsObj.find_all('a', {"title": "Email"})
for email in emails:
    email_list.append(email.get('href'))

# good : twitter
twitter_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
twitters = bsObj.find_all('a', {"title": "Twitter"})
for twitter in twitters:
    twitter_list.append(twitter.get('href'))

# good : facebook
facebook_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
facebooks = bsObj.find_all('a', {"title": "Facebook"})
for facebook in facebooks:
    facebook_list.append(facebook.get('href'))

# good : linkedin
linkedin_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
linkedins = bsObj.find_all('a', {"title": "LinkedIn"})
for linkedin in linkedins:
    linkedin_list.append(linkedin.get('href'))

# good : youtube
youtube_list = []
html_contents = page.text
bsObj = BeautifulSoup(html_contents, "html.parser")
youtubes = bsObj.find_all('a', {"title": "youtube"})
for youtube in youtubes:
    youtube_list.append(youtube.get('href'))

# standardize all list length
targets = [title_list, location_list, phone_list, description_list, email_list, twitter_list, facebook_list,
           linkedin_list, youtube_list, website_list]
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

# rough execution, information aligned on one row, some checking and correction likely needed
with open('I_am_black_business.csv', 'w') as I_am_black_business:
    file_writer = csv.writer(I_am_black_business, delimiter=',')

    # The First row for naming the items
    categories = ['Titles', "Locations", "Phone Numbers", 'Descriptions', 'Emails', 'Twitter', 'Facebook',
                  'Linkedin', 'Youtube', 'Website']
    file_writer.writerow(categories)

    count = 0
    while count < len(title_list):
        targets = [title_list[count], location_list[count], phone_list[count], description_list[count],
                   email_list[count],
                   twitter_list[count], facebook_list[count], linkedin_list[count], youtube_list[count],
                   website_list[count]]
        file_writer.writerow(targets)
        count = count + 1

# Testing -------------------------------------------------------------------------------------

# print(bsObj)
# print(max_length, "max length")
# print(len(title_list), "title length")
# print(len(location_list), "title length")
# print(len(description_list), "description length")
# print(len(phone_list), "phone length")
# print(len(website_list), "website length")
# print(len(email_list), "email length")
# print(len(twitter_list), "twitter length")
# print(len(facebook_list), "facebook length")
# print(len(linkedin_list), "linkedin length")
# print(len(youtube_list), "youtube length")
